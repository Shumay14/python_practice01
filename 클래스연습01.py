# class practice
# 251 클래스, 객체, 인스턴스에 대해 설명하라
# 클래스(class)란 붕어빵 틀과 같은 것, 객체나 인스턴스의 설계도 여러가지 함수들을 묶어서 정의해둔 것
# 객체(object)란 클래스 내에서 내부적으로 새로운 변수 지칭할 것을 만든것
# 인스턴스(instance)란 클래스나 함수를 지칭하는 것?


# 252 클래스 정의
class Human:
    pass


# 253 인스턴스 생성 & 바인딩
class Human:
    pass


areum = Human()

# 254 클래스 생성자-1
class Human:
    def __init__(self):
        print("응애응애")


areum = Human()

# 255 클래스 생성자-2
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("김아름", 25, "여자")
print(areum.name)
print(areum.sex)


# 256 인스턴스 속성에 접근
# 이름: 김아름, 나이: 25, 성별: 여자

print(areum.age)

# 257 class method-1
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {0} 나이: {1} 성별: {2}".format(self.name, self.age, self.sex))


areum = Human("김아름", 25, "여자")

areum.who()
# Human.who(areum)


# 258 class method-2
# setinfo method 추가


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {0} 나이: {1} 성별: {2}".format(self.name, self.age, self.sex))


areum = Human("불명", "미상", "모름")
areum.who()

areum = Human("김아름", 25, "여자")
areum.who()


# 259 클래스 소멸자
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {0} 나이: {1} 성별: {2}".format(self.name, self.age, self.sex))


areum = Human("김아름", 25, "여성")
areum.who()



# 260 error 원인
# class OMG:
#     def print() :
#         print("Oh my god")

# mystock = OMG()
# mystock.print()      ## OMG.print(mystock)  객체.print self 가 없어서 오류

class OMG:
    def print(self) :
        print("Oh my god")

mystock = OMG()
mystock.print()      
# OMG.print()         
OMG.print(mystock)

