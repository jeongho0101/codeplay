import random
import os

def cl():
    os.system("cls")
num = ""
guess = ""
count = 0
num_temp = ""
log = []

def make_num():
    num_temp = ""
    num_temp += str(random.randint(0,9))
    while len(num_temp) < 3:
        temp = str(random.randint(0,9))
        if temp not in num_temp:
            num_temp += temp

    return num_temp

def guess_num(n):
    global guess
    global log
    global count
    
    while n != guess:
        st = 0
        b = 0
        result = ""
        guess = input("추측(숫자 3 개): ")
        
        for i in range(len(guess)):
            if guess[i] in n:
                if guess[i] == n[i]:
                    st += 1
                else:
                    b += 1
        if st + b == 0:
            result = f"{guess} - out"
        else:
            if st > 0 and b > 0:
                result = f"{guess} - {st}S {b}B"
            else:
                if st > 0:
                    result = f"{guess} - {st}S"
                else:
                    result = f"{guess} - {b}B"
        
        log.append(result)
        count += 1
        cl()
        for say in log:
            print(say)
    return count

def final(n, c):
    cl()
    print("수고했다")
    print(f"정답은 {n}")
    print(f"{c}번 만에 맞춤")
    if 0 < c < 4:
        print("운빨")
    elif 5 < c < 9:
        print("잘함")
    else:
        print("멍청이")

def game():
    global num 
    global count

    num = make_num()
    count = guess_num(num)
    final(num, count)

game()