def phanTichSoNguyen(n):
    i = 2
    arr = []
    while n > 1:
        if n % i == 0:
            n = int(n / i)
            arr.append(i)
        else:
            i = i + 1

    if len(arr) == 0:
        arr.append(n)
    return arr
 
n = int(input("Nhập số nguyên dương n: "))
arr = phanTichSoNguyen(n)
size = len(arr)
tich = ""
for i in range(0, size - 1):
    tich = tich + str(arr[i]) + " x "
tich = tich + str(arr[size-1])
print( n, "=", tich)