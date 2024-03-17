import random
from itertools import cycle

class All_Cards:
    # number (space) type
    def generate():
        all_cards = [
        '1 gwang', '1 tti', '1 pee', '1 pee',
        '2 meong', '2 tti', '2 pee', '2 pee',
        '3 gwang', '3 tti', '3 pee', '3 pee',
        '4 meong', '4 tti', '4 pee', '4 pee',
        '5 meong', '5 tti', '5 pee', '5 pee',
        '6 meong', '6 tti', '6 pee', '6 pee',
        '7 meong', '7 tti', '7 pee', '7 pee',
        '8 gwang', '8 meong', '8 pee', '8 pee',
        '9 dpee', '9 tti', '9 pee', '9 pee',
        '10 meong', '10 tti', '10 pee', '10 pee',
        '11 gwang', '11 dpee', '11 pee', '11 pee',
        '12 gwang', '12 meong', '12 tti', '12 dpee'
        ]
        random.shuffle(all_cards)
        return all_cards


class Cards:
    def __init__(self):
        self.gwang = []
        self.meong = []
        self.tti = []
        self.pee = []

    def append(self, card):
        month, type = card.split(' ')
        if type == 'gwang':
            self.gwang.append(month)
        elif type == 'meong':
            self.meong.append(month)
        elif type == 'tti':
            self.tti.append(month)
        elif type == 'pee':
            self.pee.append(month)
        elif type == 'dpee':
            self.pee.append(month)
            self.pee.append(month)

    def get_score(self, me, other, others_cards):
        score = 0
        score += self.score_gwang()
        score += self.score_tti()
        score += self.score_meong()
        score += self.score_pee()
        if score >=7:
            if (self.score_gwang() != 0) and (score >=7) and (not others_cards.gwang) : 
                score *= 2 # 광박
            if (self.score_pee() != 0) and (score >=7) and (len(others_cards.pee)<=5) : 
                score *= 2 # 피박
            if other.go !=0 :
                score *= 2 # 고박
            if len(self.meong) >= 7 :
                score *= 2 # 멍박
            if me.shaked :
                score *= 2 # 흔들기

        return score
        
    def score_gwang(self):
        if len(self.gwang) == 3:
            if 12 in self.gwang:
                return 2
            else:
                return 3
        elif len(self.gwang) == 4:
            return 4
        elif len(self.gwang) ==5:
            return 15
        return 0
    
    def score_tti(self):
        score = 0
        if len(self.tti) >=5:
            score += len(self.tti) - 4
        
        dan = [[1,2,3],[4,5,7],[6,9,10]]
        for d in dan:
            flag = 1
            for i in d:
                if i not in self.tti:
                    flag = 0
            if flag == 1:
                score += 3
        return score
    
    def score_meong(self):
        score = 0
        if len(self.meong) >= 5 :
            score += len(self.meong) - 4
        flag = 1
        for i in [2,4,8]:
            if i not in self.meong:
                flag = 0
        if flag ==1:
            score +=5
        return score
    
    def score_pee(self):
        if len(self.pee) >=10:
            return len(self.pee) - 9
        return 0
    

class Player:
    def __init__(self):
        self.hands = []
        self.isfirst = False
        self.shaked = False #흔들었는지 여부
        self.go = 0 # 고한 횟수
        self.cards = Cards()

    def set_first(self):
        self.isfirst = True
    def set_second(self):
        self.isfirst = False   
    
    
    def set_hands(self, hands):
        self.hands = hands

    def drop_card(self, idx):
        return self.hands.pop(idx)
    
    def shake(self):
        self.shaked = True

    




def start():
    all_cards = All_Cards.generate()

    global me, opponent
    me = Player()
    opponent = Player()
    
    players = cycle([me, opponent])

    for _ in range(2): # 초기 세팅
        player = next(players)
        hnd = []
        for __ in range(10):
            card = all_cards.pop()
            hnd.append(card)
        player.set_hands(hnd)
        flr = []
        for __ in range(8):
            card = all_cards.pop()
            flr.append(card)

    global floor
    floor = flr

    global dummys
    dummys = all_cards
    

def play(me, opponent):
    if me.isfirst :
        players = cycle([me, opponent])
    else : 
        players = cycle([opponent, me])
##################
    while True:
        turn = next(players)
        drop_index = random.randint(0,len(turn.hands))
        dropped_card = turn.drop_card(drop_index)
        month, type = dropped_card.split(' ')

        cnt = 0
        for i in range(len(floor)):
            if floor[i][0] == month :
                cnt+=1
        if cnt == 0:
            floor.append(dropped_card)
        elif cnt == 1:
            floor.pop()
###################



    return None


def score():
    winner = [0].index(max([0])) # 나중에 수정

    first = winner
    

        
def main():
    start()
    play(me, opponent)
    score()


if __name__ == '__main__':
    main()

#상대 카드 예측 필요할듯
#   현재 오픈된 카드를 모두 제외한 다음,
#   여태까지의 상대 플레이를 바탕으로 예측. 여기서 상대 플레이란 상대 턴에 floor 와 그때 낸 카드로.
#   상대가 바닥을 쳤다면 더 명확하게 예측할 수 있겠지.
#floor, 각자의 cards, 나의 hands, 상대 카드 예측, 이 4개를 가지고 확률이 높은 걸 고르도록.
#확률 계산은 Monte carlo sampling 방식?