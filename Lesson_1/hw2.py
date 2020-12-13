first_coef = float(input ('enter the first coefficient of the quadratic equation that is not equal to 0,\n a = '))
second_coef = float(input ('enter the second coefficient,\n b = '))
third_coef = float(input ('enter the third coefficient,\n c = '))

D = second_coef**2 - 4*first_coef*third_coef
x1 = format((-second_coef + D**0.5)/2*first_coef, '.2f')
x2 = format((-second_coef - D**0.5)/2*first_coef, '.2f')

print(f'x1 = {x1}; x2 = {x2}')

