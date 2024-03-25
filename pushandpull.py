import os

#원하는 directory 를 아래에 적어주세요.
dir_list = [
    # "C:/Users/SSAFY/Desktop/LUCAS/my-web-front/", # front 수업 자료
    # "C:/Users/SSAFY/Desktop/LUCAS/my-web-back/", # Back 수업 자료
    # "C:/Users/SSAFY/Desktop/LUCAS/algorithm/", # Haley쌤 과제
    "C:/Users/SSAFY/Desktop/LUCAS/Dohyungh/", # Dohyungh
    "C:/Users/SSAFY/Desktop/LUCAS/Lucas-workspace/", # live 수업 java workspace
    # "C:/Users/SSAFY/Desktop/LUCAS/Lucas-workspace-STS4/", # live 수업 STS workspace
    "C:/Users/SSAFY/Desktop/LUCAS/Algorithm-workspace/", # 자습용 java workspace
    "C:/Users/SSAFY/Desktop/LUCAS/TIL/", # Live 필기(대부분)
    "C:/Users/SSAFY/Desktop/LUCAS/6630_Algorithm_study/", # 6630 스터디 자료
    # "C:/Users/SSAFY/Desktop/LUCAS/web-spring/my-web-spring", # live Spring
    # "C:/Users/SSAFY/Desktop/LUCAS/live-db/my-live-db", # live DB
    "C:/Users/SSAFY/Desktop/LUCAS/PJT-Clustering-KOSPI200" # 코스피 클러스터링 플젝
]

def push():
    count = 0
    for dirs in dir_list :
        count+=1
        os.chdir(dirs)
        message = input(dirs + "\n"+"에 입력할 Commit 메시지를 입력하세요.({}/{}) :".format(count,len(dir_list)))


        if dirs =="C:/Users/SSAFY/Desktop/LUCAS/6630_Algorithm_study/" : #혹시 branch를 따로 파서 관리하는 레포가 있다면 여기 넣어주세요
            os.system("git checkout Dohyungh")
            os.system("git add .")
            os.system("git commit -m \"{}\"".format(message))
            os.system("git push origin Dohyungh")
        else:
            os.system("git add .")
            os.system("git commit -m \"{}\"".format(message))
            os.system("git push origin master")

    print("-----------------------------------------------------푸시가 끝났습니다.")

def pull():
    count = 0
    for dirs in dir_list :
        count+=1
        os.chdir(dirs)
        os.system("git pull origin master")

    print("풀이 끝났습니다.")

def main():

    request = input("풀 받으려면 \"pull\", 푸시 하려면 \"push\"를 입력하세요. :")

    if request == 'pull':
        pull()

    elif request == 'push':
        push()

if __name__ == "__main__":
    main()