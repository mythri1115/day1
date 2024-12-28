mul=int(input("enter the integer number:"))
if(mul%3==0 and mul%5==0):
    print("multiple of three and five")
else:
    print("it is not a multiplication of three and five")
print("--------------")
mul=int(input("enter the integer number:"))
result="multiplication of three and five" if(mul%3==0 and mul%5==0) else "it is not a multiplication of three and five"
print(result)
    