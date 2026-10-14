#문제 2
#문자열을 입력받아 홀수 번째 문자들을 출력하는 프로그램을 작성하시오.
A = input()
for i in range(0, len(A), 2):
    print(A[i], end=' ')
