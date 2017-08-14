#%%

print('Hello world')

#%%
x = int(input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('This number is even')

else:
    print('')
    print('This number is odd')
    
print('Done with conditional')

#%%
x = int(input('Enter an integer: '))
if x%2 == 0:
    if x%3 ==0:
        print('')
        print('This number is divisible by 2 and 3')
    else:
        print('')
        print('This number is divisble by 2 and not by 3')

elif x%3 == 0:
    print('')
    print('This number is divisble by 3 and not 2')
    
print('Done with conditional')

#%%

x = float(input('Enter a number for x: '))
y = float(input('Enter a number for y: '))

if x == y:
    print('x and y are equal')
    if y != 0:
        print('therefore, x/y is ',x/y)
        
elif x < y:
    print('x is lesser')
    
else:
    print('x is greater')
  
    
