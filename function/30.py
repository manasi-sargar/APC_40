def decimal_binary(n):
    if n == 0:
        return ""
    return decimal_binary(n // 2) + str(n % 2)
n = int(input("Enter decimal number: "))
if n == 0:
    print("0")
else:
    print(decimal_binary(n))