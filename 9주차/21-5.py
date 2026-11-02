#5
#1부터 입력받은 수까지의 합을 출력하는 프로그램을 작성하시오.
n = int(input())

total = 0

for i in range(1, n + 1):
    total += i

print(total)
