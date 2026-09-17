#가변인수 합계 출력

def add(*numbers):
    sum=0
    for i in numbers:
        sum = sum+1
    return sum
print(add(10,20,30,40,50))
