#문제 25
#이름, 키, 몸무게를 입력받아 다음과 같이 출력하는 프로그램을 작성하시오. (몸무게는 소수 둘째 자리까지 출력한다)
name, height, weight = input("입력: ").split()

weight = float(weight)

print(f"NAME: {name}")
print(f"HEIGHT: {height}cm")
print(f"WEIGHT: {weight:.2f}kg")
