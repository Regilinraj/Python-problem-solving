#Print your name, your college, and your department, each on its own line.
print("Name:Regilin")
print("college:CSI Institute of technology")
print("Department:CSE")

#Print exactly this using only print() and *:
#           *****
#           *****
#           *****

print("*"*5)
print("*"*5)
print("*"*5)


#Using sep, print 2026-10-28 from print("2026", "10", "28").
print("2026","10","28",sep="-")

#Using end, print 1 2 3 4 5 on one line using five separate print() calls.
print(1,end=" ")
print(2,end=" ")
print(3,end=" ")
print(4,end=" ")
print(5,end=" ")

#Print this table using \t:
#        Name	Marks
#        Ravi	80
#        Mani	92
print()
print("Name\tMarks")
print("Ravi\t80")
print("Mani\t92")

#A6. Print: She said "Python is easy" (with the quotes appearing in the output).
print("She said \"Python is easy\"")

#Store your name, age, and city in variables and print one sentence using an f-string.
name="Regilin"
age=25
city="nagercoil"
print(f"{name} is {age} years old living in {city}")

#Swap two numbers: a = 10, b = 20. Print a = 20, b = 10.
a=10
b=20
a,b=b,a
print(f"a={a}, b={b}")

#Print the type of each: 42, 4.2, "42", True, "True". Write down your prediction first.
print(type(42))    #int
print(type(4.2))   #float
print(type("42"))  #str
print(type(True))  #bool
print(type("True")) #str

#What do int(7.9), int("12") + 1, float(3), and str(5) + "5" print? Predict, then run.
print(int(7.9))      #7
print(int("12")+1)   #13
print(float(3))      #3.0
print(str(5)+"5")    #55

#Use bool() on 0, 1, "", " ", "False". Predict the answer first and explain why "False" is True.
print(bool(0))    #False
print(bool(1))    #True
print(bool(""))   #False
print(bool(" "))  #True  space also consider as non empty so true
print(bool("False"))    #True because non empty string is True

#Given a = 17, b = 5, print a + b, a - b, a * b, a / b, a // b, a % b, a ** b.
a=17
b=5
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a//b)
print(a**b)

#Area and perimeter of a rectangle with length 12 and breadth 7.
length=12
breadth=7
area=length*breadth
perimeter=2*(length+breadth)
print("Area: ",area)
print("Perimeter: ",perimeter)

#Simple interest: P*R*T/100 with P=5000, R=6, T=3. Answer: 900.0.
P=5000
R=6
T=3
simple_interest=P*R*T/100
print("Simple Interest: ",simple_interest)

#Celsius to Fahrenheit: F = C * 9/5 + 32. For C=100, the answer is 212.0.
c=100
F=c*9/5+32
print("Celsius to Fahrenheit: ",F)

#Convert 17 days into weeks and days using // and %. Output: 2 weeks 3 days.
print(f"{17//7} weeks {17%7} days")

#Convert 7384 seconds into hours, minutes, and seconds. Output: 2 hours 3 minutes 4 seconds.
#Hint: hours = seconds // 3600. The remainder is seconds % 3600. Do the same again for minutes.
seconds=7384
hours=seconds//3600
remainder=seconds%3600
minutes=remainder//60
seconds=remainder%60
print(f"{hours} hours {minutes} minutes {seconds} seconds")

#For num = 4825, print the last digit, the number without the last digit, and the last two digits (no loops).
num=4825
print(num%10)
print(num//10)
print(num%100)

#For the 3-digit number 345, find the sum of its digits (no loops). Answer: 12.
#Hint: hundreds = 345 // 100, tens = (345 // 10) % 10, ones = 345 % 10.
num=345
hundreds=num//100
tens=(num//10)%10
ones=num%10
print(hundreds+tens+ones)

#Predict and then run: print(10 > 5 and 3 > 8), print(not (5 == 5)), print(5 > 3 or 1 /0)
#Why doesn’t the last one crash? (Think about when or stops checking.)

print(10>5 and 3>8)
print(not(5==5))
print(5>3 or 1/0)

#Ask for the user’s name and print Hello, <name>! Welcome.
name=input("Enter the user name: ")
print(f"Hello, {name}! Welcome.")

#Ask for two numbers and print their sum, difference, product, and division (2 decimals).
num1=int(input("Enter first number: "))
num2=int(input("Enter Second number: "))
print("sum: ",num1+num2)
print("difference: ",num1-num2)
print("product: ",num1*num2)
print(f"division: {num1/num2:.2f}")

#Ask for the radius and print the area of the circle using 3.14159 * r * r, with 2 decimals. For r=5 the answer is 78.54.
r=int(input("Enter radius: "))
pi=3.14159
area=pi*r*r
print(f"radius {area:.2f}")

#Ask for a name and print its length and its uppercase form.
name=input("Enter your name: ")
print(f"length {len(name)}")
print(f"Upper case {name.upper()}")

#Ask for 3 subject marks and print the total and the average with 2 decimals.
sub1=int(input("Enter sub1 mark: "))
sub2=int(input("Enter sub2 mark: "))
sub3=int(input("Enter sub3 mark: "))
total=sub1+sub2+sub3
average=total/3
print("total: ",total)
print(f"average: {average:.2f}")

#Read two numbers on one line (5 3) using map(int, input().split()) and print the larger one without using an if (hint: use max()).
a,b=map(int,input("Enter numbers: ").split())
print(f"Larger numer {max(a,b)}")

#Positive, negative, or zero.
#Test: 5 Positive, -3 Negative, 0 Zero.
number=int(input("Enter number: "))
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")

#Even or odd.
num=int(input("Enter number: "))
if num%2==0:
    print("even")
else:
    print("odd")

#Voting eligibility (age 18 or more).
age=int(input("Enter age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

#Grade calculator:

#  90 or more: A
#  75 to 89: B
#  60 to 74: C
#  40 to 59: D
#  below 40: Fail
mark=int(input("Enter mark: "))
if mark>=90:
    print("A grade")
elif mark>=75:
    print("B grade")
elif mark>=60:
    print("C grade")
elif mark>=40:
    print("D grade")
elif mark<40 and mark>=0:
    print("Fail")
else:
    print("Invalid")

#Larger of two numbers, or “Both are equal”.
num1=int(input("NUM1: "))
num2=int(input("NUM2: "))
if num1>num2:
    print(num1,"is largest")
elif num2>num1:
    print(num2,"is largest")
else:
    print("equal")

#Largest of three numbers. Test with the largest in each position.
n1=10
n2=45
n3=67
if n1>=n2 and n1>=n3:
    largest=n1
elif n2>n3:
    largest=n2
else:
    largest=n3
print("largest number: ",largest)

#Smallest of three numbers (use Worked Example 3 as a model, but type it yourself).
a=34
b=89
c=56
if a<=b and a<=c:
    smallest=a
elif b<c:
    smallest=b
else:
    smallest=c
print("Smallest number: ",smallest)

#FizzBuzz for one number.

#Divisible by 3 and 5: FizzBuzz
#Only 3: Fizz
#Only 5: Buzz
#Otherwise: print the number
num=3
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)

#Leap year checker. Test: 2024 Leap, 1900 Not leap, 2000 Leap, 2023 Not leap.
year=int(input("Enter year to check leap year or not: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year") 

#Vowel or consonant (handle uppercase).
#Test: a, E, z, U.
letter=input("Enter alphabet").lower()
if letter in "aeiou":
    print("vowel")
else:
    print("Consonent")

#Character type. Read one character and print whether it is a digit, a letter, or something else (special character).
#Test: 7 Digit, k Letter, # Special.
#Hint: ch.isdigit() and ch.isalpha().

value=input("Enter a value: ")
if value.isdigit():
    print("digit")
elif value.isalpha():
    print("letter")
else:
    print("special")

#Day of the week. Read a number 1 to 7 and print Monday to Sunday. Otherwise print Invalid day.
number=int(input("Enter number from 1 to 7: "))
if number==1:
    print("Sunday")
elif number==2:
    print("Monday")
elif number==3:
    print("Tuesday")
elif number==4:
    print("Wednesday")
elif number==5:
    print("Thursday")
elif number==6:
    print("Friday")
elif number==7:
    print("Saturday")
else:
    print("Invalid")

#Electricity bill:

#Up to 100 units: free
#101 to 200 units: Rs 2 per unit above 100
#Above 200 units: Rs 3 per unit above 200, plus the Rs 2 charge for the 101 to 200 slab

#Test: 80 Rs 0, 150 Rs 100, 250 Rs 350.

unit=int(input("Enter electricity unit: "))
if unit<=100:
    amount=0
elif unit<=200:
    amount=(unit-100)*2
else:
    amount=(100*2)+(unit-200)*3
print("Units ",unit)
print("Bill: ",amount) 

#Triangle type. Read three sides:

#Not a triangle if the sum of any two sides is not greater than the third
#Otherwise: Equilateral, Isosceles, or Scalene

#Test: 3 3 3, 3 3 5, 3 4 5, 1 2 5.
a=int(input("Enter side1: "))
b=int(input("Enter side2: "))
c=int(input("Enter side3: "))
if a+b<=c or b+c<=a or c+a<=b:
    print("Not a valid triangle")
elif a==b and b==c:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#Simple calculator. Read two numbers and an operator (+, -, *, /). Handle division by zero and invalid operators.
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))
operator=input("Enter the operator(+,-,*,/): ")
if operator=="+":
    print("Result: ",num1+num2)
elif operator=="-":
    print("Result: ",num1-num2)
elif operator=="*":
    print("Result: ",num1*num2)
elif operator=="/":
    if num2==0:
        print("Division by zero is not possible")
    else:
        print("Result: ",num1/num2)
else:
    print("Invalid operator")

#Check whether three numbers are in ascending order (a ≤ b ≤ c). Print Sorted or Not sorted. Try it with a chained comparison.
a=5
b=6
c=7
if a<=b<=c:
    print("Sorted")
else:
    print("not sorted")

#ATM logic. Balance is 5000. Read a withdrawal amount.

#If the amount is not a multiple of 100, print Enter a multiple of 100
#Else if the amount is more than the balance, print Insufficient balance
#Else print Collect cash and the remaining balance

#Test: 250, 6000, 1500.
balance=5000
amount=int(input("Enter amount to withdraw: "))
if amount%100!=0:
    print("Enter a multiple of 100")
elif amount>balance:
    print("Insufficient balance")
else:
    remaining_bal=balance-amount
    print("collect cash")
    print("Remaining balance: ",remaining_bal)



