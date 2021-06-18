# 171 아래와 같이 리스트의 데이터를 출력하라. 
# 단, for문과 range문을 사용하라.
# 32100
# 32150
# 32000
# 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    j = price_list
    print(j[i])

# 172 
# 0 32100
# 1 32150
# 2 32000
# 3 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i, price_list[i])

# 173
# 3 32100
# 2 32150
# 1 32000
# 0 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(3-i, price_list[i])

for i in range(len(price_list)):
    print((len(price_list)-1) - i, price_list[i])

# 174 
# 100 32150
# 110 32000
# 120 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(1, len(price_list)):
    print(90 + i*10, price_list[i])

# 175
# 가 나
# 나 다
# 다 라
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[i], my_list[i+1])

# 176 
# 가 나 다
# 나 다 라
# 다 라 마
my_list = ["가", "나", "다", "라", "마"]
for i in range(3):
    print(my_list[i], my_list[i+1], my_list[i+2])


# 177
# 라 다
# 다 나
# 나 가
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[-i-1], my_list[-i-2])

# 178 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
# 100
# 200
# 400
my_list = [100, 200, 400, 800]
x = my_list
for i in range(3):
    print(x[i+1] - x[i])

# 179 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 
# 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 
# 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 
# 같은 방식으로 나머지 데이터의 평균을 출력한다.
my_list = [100, 200, 400, 800, 1000, 1300]
x = my_list
for i in range(4):
    y = x[i] + x[i+1] + x[i+2]
    print(y/3)

# 180 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 
# 고가와 저가의 차를 변동폭이라고 정의할 때, 
# low, high 두 개의 리스트를 사용해서 
# 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
x = low_prices
y = high_prices
volatility = []
for i in range(5):
    volatility.append(x[i] - y[i])
print(volatility)

# 181 
apart = [ ["101호", "102호"], ["201호", "202호"],\
     ["301호", "302호"] ]

# 182
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

# 183 아래 표를 stock 이름의 딕셔너리로 표현하라.
# 시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 
# 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
stocks = {"시가": [100, 200, 300], "종가": [80, 210, 330]}

# 184
stockss = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}


# 185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(3):
    j = apart[i]
    print(j[0], "호")
    print(j[1], "호")

for i in apart:
    for j in i:
        print(j, "호")


# 186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(3):
    j = apart[-1-i]
    print(j[0], "호")
    print(j[1], "호")

for i in apart[::-1]:
    for j in i:
        print(j, "호")
# 187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(3):
    j = apart[-1-i]
    print(j[1], "호")
    print(j[0], "호")

# 188
for i in apart:
    for j in i:
        print(j, "호")
        print("-----")

# 189
for i in apart:
    for j in i:
        print(j, "호")
    print("-----")

# 190
for i in apart:
    for j in i:
        print(j, "호")
print("-----")

# 191
# data에는 매수한 종목들의 OHLC (open/high/low/close) 
# 가격 정보가 바인딩 되어있다.
# 수수료를 0.014 %로 가정할 때, 
# 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j * 1.00014)
    

# 192
for i in data:
    for j in i:
        print(j * 1.00014)
    print("-----")

# 193
result = []
for i in data:
    for j in i:
        k = j * 1.00014   
        result.append(k)
print(result)

#194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
sub = []
for i in data:
    for j in i:
        sub.append(j)
    result.append(sub)
print(result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:4]:
    print(i[3])

# 196
for i in ohlc[1:4]:
    if i[3] > 100:
        print(i[3])

# 197
for i in ohlc[1:4]:
    if i[3] >= i[0]:
        print(i[3])

# 198
volatility = []
for i in ohlc[1:]:
    j = i[1] - i[2]
    volatility.append(j)
print(volatility)


# 199
volatility = []
for i in ohlc[1:]:
    if i[3] > i[0]:
        j = i[3] - i[0]
        volatility.append(j)
print(volatility)

# 200
profit = 0
for i in ohlc[1:]:
    j = i[3] - i[0]
    profit = profit + j
print(profit)

