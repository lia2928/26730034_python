#문제 9
#오빠의 이름과 나이, 동생의 이름과 나이를 입력 예와 같이 입력 받은 후에, 출력 예와 같은 형식으로 두 학생의 나이 차를 출력하는 프로그램을 작성하시오.
name1, age1 = input().split()
name2, age2 = input().split()
age1 = int(age1)
age2 = int(age2)
print(f"{name1}'s age - {name2}'s age = {age1 - age2}")
