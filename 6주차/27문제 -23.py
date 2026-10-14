#문제 23
#삼각형의 밑변과 높이의 길이를 입력받아 넓이를 출력하는 프로그램을 작성하시오(넓이는 소수점 둘째자리에서 반올림하여 첫째 자리까지만 출력한다).
base = float(input("밑변을 입력하세요: "))
height = float(input("높이를 입력하세요: "))

area = (base * height) / 2

print(f"출력 : {area:.1f}")
