Balance = 300000
def bank(value):
	userId = input("USER id  ")
	passWord = input("Password  ")
	while(value):
		if userId == 'ruthvik' and passWord == '1234' :
			value=choice(value,userId,passWord)
			return value

def choice(value,userId,passWord):
	print("1. Account detail")
	print("2. Account balance")
	print("3. Money Transfer")
	print("4. Logout")
	choice=input('choice any of the above option  ')
	if choice == '1':
		return AccountDetail(value,userId,passWord)
	elif choice == '2':
		return AccountBalance(value,userId,passWord)
	elif choice == '3' :
		return MoneyTransfer(value,userId,passWord)
	elif choice == '4':
		return 0

def AccountDetail(value,userId,passWord):
	print("Account no.")
	print(userId+passWord)
	print("Balance")
	print(Balance)
	ReturnOrNot(value,userId,passWord)

def AccountBalance(value,userId,passWord):
	print("'Your Account Balance Is'")
	print(Balance)
	ReturnOrNot(value,userId,passWord)

def MoneyTransfer(value,userId,passWord):
	global Balance
	Amount=int(input("Enter Amount To Be Transfer  "))
	if Amount <= Balance:
		pas = input("Enter your Password  ")
		if  pas== '1234':
			Balance = Balance-Amount
			print(Amount,"has Been Deducted From Your Account ")
			print("Remaing Balance",Balance)
		else:
			print('Incorret Password')
	else:
		print("Insuficient Balance")
	ReturnOrNot(value,userId,passWord)
	

def ReturnOrNot(value,userId,passWord):
	a = input("Back To Previous Menu 'Yes' or 'No' ") 
	if a == "Yes"  :
		return choice(value,userId,passWord)
	else:
		return 0

a=input("do you wnat to start banking 'Yes' OR 'No'  ")
if a == 'Yes' : 
	value=1 
else:
	value=0
bank(value)
print("Thanyou for choicing us ")