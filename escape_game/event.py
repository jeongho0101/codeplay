from time import sleep
import sys

# 타이핑치는 효과
def typing_Ani(text, speed):
  string = text
  for letter in string:
    sleep(speed) 
    sys.stdout.write(letter)
    sys.stdout.flush()
  print("")

weapon = ""
battle = 0
random = 0
mhp = 100
ehp = 0

def gf(weapon):
    typing_Ani("할아버지: 용사여, 잠깐 예기좀 하겠나.", 0.1)
    typing_Ani("할아버지: 난 용잡이 였다네.", 0.1)
    typing_Ani("할아버지: 마을에 나타난 용을 잡고 성으로 가고있었어.", 0.1)
    typing_Ani("할아버지: 그러다 돌뿌리에 걸려 넘어져 여기로 굴러떨어졌지.", 0.1)
    typing_Ani("할아버지: 여기서 나가려고 가장 큰 용을 잡으러 갔지만 지고말았네.", 0.1)
    typing_Ani("할아버지: 보아하니 자네 칼이 부러졌군.", 0.1)
    typing_Ani("할아버지: 내 칼을 쓰게나.", 0.1)
    typing_Ani("할아버지: 특수한 광석으로 만들어져서 녹슬지 않았다네.", 0.1)
    while weapon != "할아버지 칼" or weapon != "맨손":
        weapon = input("무기를 받겠습니까?(네,아니오)->")
        if weapon == "네":
            typing_Ani("할아버지의 칼(공격력20)을 얻었다!", 0.05)
            weapon = "할아버지 칼"
        elif weapon == "아니오":
            typing_Ani("맨손(공격력10)을 쓰겠다!", 0.05)
            weapon = "맨손"
        else:
            typing_Ani("할아버지: 뭐라고?", 0.1)
    return weapon


def tutorial():
    ehp = 50
    typing_Ani("그냥 잡용이 나타났다!", 0.05)
    typing_Ani("배틀 방법:1과 2중 선택, 랜덤으로 성공과 실패가 결정됨", 0.05)
    while weapon != "할아버지 칼" or weapon != "맨손":
        battle = input("선택(1또는 2):")
        random = random.randint(1,2)
        if battle == random:
            typing_Ani("성공!", 0.05)
        else:
            typing_Ani("실패!", 0.05)




def battle1():
    typing_Ani("그냥 잡용이 나타났다!", 0.05)

def shop():
    '''
    1. 무기와 갑옷 하나만 선택 가능
    -> 쑤퍼 무기, 쑤퍼 갑옷
    '''

def key_room():
    '''
    1. 1번 상자와 2번 상자중 하나 선택
    -> 하나엔 2개, 다른건 1개 들어 있음
    '''

def treasure():
    '''
    1.상식퀴즈
    2.산수문제
    '''
gf(weapon)