def tong(n):
    S = 0
    while (n > 0):
        S = S + n % 10
        n = int(n / 10)
    return S
 
n = int(input("Nhập số nguyên dương n = "))
print(tong(n))
s=str(input())
result=int(0)
for i in range(len(s)):
    result+=int(s[i])
print(result)