def snt(n):
    if n == 0 or n ==1:
        return 0
    elif n == 2:
        return 1
    else:
        i = 2
        while i <= (int(sqrt(n+1)+1)):
            if n % i == 0:
                return 0
            i += 1
        return 1
t = int(input())
max = 0 
for i in range(0,t):
    x = int(input())
    if(snt(x)==1 and max <x):
        max = x
print(max)

