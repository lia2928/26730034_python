#6
#1부터 입력받은 수까지의 곱을 출력하는 프로그램을 작성하시오.
n = int(input())

result = 1

for i in range(1, n + 1):
    result *= i

print(result)
