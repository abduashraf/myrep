a = int(input("number?"))
i = 2
j=0
while(i<a):
    if a%i == 0:
        j+=1
    i+=1
if j>0:
    print("Non-prime")
else:
    print("prime")
print("The prime is found, right?")
