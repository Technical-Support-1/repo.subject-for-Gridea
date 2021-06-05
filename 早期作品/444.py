i=1
p=1
while p<=9:
    i=1
    while i<=9:
        print(i,"*",p,"=",i*p)
        i=i+1
    p=p+1

# or something others...

a = input("Here's other way to do it(more simple),do you want to try?(Y/N)")
if a == "Y":
    for i in range(1,10):
        for p in range(1,10):
            print(i,"*",p,"=",i*p)
