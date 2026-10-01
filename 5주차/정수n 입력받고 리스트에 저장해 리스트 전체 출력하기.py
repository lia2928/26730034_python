'''
#첫번쨰 문제
#정수 n을 입력받고 n개의 정수를 입력받아 리스트에 저장한 후 리스트 전체를 출력하는 프로그램을 작성하시오.
N = int(input())
lst = []

for i in range(N):
    temp = int(input())
    lst.append(temp)

print(lst)

#두번째 문제
#0이 입력될 때까지 정수를 입력받아 리스트에 저장한 후 차례대로 출력하는 프로그램을 작성하시오.
lst=[]

while True:
    n = int(input())
    if n==0:
        break
    lst.append(n)

for i in lst :
        print(i)


#세번째
#0이 입력될 때까지 정수를 입력받아 리스트에 저장한 후, 짝수번째(두 번째, 네 번째, 여섯 번째, ...) 값을 공백으로 구분하여 한 줄에 출력하는 프로그램을 작성하시오.

lst=[]

while True:
    n = int(input())
    if n==0:
        break
    lst.append(n)

for i in range(len(lst)):
    if i%2==1:
        print(lst[i])


#네번째
#정수 N개를 입력받아 리스트에 저장한 후 모든 값의 평균을 출력하는 프로그램을 작성하시오.
#(정수 부분만 출력한다.)

N = int(input())
lst = []

for i in range(N):
    temp = int(input())
    lst.append(temp)

print(int(sum(lst)/N))
'''

#마지막 문제
#여러 개의 정수를 한 줄에 입력받아 가장 큰 값을 출력하는 프로그램을 작성하시오.

a = list(map(int,input().split()))
print(max(a))

max_value = a[0]

for i in range(1,len(a)):
    if max_value < a[i]:
        max_value=a[i]
print(max_value)

















        
