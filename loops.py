###################################################################
# Practice loops 2:

error_message = str('Invalid grade. Inform another grade less then 10: ')
grade1 = int(input('Inform first grade (less then 10)\n'))
while grade1 > 10:
    grade1 = int(input(error_message))

grade2 = int(input('Inform second grade (less then 10)\n'))
while grade2 > 10:
    grade2 = int(input(error_message))

grade3 = int(input('Inform third grade (less then 10)\n'))
while grade3 > 10:
    grade3 = int(input(error_message))

grade4 = int(input('Inform four grade (less then 10)\n'))
while grade4 > 10:
    grade4 = int(input(error_message))

avg = (grade4 + grade3 + grade2 + grade1) / 4

print('Final average: {}.'.format(avg))


###################################################################
# Practice loops 1:
# n1 = int(input('Say a number: \n0 (zero) to exit \n'))
# while n1 != 0:
#     print()
#
#     for n in range(n1+1):
#         div = 0
#         for i in range(1, n+1):
#             resto = n % i
#             if resto == 0:
#                 div += 1
#
#         if div == 2:
#             print('{p} prime'.format(p=n))
#         else:
#             print('{i} not prime'.format(i=n))
#
#     print()
#     n1 = int(input('Say another number: \n0 to exit \n'))
###################################################################
