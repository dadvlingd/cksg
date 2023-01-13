
data=input("请输入data:")
Func=input("请输入Func:")
a=data+Func
b=bin(int(a,16))[2:]
c=""
for i in b:
    if(i=="1"):
        c=c+"1110"
    if(i=="0"):
        c=c+"1000"
print("原始数据:%s"%(c+"1"))

