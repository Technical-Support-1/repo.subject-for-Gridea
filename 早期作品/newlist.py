x = input("enter your list: ")
h = []
if len(x) == 0:
    print("Please press the right list!")
else:
    for b in x:
        h.append(b)
    if h[0] != "[":
        print("Please press the right list!")
    else:
        if h[len(h)-1] != "]":
            print("Please press the right list!")
        else:
            s=eval(x)
                    
            for n in s:
                type(n)
                if bool(isinstance(n,list)):
                    k=3
                else:
                    print("Please press the right list!")
                    k=5
                    break
            if k != 5:
                i=3
                a=3
                b=-1
                z=[]
                while i>0:
                    a=a-1
                    b=b+1
                    z.append(s[b][a])
                    i=i-1
                print(z)
