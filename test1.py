str=input("enter the string :")
# iterate over string
for index in range(len(str)):
    # check if index is divisible by 2
    if index % 2 == 0:
        # print character at index
        print(str[index], end='')
