#Star printing for visual representation

num_rows = int(input('Enter Number of Rows: '))
num_cols = int(input('Enter number of Columns: '))
i=0

print()

while i < num_rows:
    j = 0
    i+=1
    while j < num_cols:
        j+=1
        print('*', end=' ')
    print()