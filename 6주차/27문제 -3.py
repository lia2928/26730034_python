#문제3
#문자열을 입력받아 거꾸로 출력하는 프로그램을 작성하시오.
A = input()
for i in range(len(A)-1, -1, -1):
    print(A[i], end='')
