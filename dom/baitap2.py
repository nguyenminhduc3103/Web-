arr = [int(input("Nhập số a: ")),int(input("Nhập số b: ")),int(input("Nhập số c: ")),int(input("Nhập số d: "))]
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort(arr)
print("Số lớn nhất là: ", arr[-1])
print("Số lớn thứ 2 là: ", arr[-2])