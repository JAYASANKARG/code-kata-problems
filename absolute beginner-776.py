import math
n=int(input())
if(n<0):
  print("Error")
elif(n==0):
  print(0)
else:
  a=2*math.pi*n
  print("%.2f"%a)
