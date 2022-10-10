#employee_bonus
actualSalary = float(input('How much you stifund to a employee :'))
grade = input('Which grade does he/she have? :')
bonus = 0.0
if grade == 'A' or grade == 'a':
    bonus  = bonus + actualSalary * 0.05
elif grade == 'B' or grade == 'b':
     bonus  = bonus + actualSalary * 0.1
else:
    print('No such grade \'', grade, '\' in our company...')
    
actualSalary += bonus

if actualSalary >10000.00:
    bonus  = bonus + actualSalary * 0.02
    print('Bonus :',bonus, '  Total Salary :', actualSalary+bonus)
else:
     print('Bonus :',bonus, '  Total Salary :', actualSalary)
