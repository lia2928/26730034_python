#문제 21
#하나의 문자열을 입력받아 문자사이에 '-'문자를 넣어 거꾸로 출력하는 프로그램을 작성하시오.
def reverse_with_hyphen(text):
    reversed_text = text[::-1]
    result = "-".join(reversed_text)
    
    return result

user_input = input("문자열을 입력하세요: ")

output = reverse_with_hyphen(user_input)
print("결과:", output)
