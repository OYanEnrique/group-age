# Group Age v2

print('=-' * 30)

print('Age Verification')

adults = men = woman = sum_age = sum_name = 0
ask_continue = 'Y'

while True:
	name=input('Enter your name:\n')
	age = int(input('Enter your age:\n'))
	gender = input('Enter your gender:\n').strip().upper()[0]
	
	if age >= 18:
		adults += 1
	if gender == 'M':
		men += 1
	elif gender == 'F' and age <= 20:
		woman += 1
	sum_age += age
	sum_name +=1
	average = sum_age / sum_name
	
	ask_continue = input('Continue? [Y or N]').strip().upper()[0]
	if ask_continue == 'N':
		print('Program closed successfully\n')
		break
			
print(f'Results: There are {adults} adults, {men} men and {woman} women under the age of 20, the average age was {average}!')

print('=-' * 30)
