month=int(input("enter the month number"))
'''31 days=1,3,5,7,8,10,12
30days=4,6,9,11
28 or 29 days=2'''
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("31 days")
elif(month==2):
    print("28 or 29 days")
elif(month==4 or month==6 or month==9 or month==11):
    print("30 days")
else:
    print("invalid month")