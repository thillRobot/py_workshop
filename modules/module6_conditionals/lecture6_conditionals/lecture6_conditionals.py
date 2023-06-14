# lecture6_conditionals
# coefficients of quadratic equation

coefs=input('Type a,b,c and press enter: ') # get input string from user
a=float(coefs.split(',')[0])                # split items by commas 
b=float(coefs.split(',')[1])                # access with index
c=float(coefs.split(',')[2])                # convert string to float  

x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)           # calculate root values
x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
                         
print('The first root is:', x1)
print('The second root is:', x2)