#Input the value the user want
height = int(input("Enter the height of the triangle: "))

#Loop fot the inverted triangle
for i in range(height, 0, -1):
    print('*' * i)