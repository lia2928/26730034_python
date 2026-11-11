s = 'Monty Python'
#슬라이싱 [start :end : step]
#Python
print(s[6:12])
print(s[6:])

#Monty
print(s[0:5])
print(s[:5])
print(s[5]) 

#거꾸로 출력
print(s[::-1])

#문자자료형 + 문자자료형(연결)
print(s[:5]+s[6:])

#in 문자열 안에 문자 혹은 문자열을 포함하고 있는지 체크
#영어는 대소문자를 구분한다.
print("a" in "Abc") #False
print("a" in "abc") #True
print("a" not in "Abc") #True

#숫자 > 문자로 형변환 str()
name ="홍길동"
age = 21
print("제 이름은 " + name + "입니다.")
print("제 나이는 " + str(age) + "입니다.")

#print % 서식문자 (%d 정수,%f 실수, %c 문자, %s 문자열)
print("제 이름은 %s입니다" %name)
print("제 이름은 %s입니다. 저는 %s살입니다." % (name, age))

# f-string  활용해서 문자열 출력
print(f"제 이름은 {name}입니다, 저는 {age}살입니다.")

#format() 활용해서 문자열 출력
print("제 이름은 {}입니다, 저는 {}살 입니다. ".format(name,age))
#format() 번호로 출력정의
print("제 이름은 {0}입니다, 저는 {1}살 입니다. ".format(name,age))
