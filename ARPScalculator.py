#Requirements:
#Must be able to determine eligibility by the income requirements, marital status,
#• Adjusted Gross Income(AGI) of Individuals making <= $75,000 yearly
#• Adjusted Gross Income(AGI) of individuals making >= $80,000 yearly (Excluded)
#• Adjusted Gross Income(AGI) of Couples who file taxes jointly and making <= $150,000.00 yearly.
#• Adjusted Gross Income(AGI) of Couples who file taxes jointly and making >= $160,000.00 yearly (Excluded)
#• Adjusted Gross Income(AGI) of Head of household (Single Parent) making <= $112,500 
#• Adjusted Gross Income(AGI) of Head of household (Single Parent) making >= $120,000
#•

#Must be able to calculate stimulus amount by the number of household dependants

#• All dependant children, including students up to age 19, or age 24 for full-time college students.
#•
import json
marital_status = input("What is your marital status, married or unmarried?")

if marital_status == "unmarried":
    print("As an unmarried individual you are eligible to receive $1,400.00.")
elif marital_status == "married":
    print("As a married couple you are eligible to receive $1,400.00 each.")

AGI = float(input("What is your Adjusted Gross Income?:"))

if AGI <= 75000.00 and marital_status == "unmarried":
    print("Congratulations, you are eligible for a stimulus check in the amount of $1,400.00!")
elif AGI >= 75000.00 and marital_status == "married":
    print("Congratulations, you are eligible for a stimulus check in the amount of $2,800.00!")
elif AGI >= 80000.00 and marital_status == "married":
    print("Congratulations, you are eligible for a stimulus check in the amount of $2,800.00!")
elif AGI >= 80000.00 and marital_status == "unmarried":
    print("Sorry, you are not eligible for a stimulus check because you are over the appointed threshold.")
elif AGI <= 150000.00 and marital_status == "married":
    print("Congratulations, you are eligible for a stimulus check in the amount of $2,800.00!")
elif AGI >= 150000.00 and marital_status == "married":
    print("Sorry, you are not eligible for a stimulus check because you are over the appointed threshold.")
else:
    print("Sorry, you are not eligible for the stimulus check.")

dependants = input("Do you have any dependants? yes/no")

if dependants == "yes":
    print("For each dependant an additional $1,400.00 will be added to your stimulus total.")
else:
    print(" Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way! ")

total_stimulus = int(input("How many dependants will you be claiming?:"))

if total_stimulus == 1 and marital_status == "unmarried":
    print("Your stimulus total is $2,800.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 1 and marital_status == "married":
    print("Your stimulus total is $4,200.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 2 and marital_status == "unmarried":
    print("Your stimulus total is $4,200.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 2 and marital_status == "married":
    print("Your stimulus total is $5,600.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 3 and marital_status == "unmarried":
    print("Your stimulus total is $5,600.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 3 and marital_status == "married":
    print("Your stimulus total is $7,000.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 4 and marital_status == "unmarried":
    print("Your stimulus total is $7,000.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 4 and marital_status == "married":
    print("Your stimulus total is $8,400.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 5 and marital_status == "unmarried":
    print("Your stimulus total is $8,400.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 5 and marital_status == "married":
    print("Your stimulus total is $9,800.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 6 and marital_status == "unmarried":
    print("Your stimulus total is $9,800.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 6 and marital_status == "married":
    print("Your stimulus total is $11,200.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 7 and marital_status == "unmarried":
    print("Your stimulus total is $11,200.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 7 and marital_status == "married":
    print("Your stimulus total is $12,600.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 8 and marital_status == "unmarried":
    print("Your stimulus total is $12,600.00.")
    print("Thank you for using,the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 8 and marital_status == "married":
    print("Your stimulus total is $14,000.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 9 and marital_status == "unmarried":
    print("Your stimulus total is $14,000.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 9 and marital_status == "married":
    print("Your stimulus total is $15,400.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 10 and marital_status == "unmarried":
    print("Your stimulus total is $15,400.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus == 10 and marital_status == "married":
    print("Your stimulus total is $16,800.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus >= 11 and marital_status == "unmarried":
    print("How do you feed that army of yours? Your stimulus total is $16,800.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")
elif total_stimulus >= 11 and marital_status == "married":
    print("How do you feed that army of yours? Your stimulus total is $18,200.00.")
    print("Thank you for using the American Rescue Plan Stimulus Calculator, your stimulus is on the way!")