# class 참치선물세트: #사용자 정의 클래스 / class 정의
#     일반 = 0
#     야채 = 0
#     고추 = 0
#     def 총합(self, 이름):
#         내용물갯수 = self.일반 + self.야채 + self.고추
#         print(이름 + str(내용물갯수) + "개")
#     def 출력(self):
#         self.총합("담긴참치갯수: ")


# 참치1호세트 = 참치선물세트() #인스턴스 생성 /생성된 인스턴스는 객체
# 참치1호세트.일반 = 5
# 참치1호세트.야채 = 3
# 참치1호세트.고추 = 2

# 참치1호세트.출력()
#print(참치1호세트.총합("참치1호세트 내용물"))

# class units:
#     hp = 0
#     damage = 0
#     speed = 0

# Timo = units()
# Timo.hp = 10
# Timo.damage = 100
# Timo.speed = 50

# Yasuo = units()
# Yasuo.hp = 5
# Yasuo.damage = 1000
# Yasuo.speed = 100
# print(f"티모-체력:{Timo.hp}|공격력:{Timo.damage}|이속:{Timo.speed}")

# Yasuo.hp -= Timo.damage
# print(Yasuo.hp)
class 참치선물세트(): #사용자 정의 클래스 / class 정의
    def __init__(self,일반,야채,고추):
        self.normal = 일반
        self.vege = 야채
        self.pepper = 고추
    
    def 내용물보기(self,name):
        print(name)
        print("일반참치:" + str(self.normal))
        print("야채참치:" + str(self.vege))
        print("고추참치:" + str(self.pepper))

참치1호 = 참치선물세트(10,3,2)
참치1호.내용물보기("참치1호 내용물 안내")