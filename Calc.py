print("Select an Operator")
print("1-ADD")
print("2-SUBTRACT")
print("3-MULTIPLY")
print("4-DIVIDE")
Option = input("Your Choice=")
print("Choose a Number")
Num1 = int(input("Your first Number is="))
Num2 =int(input ("Your Second Number is = "))

if Option == "1":
    output = Num1 + Num2
elif Option == "2" :
    output = Num1 - Num2
elif Option == "3" :
    output = Num1 * Num2
else :
    output = Num1/ Num2
   
print(output)


