x = eval(input("enter my list: "))
c=[]
for n in x:
    c.append(n)
if c[0] and c[1] and c[2]==True:
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
    print("Please press the right list!")
