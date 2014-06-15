##Name: Juan dela Cruz
##Time Spent: 2 hours
##Collaborators: Juana Sing and Pedro Penduko
#
import sys

message = "Please enter the starting balance: "
bal_start = float(input(message))

message = "Please enter the finance charge as a decimal: "
fin_charge = float(input(message))

message = "Please enter the rate for minimum amount due as a decimal: "
min_amount_due = float(input(message))

message = "Please enter the default minimum amount due: "
def_min_a_due = float(input(message))

count = 0
amount_paid = 0.0

while (bal_start > 0):
    #determine minimum amount due in current month
    min_mon_due = 0.0;
    per_mon_due = min_amount_due * bal_start
    if per_mon_due > def_min_a_due:
        min_mon_due = per_mon_due
        #end if
    else:
        min_mon_due = def_min_a_due
        #end if-else
    new_bal = (bal_start - min_mon_due) * (1 + fin_charge)
    amount_paid = amount_paid + min_mon_due#to determine amount to pay
    bal_start = new_bal#credit is determined via bal_start
    count = count + 1#time frame to pay debt is determined by count
    #end while

print("It takes ", count, " months", "to totally pay-off the debt.")
print("Total amount paid is PhP", round(amount_paid,2))
print("Remaining credit is ", round(new_bal,2))
#end module
