num ={"one":1,"two":2,"three":3}
print(num["one"]) #key를 사용해서 value 출력
print(num["four"]) #key error

#get 메서드는 특정키에 해당하는 갑을 가져올 때 사용
#존재하지않는 키를 조회해도 오류가 발생하지 않는다.
print(num.get("four","해당키가 없습니다."))

#get()개수를 카운트할 때 사용 가능 
fruits = ["apple","banana","apple","melon","banana","apple"]
count={} # set을 만들려면 b = set()

for fruit in fruits:
    count [fruit] = count.get(fruit, 0) +1
print(count)

#항목 key,value 출력 (items())
for key,value in count.items():
    print(key,":",value)

#딕셔너리에서 key만 출력 (keys())
print(count.keys())
print(*count.keys())

#딕셔너리에서 value만 출력 (values())
print(count.values())
print(*count.values())
