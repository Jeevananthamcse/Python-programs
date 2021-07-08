a=int(input("ENTER THE FIRST NUMBER :"))
x=a;
b=int(input("ENTER THE SECOND NUMBER :"))
y=b;
n=int(input("ENTER THE RANGE  :"))
#for two digits
for i in range(1,n+1):
     if(i<10):
          if(i==x or i==y):
               print("\n",i)
     elif(i>=10 and i<100):
          f=i//10
          s=i%10
          #print("f=",f)
          #print("s=",s)
          if(((f==x)or(f==y))and ((s==x)or(s==y))):
               print("\n",i)
     elif(i>=100 and i<1000):
          f=i//100
          stemp=i//10
          s=stemp%10
          ttemp=i%10
          t=ttemp%10
          
          if((f==x)or(f==y))and ((s==x)or(s==y)) and ((t==x)or(t==y)):
               print("\n",i)
          
     else:
          print("invlid range")
               
     






