#Group Age

sum_age = 0
age_older_man = 0
name_older_man = ''
total_young_woman = 0

for people in range (0, 4):
	name = input('Enter a name:').strip()
	age = int(input('Enter a age:'))
	sex = input('Enter M for male or F for female: ').strip().upper()
	
	sum_age += age
	
	if sex == 'M':
		if age > age_older_man:
			age_older_man = age
			name_older_man = name
			
	elif sex == 'F' and age < 20:
		total_young_woman += 1
		
average=sum_age / 4
print(f'The average age is: {average}')
print(f'The name of the older man is: {name_older_man}')
print(f'The total number of young woman is: {total_young_woman}')
		
		