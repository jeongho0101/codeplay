class 참치선물세트():
    def __init__(self, 일반, 야채, 고추):
        self.일반 = 일반
        self.야채 = 야채
        self.고추 = 고추
    
    def 내용물보기(self,name):
        print(name)
        print("일반참치:" + str(self.일반))
        print("야채참치:" + str(self.야채))
        print("고추참치:" + str(self.고추))

class 특별선물세트(참치선물세트):
    def __init__(self, 일반, 스팸, 올리브유):
        super().__init__(일반,0,0)
        self.스팸 = 스팸
        self.올리브유 = 올리브유
    
    def 내용물보기(self,name):
        super().내용물보기(name)
        print("스팸:"+str(self.스팸))
        print("올리브유:"+str(self.올리브유))

특별01 = 특별선물세트(6,3,2)
특별01.내용물보기("특별세트 1호")