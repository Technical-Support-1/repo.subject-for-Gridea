c=input("摄氏度：")
if c.isnumeric():  
  d=int(c)
  g=d*1.8+32
  print(g)
else:
  d=float(c)
  g=d*1.8+32
  print(g)
