#Problem Set 1 part c
#Main variables casted from float inputs
annual_salary= float(input("What is your annual salary? "))
total_cost= 1000000.00

#portion_saved= float(input("What percentage of your monthly pay do you put towards the down payment?"))
portion_down_payment= .25*total_cost
months = 0
low=0
high=10000
epsilon=100
num_guesses=0

#function to calculate savings over the time interval
def Savings_func(x,y):
     """
     Input: x, a positive integer representing a guess, and y the annual salary from main program
     Returns a total savings after 36 months with
     """
     #print("guess being sent to func:", x)
     annual_salary=y
     Savings=0
     semi_annual_raise= .07
     for i in range(1,36,1):
            if i in range(6,37,6):
                annual_salary += (semi_annual_raise*annual_salary)
            Savings+= (x/10000)*(annual_salary/12)+((Savings*.04)/12)
     return Savings

#bisection search tree   
while True:
    guess=(high+low)/2
    if abs(Savings_func(guess,annual_salary)-portion_down_payment)<= epsilon:
         print("A monthly savings rate of ",float(guess/10000),"is close to optimal for your salary and dream home price!")
         print(Savings_func(guess,annual_salary))
         print("Steps in bisection search:",num_guesses)
         break
    elif Savings_func(guess,annual_salary) > portion_down_payment:
         high=int(guess)
         #print("guess too high, new high bound:",high)
    elif Savings_func(guess,annual_salary) < portion_down_payment:
         low=int(guess)
         #print("guess too low, new low bound:",low)
    if low==9999:
         print("It is not possible to pay the down payment in three years.")
         break
    if num_guesses>20:
         break
    num_guesses+=1
    # print("total savings on this iteration:", Savings_func(guess,annual_salary))
    # print("num_guesses:",num_guesses)

   