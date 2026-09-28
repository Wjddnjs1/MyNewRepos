a = [5, 12, 28, 29, 40, 41, 53, 54, 98, 69, 49, 80, 83, 79, 99, 100]
x = input('Input a number: ')
left = 0
right = len(a) - 1

# Find x in the list a
while left <= right:
    middle = (left + right) // 2
  
    if a[middle] == int(x):  # Success
        print('There is {:3} at a[{:2}] in the list.'.format(x, middle))
        break   
    elif a[middle] < int(x):
        left = middle + 1    
    else:
        right = middle - 1

if left > right: 
    print('There is not {:3} in this list.'.format(x))
