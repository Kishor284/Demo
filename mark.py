markOne=int(input())
markTwo=int(input())
markThree=int(input())
markFour=int(input())
total=markOne+markTwo+markThree+markFour
avg=total/4

if (avg>91) and (avg<100):
    print("your grade is A1")
elif (avg>81) and (avg<91):
    print("your grade is A2")
elif (avg>71)and (avg<81):
    print("your grade is B1")
elif (avg>61) and (avg<71):
    print("your grade is B2")
elif (avg>51)and (avg<61):
    print("your grade is C1")
elif (avg>41) and (avg<51):
    print ("your grade is C2")
elif (avg>31) and (avg<41):
    print("your grade is D1")
elif (avg>21) and (avg<31):
    print("your grade is E")
elif (avg>0) and (avg<21):
    print("your grade is f")
else :
    print("invalid input")
