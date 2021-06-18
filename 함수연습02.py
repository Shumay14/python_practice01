# 221
def print_reverse(anything):
    print(anything[::-1])

print_reverse("python")

# 222
def print_score(a):
    print(sum(a)/len(a))

c = [10, 20, 30]
print_score(c)

# 223
def print_even(b):
    for i in b:
        if i % 2 == 0:
            print(i)

c = [1, 3, 2, 10, 12, 11, 15]
print_even(c)

# 224
def print_keys(some):
    for key in some.keys():
        print(key)

someone = {"이름":"서장연", "나이":30, "성별":0}
print_keys(someone)
        
# 225
def print_value_by_key(딕셔너리, key):
    print(딕셔너리[key])

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/26")


# 226
def print_5xn(string):
    some = int(len(string)/5)
    for x in range(some + 1):
        print(string[x * 5: x * 5 + 5])

print_5xn("아이엠어보이유알어걸")
print_5xn("아임엠어보이유알어걸앤왓이즈잇")
print_5xn("1234567890abcdefghijklmnopqrst")

# 227
def printmxn(string, num):
    some = int(len(string)/num)
    for x in range(some + 1):
        print(string[x * num : x * num + num])

printmxn("아이엠어보이유알어걸", 3)

# 228
def calc_monthly_salary(annual_salary):
    monthly = int(annual_salary/12)
    print(monthly)

calc_monthly_salary(12000000)

def calc_monthly_salary(annual_salary):
    monthly = int(annual_salary/12)
    return monthly

print(calc_monthly_salary(12000000))

# 229
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)
'''
왼쪽: 100
오른쪽: 200
'''

# 230
def my_print(a, b):
    print("왼쪽:", b)
    print("오른쪽:", a)

my_print(b=100, a=200)

# 231
# 함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능합니다. 
# 함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용해야 합니다.
def n_plus_1(n):
    result = n + 1
    return result

print(n_plus_1(3)) # 4

# 232
def make_url(site):
    print("www.{}.com".format(site))

make_url("kakao")
#
def make_url(site):
    url = "www." + site + ".com"
    return url

print(make_url("naver"))
#
def make_url(site):
    return "www." + site + ".com"

print(make_url("google"))

# 233
def make_list(some):
    done_list = []
    for i in some:
        done_list.append(i)
    return done_list    

print(make_list("abcd"))
#
def make_list(some):
    return list(some)

print(make_list("dcba"))


# 234
def pickup_even(some_list):
    some_even = []
    for i in some_list:
        if i % 2 == 0:
            some_even.append(i)
    return some_even

print(pickup_even([3, 4, 5, 6, 7, 8]))      


# 235
def convert_int(some):
    return int(some.replace(",", ""))

print(convert_int("1,234,567"))

# 236
def 함수(num):
    return num + 4

a = 함수(10)        # 14
b = 함수(a)         # 18
c = 함수(b)         # 22
print(c)           ## 22

# 237
def 함수(num):
    return num + 4

c = 함수(함수(함수(10)))
print(c) # 22


# 238
def 함수1(num):
    return num + 4

def 함수2(num):
    return num * 10

a = 함수1(10)   # 14
c = 함수2(a)    # 140 
print(c) 

# 239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)   # 16
print(c)


# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)    # 28
print(c)