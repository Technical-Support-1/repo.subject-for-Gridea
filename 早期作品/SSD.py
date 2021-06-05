x = eval(input("enter my list: "))
for n in x:
    type(n)
    h=bool(isinstance(n,list))
if h==True:
    i=3
    a=3
    b=-1
    z=[]
    while i>0:
        a=a-1
        b=b+1
        z.append(x[b][a])
        i=i-1
    print(z)
else:
    print("Please press the right list")
