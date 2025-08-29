import random
eng =['apple', 'watermelon', 'grape', 'pear', 'peach']
kor = ['사과', '수박', '포도', '배', '복숭아']
score = 0
order = 0
def exercise():
    for i in range(len(kor)):
        answer = input(f'{kor[i]}:')
        if answer == eng[i]:
            print('정답')
            score += 1
        else:
            print('틀렸데여')
            print(f'{eng[i]}임')

    print(f'{len(kor)}/{score}개 맞춤')
def add():
    k = input('한글단어:')
    e = input('영어단어:')
    c = input(f'{k},{e} 맞음? (y/n)')
    if c == 'y':  
        kor.append(k)
        eng.append(e)
        print('추가됨')
    else:
        print('취소됨')
end = 0
while end == 0:
    quest = input('1.문제풀기 2.단어추가 3.종료: ')
    if quest == '1':
        exercise()
    elif quest == '2':
        add()
    elif quest == '3':
        end = 1
        print('종료')
    else:
        print('똑바로 써')