from cs50 import get_string


while True:

    while True:
        c_num = get_string("Number: ")
        if c_num.isdigit():
            break

    if len(c_num)!=13 and len(c_num)!=15 and len(c_num)!=16:
        print("INVALID")
        break

    nums = []
    calc = 0

    for i in range(2, len(c_num)+1, 2):
        nums.append(int(c_num[len(c_num)- i]))

    for num in nums:
        num = num * 2
        if num > 9:
            new = str(num)
            num = int(new[0]) + int(new[1])
        calc = calc + num

    for j in range(1, len(c_num)+1, 2):
        calc = calc + int(c_num[len(c_num)- j])

    if (calc % 10)!=0:
        print("INAVLID")
        break
    if c_num[0] == '3':
        print("AMEX")
        break
    if c_num[0] == '4':
        print("VISA")
        break
    if c_num[0] == '5':
        print("MASTERCARD")
        break


