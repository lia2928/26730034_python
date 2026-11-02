#9
#1부터 차례대로 곱하다가 입력받은 수 이상이 되면 중단하고 마지막에 곱해진 수를 출력하는 프로그램을 작성하시오.
n = int(input())

result = 1
i = 1

while result < n:
    result *= i
    i += 1

print(i - 1)
