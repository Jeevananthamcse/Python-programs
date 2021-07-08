n= int(input("Enter the integer number: "))  
sum= 0  
while (n>0):  
    r= n%10  
    sum= (sum * 10) +r
    n=n// 10  
print("The reverse number is : {}".format(sum))   
