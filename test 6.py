n = int(input("Enter Your Number: "))
old=n;
sum =0
while(n > 0):    
    r = n %10    
    sum = (sum *10) + r
    n = n //10    
if(old == sum): 
     print("true")  
