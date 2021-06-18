# 201
# "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")

# 202
print_coin()

# 203
for i in range(10):
    print_coin()

# 204
def print_coin():
    for _ in range(10):
        print("이더리움")

print_coin()

# 205
# 함수가 정의되기 전에 호출되면 에러가 발생합니다.

# 206
# A B C A B

# 207
# A C B

# 208
# A C B E D

# 209
# B A

# 210
# B C B C B C A

# 211
# 안녕 Hi
def 함수(아무거나):
    print(아무거나)

함수("안녕")
함수("Hi")

# 212
def 함수(a, b):
    print(a + b)

함수(3, 4)

# 213
# 정의한 함수와 다르게 호출해서 오류

# 214
# str 과 int 는 함께 연산 불가능

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 
# 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(anything):
    print(anything + ":D")

print_with_smile("좋아")

# 216
print_with_smile("안녕하세요")

# 217
# 30% 상한가를 출력하는 print_upper_price 함수를 정의하라
def print_upper_price(price):
    print(price * 1.3)

print_upper_price(100)


# 218
def print_sum(a, b):
    print(a + b)

print_sum(5, 7)

# 219
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

print_arithmetic_operation(10, 2)

# 220
def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
    
print_max(1, 2, 3)

