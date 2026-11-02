#21
#다음 명령을 반복하여 입력받아 해당하는 기능을 출력하는 프로그램을 작성하시오.

단, E를 입력하면 "EXIT"를 출력한 후 프로그램을 종료한다.

while True:
    n = input()

    if n == "A":
        print("ADD")
    elif n == "B":
        print("BACK")
    elif n == "C":
        print("COPY")
    elif n == "D":
        print("DELETE")
    elif n == "E":
        print("EXIT")
        break
    else:
        print("NONE")
