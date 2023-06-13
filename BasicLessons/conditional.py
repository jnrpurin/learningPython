###################################################################
# Practice conditionals 3:
grade1 = int(input('Inform first grade \n'))
grade2 = int(input('Inform second grade \n'))
grade3 = int(input('Inform third grade \n'))
grade4 = int(input('Inform four grade \n'))

avg = grade4 + grade3 + grade2 + grade1 / 4

if grade1 <= 10 and grade2 < 11 and grade3 < 11 and grade4 <= 10:
    print('Final average: {}.'.format(avg))
else:
    print('Incorrect grade informed.')

###################################################################
# Practice conditionals 2:
# n1 = int(input('Inform a value: '))
# n2 = int(input('Inform another value: '))
# remnant1 = n1 % 2
# remnant2 = n2 % 2
#
# if remnant1 == 0 or not remnant2 > 0:
#     print('Numbers are all pairs')
# else:
#     print('The numbers are unpaired')
###################################################################

# Practice conditionals 1:
# first = int(input('Inform first value: '))
# second = int(input('Inform second value: '))
# third = int(input('Inform third value: '))
#
# if first > second and first > third:
#     print('Bigger number is the first one: {f}'.format(f=first))
# elif second > first and second > third:
#     print('The bigger number is the second: {s}'.format(s=second))
# else:
#     print('The bigger number is the third: {t}'.format(t=third))
