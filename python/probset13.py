##Name: Juan dela Cruz
##Time Spent: 2 hours
##Collaborators: Juana Sing and Pedro Penduko
#
import sys

message = "Please enter the starting balance: "
input_bal = float(input(message))

message = "Please enter the finance charge as a decimal: "
fin_charge = float(input(message))

bal_start = input_bal
mon_pay = round(bal_start / 12.0)
while (bal_start > 0):
    count = 0
    bal_start = input_bal
    amount_paid = 0.0
    while (count < 12):
        new_bal = (bal_start - mon_pay) * (1 + fin_charge)
        bal_start = new_bal#credit is determined via bal_start
        amount_paid = amount_paid + mon_pay#determine amount paid
        count = count + 1
        #end while (count < 12)
    mon_pay = mon_pay + 10.0
    #end while (bal_start > 0)

print("Your monthly fix payment is ", mon_pay)    
print("You paid a total of PhP", amount_paid)
print("Remaining credit is PhP", round(bal_start,2))
#end module
