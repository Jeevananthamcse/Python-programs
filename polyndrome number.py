n=int(input("ENTER THE NUMBER :"))
old=n;
sum=0
while (n>0):
     r=(n%10)
     sum=sum*10+r
     n=n//10
if(old == sum):
     print("IT IS A POLYNDROME NUMBER ")
else:
     print("IT IS NOT A POLYNDROME NUMBER")
