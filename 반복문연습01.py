# 131 for문 실행결과를 예측하라
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

# 사과
# 귤
# 수박

# 132
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print("#####")

# #####
# #####   
# #####

# 133 다음 for문과 동일한 기능을 수행하는 코드를 작성하세요
# for 변수 in ["A", "B", "C"]:
#     print(변수)

Capital = ["A", "B", "C"]
for 변수 in Capital:
    print(변수)

# 134 for문을 풀어서 동일한 동작을 하는 코드를 작성하라
for 변수 in ["A", "B", "C"]:
    print("출력", 변수)

print("출력 A")
print("출력 B")
print("출력 C")

print("출력", "A")
print("출력", "B")
print("출력", "C")

# 135 for문을 풀어서 동일한 동작을 하는 코드를 작성하라
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

print("변환:", "a")
print("변환:", "b")
print("변환:", "c")

# 136 다음 코드를 for문으로 작성하여라
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

for 변수 in [10, 20, 30]:
    print(변수)

# 137 다음 코드를 for문으로 작성하여라
print(10)
print(20)
print(30)

for i in [10, 20, 30]:
    print(i)

# 138
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for i in [10, 20, 30]:
    print("-------")

# 139 다음 코드를 for문으로 작성하라
print("++++")
print(10)
print(20)
print(30)

for i in ["++++", 10, 20, 30]:
    print(i)

# 140 
print("-------")
print("-------")
print("-------")
print("-------")

for i in range(4):
    print("-------")

# 141 다음과 같이 판매가가 저장된 리스트가 있을 때 
# 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 
# 단 부가세는 10원으로 가정한다.

리스트 = [100, 200, 300]
for price in 리스트:
    print(price + 10)

# 142 for문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
리스트 = ["김밥", "라면", "튀김"]
for today_menu in 리스트:
    print("오늘의 메뉴:", today_menu)

# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144
리스트 = ['dog', 'cat', 'parrot']
for name in 리스트:
    print(name, len(name))

# 145 for문을 사용해서 동물이름의 첫 글자만 출력하라
리스트 = ['dog', 'cat', 'parrot']
for name in 리스트:
    print(name[:1])

# 146 for문을 활용하여 다음과 같이 출력하라
# 3 x 1
# 3 x 2
# 3 x 3
리스트 = [1, 2, 3]
for smt in 리스트:
    print("3 X {}".format(smt))

# 147
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
for smt in 리스트:
    print("3 X {0} = {1}".format(smt, smt*3))

# 148 for문을 사용해서 다음과 같이 출력하라
리스트 = ["가", "나", "다", "라"]
for smt in 리스트[1:]:
    print(smt)

# 149
for smt in 리스트[::2]:
    print(smt)

# 150
# 증감폭을 음수로 설정하면 끝에서 앞방향으로 값을 슬라이싱합니다.
for smt in 리스트[::-1]:
    print(smt)



