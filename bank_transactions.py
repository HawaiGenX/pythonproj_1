account = {
    "Account Holder": "Jahim Edwards",
    "Accout type": "Checking",
    "balance": 250000.00,
    "last transaction": "Grocery store"
}

print(f"Welcome {account['Account Holder']}!, how can we help you today?")
deposit = float(input("Enter amout you want to deposit: "))
current_balance = account["balance"]
current_balance+=deposit
account["balance"] = current_balance



