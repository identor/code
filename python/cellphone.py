import sys

load = float(input("Load: "))
sms_cost = float(input("Cost per text: "))
call_cost = float(input("Cost per minute: "))
n_messages = float(input("Number of messages: "))
n_calls = float(input("Calls in minutes: "))

tot_sms = sms_cost * n_messages
tot_calls = call_cost * n_calls
usage = tot_sms + tot_calls
balance = load - usage

print()
print("Cost of Messages: " + str(tot_sms))
print("Cost of calls: "  + str(tot_calls))
print("Total Usage: " + str(usage))
print("Balance: " + str(balance))

input("Press Enter to continue...")
