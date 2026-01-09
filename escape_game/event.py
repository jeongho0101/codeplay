from time import sleep
import sys
import random

# 타이핑치는 효과
def typing_Ani(text, speed):
  string = text
  for letter in string:
    sleep(speed) 
    sys.stdout.write(letter)
    sys.stdout.flush()
  print("")

weapon = 0
battle = 0
Random = 0
mhp = 100
ehp = 0
answer = ""
keys = 2

def gf(weapon):
    typing_Ani("할아버지: 용사여, 잠깐 얘기좀 하겠나.", 0.1)
    typing_Ani("할아버지: 난 용잡이 였다네.", 0.1)
    typing_Ani("할아버지: 마을에 나타난 용을 잡고 성으로 가고있었어.", 0.1)
    typing_Ani("할아버지: 그러다 돌뿌리에 걸려 넘어져 여기로 굴러떨어졌지.", 0.1)
    typing_Ani("할아버지: 여기서 나가려고 가장 큰 용을 잡으러 갔지만 지고말았네.", 0.1)
    typing_Ani("할아버지: 그 용을 잡아주게.", 0.1)
    typing_Ani("할아버지: 보아하니 자네 칼이 부러졌군.", 0.1)
    typing_Ani("할아버지: 내 칼을 쓰게나.", 0.1)
    typing_Ani("할아버지: 특수한 광석으로 만들어져서 녹슬지 않았다네.", 0.1)
    while weapon != 20 or weapon != 10:
        weapon = input("무기를 받겠습니까?(네,아니오)->")
        if weapon == "네":
            typing_Ani("할아버지의 칼(공격력20)을 얻었다!", 0.05)
            weapon = 20
            return weapon
        elif weapon == "아니오":
            typing_Ani("맨손(공격력10)을 쓰겠다!", 0.05)
            weapon = 10
            return weapon
        else:
            typing_Ani("할아버지: 뭐라고?", 0.1)

def tutorial(mhp):
    ehp = 50
    typing_Ani("그냥 잡용이 나타났다!", 0.05)
    typing_Ani("배틀 방법:1과 2중 선택, 랜덤으로 성공과 실패가 결정됨", 0.05)
    while ehp > 0:
        battle = input("선택(1또는 2):")
        Random = random.randint(1,2)
        if int(battle) == Random:
            typing_Ani("성공!", 0.05)
            ehp -= weapon
        else:
            typing_Ani("실패!", 0.05)
            mhp -= 10
            if mhp < 0:
                typing_Ani("용사 사망", 0.07)
                return mhp
    typing_Ani("승리!!!!!!!!!!!!", 0.05)
    return mhp

def battle1(mhp):
    ehp = 100
    typing_Ani("그냥 잡용이 나타났다!", 0.05)
    while ehp > 0:
        battle = input("선택(1또는 2):")
        Random = random.randint(1,2)
        if int(battle) == Random:
            typing_Ani("성공!", 0.05)
            ehp -= weapon
        else:
            typing_Ani("실패!", 0.05)
            mhp -= 10
            if mhp < 0:
                typing_Ani("용사 사망", 0.07)
                return mhp
    typing_Ani("승리!!!!!!!!!!!!", 0.05)
    return mhp

def battle2(mhp):
    ehp = 200
    typing_Ani("중간용이 나타났다!", 0.05)
    while ehp > 0:
        battle = input("선택(1또는 2):")
        Random = random.randint(1,2)
        if int(battle) == Random:
            typing_Ani("성공!", 0.05)
            ehp -= weapon
        else:
            typing_Ani("실패!", 0.05)
            mhp -= 20
            if mhp < 0:
                typing_Ani("용사 사망", 0.07)
                return mhp
    typing_Ani("승리!!!!!!!!!!!!", 0.05)
    return mhp

def boss(mhp):
    ehp = 500
    typing_Ani("보스용이 나타났다!", 0.05)
    while ehp > 0:
        battle = input("선택(1또는 2):")
        Random = random.randint(1,2)
        if int(battle) == Random:
            typing_Ani("성공!", 0.05)
            ehp -= weapon
        else:
            typing_Ani("실패!", 0.05)
            mhp -= 30
            if mhp < 0:
                typing_Ani("용사 사망", 0.07)
                return mhp
    typing_Ani("보스 승리!!!!!!!!!!!!", 0.05)
    return mhp

def shop(weapon,mhp,answer):
    typing_Ani("점원: 어서오세요", 0.05)
    typing_Ani("점원: 계산은 가지고 계신 식량으로 해주세요.", 0.05)
    typing_Ani("가진 식량: 2개", 0.05)
    typing_Ani("1.쑤퍼 용잡이칼(40) 가격: 식량2개", 0.05)
    typing_Ani("2.쑤퍼 갑옷(hp+100) 가격: 식량2개", 0.05)
    while answer != 1 or answer !=2:
        answer = input("무엇을 사겠습니까?(1.무기,2.갑옷)->")
        if answer == "1":
            typing_Ani("쑤퍼 용잡이칼(공격력40)을 얻었다!", 0.05)
            weapon = 40
            return weapon
        elif answer == "2":
            typing_Ani("쑤퍼 갑옷(hp+100)을 얻었다!", 0.05)
            mhp = 200
            return mhp
        else:
            typing_Ani("점원: 그런 물건은 없습니다.", 0.1)

def key_room(keys,answer):
    Random = random.randint(1,2)
    typing_Ani("상자가 2개 있다!",0.05)
    typing_Ani("2개의 상자중 1개만 열수있다.",0.05)
    while answer != 1 or answer !=2:
        answer = input("어떤 상자를 여시겠습니까?(1 또는 2)->")
        if int(answer) == Random:
            typing_Ani("열쇠 2개를 얻었다!",0.05)
            keys = 2
            return keys
        elif answer != Random:
            typing_Ani("열쇠 1개를 얻었다!",0.05)
            keys = 1
            return keys
        else:
            typing_Ani("그런 상자는 없다.", 0.1)
    
def treasure1(weapon,answer):
    typing_Ani("보물상자를 발견했다!",0.05)
    typing_Ani("하지만 문제를 풀어야 가져갈수있다.",0.05)
    typing_Ani("1번 문제.",0.05)
    answer = input("마타톤 주행거리에서 파이 소수점 3번째 자리까지를 뺀 값은? ->")
    if answer == "39.054":
        typing_Ani("정답!!",0.05)
        typing_Ani("하지만 두번째 문제가 남아있다.",0.05)
        typing_Ani("2번 문제.",0.05)
    elif answer != "39.054":
        typing_Ani("틀렸다!!",0.05)
        typing_Ani("상자가 불타 재가되었다",0.05)
        typing_Ani("재가된 상자를 얻었다.",0.05)
        return weapon
    answer = input("미국의 지역이 아닌 것은?\n(1.오리건 2.조지아 3.펜실베니아 4.웰링턴 5.와이오밍) ->")
    if answer == "4" or answer == "웰링턴":
        typing_Ani("정답!!.",0.05)
        typing_Ani("보물상자에서 전설의 용잡이칼(공격력 500)을 얻었다!",0.05)
        typing_Ani("주의! 공격력이 높은 대신 공격 선택지가 4개로 늘어난다.",0.05)
        weapon = 500
        return weapon
    elif answer != "4" or answer != "웰링턴":
        typing_Ani("틀렸다!!",0.05)
        typing_Ani("상자가 불타 재가되었다",0.05)
        typing_Ani("재가된 상자를 얻었다.",0.05)
        return weapon
    
def treasure2(mhp,answer):
    typing_Ani("보물상자를 발견했다!",0.05)
    typing_Ani("하지만 철창 뒤에 있다.",0.05)
    typing_Ani("열쇠로 문을 열어야 한다.",0.05)
    if keys == 2:
        typing_Ani("남은 열쇠로 문을 열었다",0.05)
        typing_Ani("하지만 문제를 풀어야 가져갈수있다.",0.05)
        typing_Ani("1번 문제.",0.05)
        answer = input("마블 케릭터가 아닌것은\n(1.아이언맨 2.블랙팬서 3.샤잠 4.스타로드 5.로켓 ->")
        if answer == "3" or answer == "샤잠":
            typing_Ani("정답!!",0.05)
            typing_Ani("하지만 두번째 문제가 남아있다.",0.05)
            typing_Ani("2번 문제.",0.05) 
            answer = input("아시아에 있는 나라가 아닌것은?\n(1.한국 2.수리남 3.싱가포르 4.몰디브 5.사이프러스) ->")
            if answer == "2" or answer == "수리남":
                typing_Ani("정답!!.",0.05)
                typing_Ani("보물상자에서 전설의 갑옷(방어력 300)을 얻었다!",0.05)
                mhp = 300
                return mhp
            elif answer != "2" or answer != "수리남":
                typing_Ani("틀렸다!!",0.05)
                typing_Ani("상자가 불타 재가되었다",0.05)
                typing_Ani("재가된 상자를 얻었다.",0.05)
                return mhp
        elif answer != "3" or answer != "샤잠":
            typing_Ani("틀렸다!!",0.05)
            typing_Ani("상자가 불타 재가되었다",0.05)
            typing_Ani("재가된 상자를 얻었다.",0.05)
            return mhp
    elif keys == 1:
        typing_Ani("열쇠가 없어 문을 열지 못했다",0.05)
        return mhp
    


treasure2(keys,answer)
