import sys

n, b = map(int, sys.stdin.readline().split())

# b진수로 변환된 값은 문자열로 반환
num_b = ""

while n != 0:
    b_num = n % b
    n = n // b

    # 10 이상일때: 알파벳으로 변환 후 삽입
    if b_num >= 10:
        num_b = str(chr(ord('A') + b_num - 10)) + num_b
    # 10 이하일때: 문자로만 바꾸고 바로 삽
    else:
        num_b = str(b_num) + num_b

print(num_b)
