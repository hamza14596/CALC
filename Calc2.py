print("Select an Operator")
print("1-ADD")
print("2-SUBTRACT")
print("3-MULTIPLY")
print("4-DIVIDE")
Option = input("Your Choice=")
print("Choose a Number")
Num1 = int(input("Your first Number is = "))
Num2 = int(input ("Your Second Number is = "))

if Option == "1":
    output = Num1 + Num2
elif Option == "2" :
    output = Num1 - Num2
elif Option == "3" :
    output = Num1 * Num2
else :
    output = Num1/ Num2
   
print("Your Answer is ",output)

print ("Would you like to calculate again?")
Ans = input ()
if Ans == "No" or "no" :
    print ("Goodbye!") 

if  Ans == "Yes" :
    print("Select an Operator")
    print("1-ADD")
    print("2-SUBTRACT")
    print("3-MULTIPLY")
    print("4-DIVIDE")
    
    Option2 = input("Your Choice=")
    print("Choose a Number")
    Num1 = int(input("Your first Number is="))
    Num2 =int(input ("Your Second Number is = "))
if Option2 == "1":
    output = Num1 + Num2
    print("Your Anwer is ", output )
elif Option == "2" :
    output = Num1 - Num2
    print("Your Anwer is ", output )
elif Option2 == "3" :
    output = Num1 * Num2
    print("Your Anwer is ", output )
else :
    output = Num1/ Num2
    print("Your Anwer is ", output )

