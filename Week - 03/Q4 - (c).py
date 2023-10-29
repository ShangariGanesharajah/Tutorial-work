m = int(input("Enter your exam mark: "))

if m < 0 or m > 100:
    print('Invalid mark')
elif m >= 70:
    print('Exceptional result!')
elif m >= 40:
    print('Satisfactory result!')
else:
    print('You have failed.')
