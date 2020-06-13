import pandas as pd #importing the pandas package

bill = [34,108,64,88,99,51] #Bill Amount
tips = [5,17,11,8,14,5] #Tip Amount

df = pd.DataFrame(list(zip(bill, tips)), columns =['bill_amt', 'tip_amt']) #Creating DataFrame

df['bill_amt'].mean() #Mean/Average of Bill Amount

df['tip_amt'].mean() #Mean/Average of Tip Amount

df['bill_amt']-df['bill_amt'].mean() #Xi - X-bar

df['tip_amt']-df['tip_amt'].mean() #Yi - X-bar

(df['bill_amt']-df['bill_amt'].mean()) * (df['tip_amt']-df['tip_amt'].mean()) #(xi - xbar) * (yi - ybar)

(df['bill_amt']-df['bill_amt'].mean())**2 #(xi - xbar)^2

# b1 = Sum((xi - xbar) * (yi - ybar)) / Sum(xi - xbar)
b1 = ((df['bill_amt']-df['bill_amt'].mean()) * (df['tip_amt']-df['tip_amt'].mean())).sum()/((df['bill_amt']-df['bill_amt'].mean())**2).sum()

# b0 = (ybar - xbar) * b1
b0 = df['tip_amt'].mean()-(df['bill_amt'].mean()*b1)

#Simple Linear Regression Formula
#y = b0 + b1*x
#where:
# y is the dependant variable which we will be predicting
# x is the independant variable
# b0 is the Y intercept
# b1 is regression slope

#Function Created to predict Y based on X
def pred(x):
    return b0 + (b1 * x)
#X will be the bill amount and outcome will be the tip amount 

pred(10)
#Output was 0.6419400855920117
#For a $10 bill tip would be 0.6419400855920117 or $0.64 

pred(70)
#Output was 9.4151212553495 

pred(80)
#output was 10.877318116975749