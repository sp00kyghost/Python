#String / List Basics

my_str = 'This is a string.\n'
print(my_str)

str_two = 'You can also append strings by using the "+" symbol. "full_name = fname + lname" results in my name below.\n'
print(str_two)

fname = 'Seth ' #whitespace included to add a space effect.
lname = 'Prevott'

full_name = fname + lname

print(full_name, end='\n')

my_list = ['this', 'is', 'a', 'list']
print(my_list, end='\n')

list_two = [420, 'words'] #this list shows you can mix elements.
print(list_two, end='\n')

my_list.pop(2) #pop removes an element from index | .remove('a') will remove the first element of the value inside brackets.
print(my_list, end='\n')
