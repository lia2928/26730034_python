#출력시 ",' 구분하여 출력하기
print('신씨가 소리질렀다. "도둑이야"')

#2
print("Mary's cosmetics")

#3 print(sep=' ') sep?
print(1,2,3,4,5,sep='/')

# 파이썬 300제 007번 문제(naver;kakao;sk;samsung)
print("naver", "kakao", "sk", "samsung", sep=";")

#for i in range(7):
#print(i,end=' ')
#python 300제 009번 문제
print("first", end=' ');print("second")

#python 300제 013번 문제
s = "hello"
t = "python"
print(s+"!", t)

#type 값의 타입을 알려주는 함수
 a = 128
print (type(a))#int       

a = "128"
print (type(a))#str           

a = 12.5
print (type(a))#float          

#문자(열) ->정수 (str->int)
a="128"

#변수에 데이터 타입을 변경하지않고 사용
print(type(int(a)))
      
#대입해서 변수 int 변경
a=int(a)

#정수->실수
b=123
b=float(b)

#정수->문자열
c=123
c= str(c)

#문자열 인덱싱 - p t
letters = 'python'
print(letters[0], letters[2])

# 문자열 슬라이싱 -> 뒤에 4자리
license_plate = "24가 2210"
print(license_plate[-4::])

#문자열 슬라이싱 step
string = "홀짝홀짝홀짝"
print(string[::2])#홀홀홀
print(string[1::2])#짝짝짝      

#문자열 슬라이싱 거꾸로 출력
string = "PYTHON"
print(string[::-1])

#문자열 치환 (replace())
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
#phone_number=phone_number.replace("-", " "))
print(phone_number)

#python 300제 026
phone_number1 = phone_number.replace("-", "")

#python 300제 027
url = "http://sharebook.kr" #kr
url = url.split('.')
print(url[-1])

# 문자+문자 (더하기연산 ->연결)
a = "3"
b = "4"
print(a + b)#"34"

# 문자* 숫자(곱하기-> 문자를 숫자만큼 반복해서 출력
a="hi"
print(a*10)#"hihihihihihihihihihi"

#python 300제 034(python java python java python java python java)
t1 = "python"
t2 = "java"
print((t1+" "+t2+" ")*4)

#python 035~037 검토

#python 300제 038 (콤마 제거 후 정수 형변환)
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))

#040 strip() 좌우 공백을 제거
data = "   삼성전자    "
print(data.strip())

#049 date = "2020-05-01"-> 연도,월,일
date = "2020-05-01"
temp = date.split("-")
year=temp[0]
month = temp[1]
day= temp[2]

print(year)
print(month)
print(day)

#051 리스트 생성     
movies= ["닥터 스트레인지", "스플릿", "럭키"]

#052 리스트에 원소 추가 -> append("값") (맨 뒤에 값을 추가)
movies.append("배트맨")
print(movies)

#053 리스트에 원소추가 (특정위치) -> insert(인덱스, 값)
movies.insert(1, "슈퍼맨")
print(movies)

#054 리스트에 원소 삭제 (remove("값"), del 리스트이름[인덱스])
#pop(인덱스)
moveies.remove("럭키")
print("remove: ", movies)#(0)

#056 리스트에 합 (더하기 연상)중복허용
a=['a','b','c']
b=['a','b','c']
c=a+b
print(c)

#057 리스트 값 중에 최대값 (max()), 최솟값(min())
a_list=[1,2,3,4,5,6,7,8]
print(max(a_list))
print(min(a_list))

#058리스트 요소값에 합 (sum())
print(sum(a_list())

#59리스트 요소에 개수(len())
print(len(a_list()))

#60 리스트요소값에 평균 (sum()/len())
print(sum(nums) / len(nums))


























