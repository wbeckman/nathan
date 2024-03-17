#Problem Set 1
#Main variables casted from float inputs
annual_salary= float(input("What is your annual salary? "))
portion_saved= float(input("What percentage of your monthly pay do you put towards the down payment?"))
total_cost= float(input("What is the cost of your dream home? "))
semi_annual_raise= float(input("What is your semi-annual raise in decimal of your current annual salary?"))

portion_down_payment= .25*total_cost
current_savings= 0.0

#maybe months_needed should be in the while statement?
months_needed = 0

#creating while loop because its an 'until' situation
while True:
    months_needed+=1
    if months_needed in range(6,1200,6):
        annual_salary+=(semi_annual_raise*annual_salary)
        #print(annual_salary)
        
    current_savings += portion_saved*(annual_salary/12)+((current_savings*.04)/12)
    #print(current_savings, months_needed)
    if current_savings>=portion_down_payment:
        print("Number of months:",months_needed)
        break
    
    


