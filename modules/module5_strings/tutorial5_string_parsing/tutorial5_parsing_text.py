# Intro to Programming with Python
# Tutorial 5 - Parsing Text
# Tristan Hill - June 12, 2023

raw_data='''Name, ID, Price, Quantity
Motor, 103, $357.45, 2
Wheel, 78, $48.23, 4
LiDAR, 1089, $2500.00, 1
Computer, 99, $725.78, 1
Battery, 401, $501.01, 2
Battery Controller, 700, $58.99, 1'''

print(type(raw_data))
print(raw_data)
# split into rows with newline ('\n')
rows_data=raw_data.split('\n')
print(rows_data)
print('The top row is:', rows_data[0])
print('The second row is:', rows_data[1])
print('The items in the second row are', rows_data[1].split(','))
print('The third item in the third row is', rows_data[2].split(',')[2])
