#a = 1
print(type(a))

#b,c,d = 1,2,3
print(type(b),type(c),type(d))

# turple
a = 1,2,3
print(type(a))   

#list
a = 1,2,3    # <-- turple
a = list(a)
print(type(a))

#set (고유한 값을 갖는다, 순서가 없다)
b = [1,2,3,1,2,3,1,2,3]
a = set(b)
print(*a)

# len() 개수 반환 
fruits = {"apple", "banana", "grape"}
size = len(fruits)
print(size)

# in 포함되는지

fruits = {"apple","banana","grape"}
if "apple" in fruits:
    print("apple 있습니다.")
else:
    print("없습니다.")

string = input()
fruits = {"apple", "banana", "grape"}
if string in fruits:
    print(string, "있습니다.")
else:
    print(string, "없습니다.")

# 출력 (저장된 순서가 없다)
fruits = {"apple", "banana", "grape"}
print(fruits)

# 출력 (출력시 정렬해서 출력할수는 있다.)
fruits = {"apple", "banana", "grape"}
for x in sorted(fruits, reverse=True):
    print(x, end=" ")

# add() 요소 추가
fruits = {"apple", "banana", "grape"}
fruits.add("kiwi")
print(fruits)
fruits.discard("o") #remove()
print(fruits)
fruits.clear()
print(fruits)

#del
fruits = {"apple","banana","grape"}
del fruits[1]
print( fruits)
