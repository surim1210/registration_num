#첫번째 접근
def mask_security_number(security_number):

    result = security_number[:-4] + '****'
    return result

def mask_security_number_sec(security_number):

    #리스트로 변환
    num_list = list(security_number)

    # 마지막 4개의 값을 '*'로 대체
    for i in range(len(num_list)-4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구
    total_str = "".join(num_list) # total_str = '' 빈 문자열을 변수로 할당
    return total_str


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

print(mask_security_number_sec("sec: 880720-1234567"))
print(mask_security_number_sec("sec: 8807201234567"))
print(mask_security_number_sec("sec: 930124-7654321"))
print(mask_security_number_sec("sec: 9301247654321"))
print(mask_security_number_sec("sec: 761214-2357111"))
print(mask_security_number_sec("sec: 7612142357111"))