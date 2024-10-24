#func test

#Function to test python tuple unpacking.

def tu_test(a,b,x,y):
    a,b,x,y = b,a,y,x
    
    return a,b,x,y

val1 = int(input(f'Please input value 1: '))
val2 = int(input(f'Please input value 2: '))
val3 = int(input(f'Please input value 3: '))
val4 = int(input(f'Please input value 4: '))

print(f'The numbers you entered are {val1}, {val2}, {val3}, and {val4}.')

output = tu_test(val1,val2,val3,val4)

print(f'We can mix the values of a, b, x, y (or the 4 values you entered) and print them as b, a, y, x ')
print(f'After using the function \'tu_test\' the swapped output is: {output}.')

