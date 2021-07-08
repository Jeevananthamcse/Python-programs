#polyntrome string
word=input("ENTER YOUR WORD :")
temp=word;
str=" "
for x in word:
     str=x+str
print(str)
if(temp==str):
     print("\n PLOYNDROME STRING ")
else:
     print("\n NOT A PLYNDROME STRING ")
