with open('input/input1.txt', 'r') as f:
    digits = f.read().strip()

captcha = 0
for i in range(len(digits)):
    if i == len(digits) - 1:
        if digits[i] == digits[0]:
            captcha += int(digits[i])
    else:
        if digits[i] == digits[i+1]:
            captcha += int(digits[i])

print(captcha)


