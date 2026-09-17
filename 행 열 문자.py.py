#행 열 문자 인수로 받아 중첩 반복문으로 출력

def printPattern(rows=5, cols=5, char="*"):
    for _ in range(rows):
        for _ in range(cols):
            print(char,end="")
        print()
        
printPattern(3,10,"%")
