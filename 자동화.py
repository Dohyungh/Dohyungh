import os
import shutil
import inspect

#글처음에서 끝까지 잘 복붙할 것.
#ws 에는 -# 가 있고, hw에는 없음.
#이 파이썬 파일 옆에 .gitignore를 복사해서 놔주세요.
오늘의_과제 = """온실_Java_10_ws_02:"""
깃랩유저네임 = "bley1217" #user_name
깃랩이메일 = "bley1217@gmail.com" #user_email
상위_폴더 = "C:/Users/SSAFY/Desktop/오늘의미션" #directory

def clone():            
    text = 오늘의_과제
    user_name = 깃랩유저네임
    directory = 상위_폴더

    #전처리해서 과제 목록(job_list) 만들기 ex) ["ws","01","3","2"]
    job_list = []

    for i in range(len(text)):
        # :가 기준임
        if text[i]==":":
            for j in range(i-9,i):

                if text[j:j+2]=="ws":
                    date = text[j-3:j-1]
                    level = text[j+3:j+5]
                    flag = text[j+6:j+7]
                    job_list.append(["ws",date,level,flag])
                    break

                if text[j:j+2]=="hw":
                    date = text[j-3:j-1]
                    level = text[j+3:j+5]
                    job_list.append(["hw",date,level])
                    break

    #클론받을 싸피 깃 주소
    URL = "https://lab.ssafy.com/{}/{}".format(user_name,subject)
    
    #0n_subject 폴더 생성
    createFolder(directory+"/{}_{}".format(date,subject))

    #git clone
    os.chdir(directory+"/{}_{}".format(date,subject))
    need_to_del = ['/bin','.classpath','.project']
    for i in need_to_del:
        if os.path.isfile('./{}'.format(i)):
            os.remove('./{}'.format(i))

    for i in range(len(job_list)):
        if len(job_list[i]) ==3:
            temp = str(int(job_list[i][2]))
        
        elif len(job_list[i]) ==4:
            if job_list[i][3] ==1:
                temp = str(int(job_list[i][2])) #1,2,3,4,5

            elif job_list[i][3] ==2:
                temp = chr(ord("`")+int(job_list[i][2])) #a,b,c

            temp = str(int(job_list[i][2]))
            os.system("git clone {}_{}_{}_{}.git".format(URL,job_list[i][0],job_list[i][1],temp))

    # 폴더 순회하면서 .gitignore 붙여넣기
    dir_list = []

    for folder in os.listdir(directory+"/{}_{}/".format(date,subject)):
        if (os.path.isdir(directory+"/{}_{}/".format(date,subject)+folder) and folder != 'bin'): # 원하는 ""폴더""만 선택
            dir_list.append(directory+"/{}_{}/".format(date,subject)+folder+'/.gitignore')

    for i in dir_list:
        shutil.copy(start_dir+'\.gitignore',i)
    

def push():
    text = 오늘의_과제
    user_name = 깃랩유저네임
    user_email = 깃랩이메일
    directory = 상위_폴더
    #text에서 date만 가져오기
    for i in range(len(text)):
        if text[i]==":":
            for j in range(i-9,i):
                if text[j:j+2]=="ws":
                    date = text[j-3:j-1]
                if text[j:j+2]=="hw":
                    date = text[j-3:j-1]

    #원하는 directory update
    dir_list = []

    for folder in os.listdir(directory+"/{}_{}/".format(date,subject)):
        if (os.path.isdir(directory+"/{}_{}/".format(date,subject)+folder) and folder != 'bin'): # 원하는 ""폴더""만 선택
            dir_list.append(directory+"/{}_{}/".format(date,subject)+folder)

    #config, add, commit, push
    message = input("Commit 메시지를 입력하세요. :")

    for dirs in dir_list :
        os.chdir(dirs)
        os.system("git config --local user.name \"{}\"".format(user_name))
        os.system("git config --local user.email \"{}\"".format(user_email))
        os.system("git add .")
        os.system("git commit -m \"{}\"".format(message))
        os.system("git push origin master")


    #eclipse = "C:/Users/SSAFY/Desktop/1학기/Java/eclipse/eclipse.exe"
    #ctypes.windll.shell32.ShellExecuteA(0, 'open', eclipse, None, None, 1)

def main():
    global start_dir
    start_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


 # 해당 폴더에 .gitignore 있어야 함
    request = input("클론 받으려면 \"clone\", 푸시 하려면 \"push\"를 입력하세요. :")

    global subject
    subject = input("과목을 입력하세요. \"Java\"라면, \"java\"를 입력하세요. : ")

    if request == 'clone':
        clone()

    elif request == 'push':
        push()

def createFolder(directory):
    try :
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ("폴더를 못 만들겠습니다.")

if __name__ == "__main__":
    main()

