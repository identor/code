##Name: Juan dela Cruz
##Time Spent: 2 hours
##Collaborators: Juana Sing and Pedro Penduko
#
import sys
bal_start = input("Please enter the starting balance: ")
fin_charge = input("Please enter the finance charge as a decimal: ")
min_amount_due = input("Please enter the rate for minimum amount due as a decimal: ")

count = 1
while (count < 13):
    min_mon_due = float(min_amount_due) * float(bal_start)
    new_bal = ((float)(bal_start) - min_mon_due) * (1 + float(fin_charge))
    bal_start = float(new_bal)
    print("Starting balance is: ", round(bal_start,2))
    print("Minimum amount due is: ", round(min_mon_due,2))    
    print("New balance for month", (count + 1), "is:", round(new_bal,2))
    count = count + 1
##end module##


