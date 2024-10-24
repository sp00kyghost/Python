#binary / reverse string test

def binary(x):
    #store binary output in a string for easy reversal
    output_string = '' #empty string for storing
    
    while x > 0:
        output_string += str(x % 2)
        x = x // 2
    return output_string

#function to reverse string
def reverse_str(output):
    return output[::-1] #this will reverse our string starting with the end of output

x = int(input(f'Please enter an integer! ->: '))

binary_output = binary(x)

print(f'You entered \'{x}\'... the binary code is: {binary_output} but is reversed.')

str_output = reverse_str(binary_output)

print(f'The proper binary string for \'{x}\' is {str_output}')