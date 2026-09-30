owner_age = int(input("Owner Age: "))
monthly_revenue = int(input("What is your monthly revenue: "))
credit_score = int(input("What is your credit score: "))
years_in_business = int(input("How many years are you in business: "))
has_defaults = input("Has Defaults: ") == "yes"
collateral_description = input("What will you collateral: ")
collateral_value = float(input("What is the value of your collateral: "))

if owner_age >= 21:
    print("Eligible")
    if years_in_business >= 2.0:
        print("Eligible")
        if has_defaults:
            print("Eligible")
        else:
            print("Rejected: High risk Applicant")
    else:
        print("Rejected: High risk Applicant")
else:
    print("Rejected: High risk Applicant")        


#Tier 1
if credit_score >= 720:
    maximum_loan_limit = monthly_revenue * 3
    if monthly_revenue >= 50000:
        base_processing_fee = 0.015 * maximum_loan_limit
    else:
        base_processing_fee = 0.025 * maximum_loan_limit


#Tier 2
if 620 <= credit_score < 720:
    maximum_loan_limit = monthly_revenue * 1.5
    if monthly_revenue >= 5.0:
        base_processing_fee = 0.02 * maximum_loan_limit
    else:
        base_processing_fee = 0.035 * maximum_loan_limit

#Tier 3
if credit_score < 620:
    print("Rejected: Credit Score below requirement")



collateral_value >= maximum_loan_limit
if collateral_value < maximum_loan_limit:
    print("Rejected: Insufficient Collateral")


#surcharge

maximum_loan_limit * base_processing_fee
collateral_value % 5000 != 0
if collateral_value % 5000 != 0:
    base_processing_fee + 250

print("_________________________________________________")
print("Owner Age: ", owner_age)
print("Years in Business: ", years_in_business)
print("Has Defaults?: ", has_defaults)
print("Credit Score: ", credit_score)
print("Monthly Revenue: ", monthly_revenue)
print("Collateral Description: ", collateral_description)
print("Collateral Value: ", collateral_value)
print("Maximum Loan Limit: ", maximum_loan_limit)
print("Base Processing Fee: ", base_processing_fee)