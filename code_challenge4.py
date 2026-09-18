print("----------------------------------------Create Account----------------------------------------")
a = input("Enter your email----> ")
b = input("Enter your password----> ")
print("----------------------------------------Login-------------------------------------------------")
username = input("Enter your username----> ")
password = input("Enter your password----> ")

if username == a and password == b:
  print("Access Granted")
else:
  print("Access Denied")




age = int(input("How old are you?----> "))

if age < 65:
  print("eligible for loan")
else:
  print("not eligible for loan")

is_employed = input("Are you employed? yes/no----> ")  == "yes"
credit_score = eval(input("What is your credit score?----> "))
annual_income = eval(input("What is your annual income?----> "))
has_collateral = input("Collateral? yes/no----> ") == "yes"
collateral_description = input("What is the collateral you will give?----> ")
collateral_value = eval(input("What is the value of the collateral?----> "))

if collateral_value < 30000:
  print("\nCollateral value is too low for loan approval")
else:
  print("\nCollateral value is sufficient for loan approval")

#Baseline eligibilty criteria for loan approval and Tier 1
if age >= 21 and is_employed:
  if credit_score >= 750:
    baseline_interest_rate = 5
    if annual_income >= 100000:
      baseline_interest_rate = 4.5
      print("\nYou are eligible for a loan with an interest rate of", baseline_interest_rate, "%")
    else:
        print("\nYou are eligible for a loan with an interest rate of", baseline_interest_rate, "%")
else:
  print("\nYou are not eligible for a loan at this time.")

#Tier 2 eligibility criteria for loan approval
if credit_score >= 600 and credit_score < 750:
  base_interest_rate = 8
  if has_collateral:
    base_interest_rate = 7
    print("\nYou are eligible for a loan with an interest rate of", base_interest_rate,  "%")
  elif has_collateral and annual_income < 40000:
    base_interest_rate = 9.5
    print("\nYou are eligible for a loan with an interest rate of", base_interest_rate,  "%")
  else:
    print("\nYou are eligible for a loan with an interest rate of", base_interest_rate,  "%")


#Tier 3 eligibility criteria for loan approval
if credit_score < 600:
    print("\nRejected: Credit Score too low")
print("________________________________________________________________________________________________________________________\nAge: ", age, "\nEmployed?: ", is_employed, "\nCredit Score: ", credit_score, "\nIncome: ", annual_income, "\nHas Collateral?: ", has_collateral, "\nCollateral Description: ", collateral_description, "\nCollateral Value: ", collateral_value)

