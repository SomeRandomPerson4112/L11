number=int(input("Enter your number: "))
count=0
while number!=0:
    count+=1
    number=number//10
print(count)