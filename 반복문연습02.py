# 151 for문을 사용해서 리스트의 음수를 출력하라
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)

# 152 for문을 사용해서 3의 배수만 출력하라
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print(i)

# 153 20보다 작은 3의 배수를 출력하라
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i < 20 and i % 3 ==0:
        print(i)

# 154 세글자 이상의 문자를 출력하라
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)

# 155 대문자만 출력하라
# isupper() 메서드는 대문자 여부를 판별합니다.
리스트 = ["A", "b", "c", "D"]
for cap in 리스트:
    if cap.isupper():
        print(cap)

# 156 소문자만 출력하라
for cap in 리스트:
    if cap.isupper():
        continue
    else:
        print(cap)

# 157 이름의 첫글자를 대문자로 변경해서 출력하라
# upper() 메서드는 문자열을 대문자로 변경합니다.
# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[:1].upper() + i[1:])

# 158 확장자를 제거하고 파일이름만 출력하라
# split() 메서드 활용
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for file_name in 리스트:
    a = file_name.split(".")
    print(a[0])

# 159 확장자가 .h 인 파일이름만 출력하라
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file_name in 리스트:
    a = file_name.split(".")
    if a[1] in "h":
        print(file_name)

# 160 확장자가 .h or .c 인 파일을 출력하라
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file_name in 리스트:
    a = file_name.split(".")
    if a[1] in "h" or a[1] in "c":
        print(file_name)


# 161 for문과 range 구문을 사용해서 0~99까지 
# 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
for num in range(10):
    print(num)

# 162 월드컵은 4년에 한 번 개최된다.
# range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
# range의 세번 째 파라미터는 증감폭을 결정합니다.
for wc in range(2002, 2051, 4):
    print(wc)

# 163 1~30까지 숫자 중 3의 배수를 출력하라
for num in range(1,31):
    if num % 3 == 0:
        print(num)
    num += 1

# 164 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for num in range(100):
    num2 = 99 - num
    print(num2)

# 165 for문을 사용하여 아래와 같이 출력하라.
# 0.0
# 0.1
# 0.2
# 0.3
# ...
# 0.9
num = 0
for times in range(10):
    if times <= 10:
        print(num/10)
    num += 1

for num in range(10):
    print(num/10)

# 166 구구단 3단을 출력하라
for n in range(1,10):
    print("3x{0} = {1}".format(n, 3*n))


# 167 구구단 3단을 출력하라. 단, 홀수 번째만 출력한다.
for n in range(1,10,2):
    print("3x{0} = {1}".format(n, 3*n))

# 168 1~10까지 모든 수를 더한 값을 출력하라
j = 0
for i in range(11):
    j = j + i
print(j)

# 169 1~10까지 숫자 중 모든 홀수의 합을 구하는
# 프로그램을 for문을 사용하여 작성하라
j = 0
for i in range(1,11,2):
    j = j + i
print(j)

# 170 1~10까지 숫자를 모두 곱하라
j = 1
for i in range(1,11):
    j = j * i
print(j)



