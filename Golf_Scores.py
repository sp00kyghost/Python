#Lab from python class, to help understand if / elif statements.

#accept user input
par_int = int(input())
strokes = int(input())

#if par IS NOT 3,4,5 print error
if par_int != 3 and par_int != 4 and par_int != 5:
    print('Error')
else: #else print score.
    if strokes == par_int - 2:
        print(f'Eagle')
    elif strokes == par_int - 1:
        print(f'Birdie')
    elif strokes == par_int:
        print(f'Par')
    elif strokes == par_int + 1:
        print(f'Bogey')