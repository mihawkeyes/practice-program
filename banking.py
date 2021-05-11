def choice():
	print('1. Account detail')
	print('2. Account balance')
	print('3. Money Transfer')
	print('4. Logout')
def main():
	userId = input('USER ID')
	passWord = input('Password')
	if userId == 'ruthvik' and passWord == '1234' :
		choice()