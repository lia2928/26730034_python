#문제 14
#시와 분을 입력받아 출력예와 같은 형식으로 시간을 출력하는 프로그램을 작성하시오.
hour, minute = map(int, input().split())
print(f"{hour}:{minute:02d}")
