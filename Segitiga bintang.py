print("a. Segitiga Atas")
x = int(input("Masukkan tinggi : "))
for i in range(x,0,-1):
    if i==x:
        print(i*'*')
    else:
        print(' '*(x-i)+'*'*(x-(x-i)))


print("b. Segitiga Sama Sisi Terbalik")
x = int(input("Masukkan tinggi : "))
for i in range(x,0,-1):
    if i==x:
        print((i*2-1)*'*')
    else:
        print(' '*(x-i)+'*'*((x-(x-i)+i-1))) 


print("c. Belah Ketupat")
x=int(input("Masukkan tinggi : "))
n=1
m=x//2
for i in range ((x//2)+1,0,-1):
    print(" "*(i-1)+((n*2-1)*"*"))
    n+=1
for j in range (1,(x//2)+1):
    print(" "*(j)+((m+1)*"*"))
    m-=2


