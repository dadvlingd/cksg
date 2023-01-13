import sys
a=str(sys.argv[1])
b=[]
c=""
for i in range(0,len(a)//4):
    b.append(a[i*4:i*4+4])
b=['1' if i == '1110'else i for i in b]
b=['0' if i == '1000'else i for i in b]
for i in range(0,len(b)):
    c=c+str(b[i])
d = hex(int(c,2))
print("-----------------------")
print("1527解码:%s"%c)
print("data:%s"%d[:-1])
print("Func:%s"%d[-1:])
print("-----------------------")