#Problem Set 1
#Main variables casted from float inputs
annual_salary= float(input("What is your annual salary? "))
total_cost= float(input("What is the cost of your dream home? "))
#multiplier variable 
portion_saved= float(input("What percentage of your monthly pay do you put towards the down payment?"))*(annual_salary/12)

portion_down_payment= .25*total_cost
current_savings= 0.0

#maybe months_needed should be in the while statement?
months_needed = 0

#initializing outside of while loop to make it more concise
#check = bool(current_savings<portion_down_payment)

#creating while loop because its an 'until' situation
while True:
    months_needed+=1
    current_savings += portion_saved + ((current_savings*.04)/12)
    #print(current_savings, months_needed)
    if current_savings>=portion_down_payment:
        print("Number of months:",months_needed)
        break
    
    
#trying if statement because I think I do want to     


#preliminary tests
#print(total_cost)


