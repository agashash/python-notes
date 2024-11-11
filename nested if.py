""" Exercise 1: Grade Classification
Write a program that asks the user for their score and classifies it into a letter grade with additional distinctions based on the score range.

Instructions:

Get the score from the user.
Use a nested if statement to classify the score:
If the score is 90 or above, print "Grade: A" and "Excellent!" if the score is above 95.
If the score is between 80 and 89, print "Grade: B" and "Well done!" if the score is above 85.
If the score is between 70 and 79, print "Grade: C."
If the score is between 60 and 69, print "Grade: D."
If the score is below 60, print "Grade: F." """

""" 

score=int(input("Enter your Score:"))
if score>=90:
    if score>=95:
        print("Excellent!,Your score greater than 95")    
    else:
        print("Grade:A")
elif score>=80 and score<90:
    if score>=85:
        print("Well Done!, Your score Greater than 85")
    else: 
         print("Grade:B")   
elif score>=70:
     print("Grade:c")
elif score>=60:
     print("Grade:D")         
else:
    print("Grade: F") 
"""

""" 
Exercise 2: Weather Advice
Create a program that suggests an outfit based on the temperature and whether it is raining.

Instructions:

Ask the user for the current temperature (in degrees Celsius) and whether it is raining (yes or no).
Use nested if statements to provide suggestions:
If the temperature is above 20 degrees:
If it is raining, suggest wearing a light jacket and carrying an umbrella.
Otherwise, suggest wearing a t-shirt.
If the temperature is between 10 and 20 degrees:
If it is raining, suggest wearing a waterproof jacket.
Otherwise, suggest wearing a sweater.
If the temperature is below 10 degrees, suggest wearing a heavy coat.
 """
""" 
temp=int(input("Enter a temperature in c:"))
rain=input("yes or No:")
if temp>20:
    if rain=="yes":
       print("wearing a light jacket and carrying an umbrella.")
    else:
        print("wearing a t-shirt.")  
elif temp>=10 and temp<=20:
    if rain=="yes":
        print("wearing a waterproof jacket")
    else:
        print(" wearing a sweater")
elif temp<10:
    print("wearing a heavy coat")
else:
    print("Invalid!")
 """
""" 
Exercise 3: Number Classification
Write a program that classifies a number as positive, negative, or zero and further classifies it as even or odd.

Instructions:

Get a number from the user.
Use a nested if statement:
If the number is greater than zero, print "Positive".
If it is even, print "Even".
Otherwise, print "Odd".
If the number is less than zero, print "Negative".
If it is even, print "Even".
Otherwise, print "Odd".
If the number is zero, print "Zero". 
"""

""" number=int(input("Enter a Number:"))
if number>0:
    print("Positive")
    if number%2==0:
        print("even")
    else:
        print("Odd")    
elif number<0:
    print("Negative")
    if number%2==0:
        print("even")
    else:
        print("Odd") 
else:
    print("The Number is zero")
 """
""" 
Exercise 4: Quiz Scoring System
Create a quiz scoring system that gives feedback based on the number of questions answered correctly.

Instructions:

Ask the user how many questions they answered correctly out of a total of 10.
Use nested if statements to provide feedback:
If the score is 8 or above, print "Great job!" and check if the score is 10 for "Perfect score!".
If the score is between 5 and 7, print "Good effort!".
If the score is below 5, print "Better luck next time.". """

""" score=int(input("How many questions they answered correctly out of a total of 10 :"))
if score>=8:
    print("Great job!")
    if score==10:
        print("Perfect score!")
elif score >=5 and score<=7:
    print("Good effort!")
else:
    print("Better luck next time.")   """          