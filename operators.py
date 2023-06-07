# line comment

# variables
a = int(input('Tip first value \n'))
b = int(input('Tip second value \n'))

# calculations
soma = a + b
sub = a - b
mult = a * b
div = a / b
resto = a % b

# printing values
print(soma, sub, mult, div, resto)
print('convert and rounded division = ', int(div))
print('sum = ' + str(soma))  # str convert to string
print('sum = {} '.format(soma, mult))  # format
print('sum = {ss} and multiplication = {mm} '.format(mm=mult, ss=soma))  # format with alias
print(type(soma))  # show var type
print()
result = ('sum = {ss}.'
          '\nmultiplication = {mm}.'
          '\ndivision = {dd}.'
          .format(mm=mult,
                  ss=soma,
                  dd=div))  # \n start printing in a new line
print(result)
