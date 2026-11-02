#11
#0이 입력될 때까지 정수를 계속 입력받아 입력된 수 중 가장 큰 수를 출력하는 프로그램을 작성하시오. 단, 음의 정수는 입력되지 않는다

max_num = 0

while True:
    n = int(input())

    if n == 0:
        break

    if n > max_num:
        max_num = n

print(max_num)
