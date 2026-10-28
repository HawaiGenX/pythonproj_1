import random
account = {
    "Account Holder": "Jahim Edwards",
    "Accout type": "Checking",
    "balance": 250000.00,
    "last transaction": "none"
}
print("\n")
print(f"Welcome {account['Account Holder']}!, how can we help you today?")

service = input("Choose service (deposit, withdrawal, balance): ")
if service == "deposit":
    deposit = float(input("Enter amout you want to deposit: "))
    account["balance"] += deposit
    account["last transaction"] = f"deposit of ${deposit:,.2f}"
    print(f"Deposited amount is:${deposit:,.2f} and your balance is:${account['balance']:,.2f}")
elif service == "withdrawal":
    available_funds = account["balance"]
    withdrawal = float(input("Enter amount you want to withdraw: "))
    if withdrawal <= account["balance"]:
        account["balance"] -= withdrawal
        account["last transaction"] = f"withrawal of ${withdrawal:,.2f}"
        print(f"Available funds: ${available_funds:,.2f} and amount withdrawn is: ${withdrawal:,.2f} and your balance is: ${account['balance']:,.2f}")
    else:
        print("Insufficient funds. Withdrawal cancelled.")
elif service == "balance":
    print(f"Your current balance is: ${account['balance']:,.2f}")
    
else:
    print("Invalid service. Please choose deposit, withdrawal, or balance")

print("\n")
for key,value in account.items():
    print(f"{key.replace('-', ' ').title()}: {value}")
print("\n")          
    







