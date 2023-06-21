# intro to programming with Python - GSET 2023
# tutorial6 - Conditionals - Triangles
# Tristan Hill - June 20, 2023 - example code 

# prompt the user for input
data=input('''Type the values for the vertices of a triangle
The following format is required. x1, y1, x2, y2, x3, y3:''')

# get values from user input, store as separate lists 
xvalues=[float(data.split(',')[0]), float(data.split(',')[2]), float(data.split(',')[4])]
yvalues=[float(data.split(',')[1]), float(data.split(',')[3]), float(data.split(',')[5])]
print('xvalues:',xvalues)
print('yvalues:',yvalues)