#Input the size of the array
size = int(input("Enter the size of the array: "))

#Input the elements of the array
elements = list(map(int, input("Enter the elements separated by space: ").split()))

# Check if the number of elements
if len(elements) != size:
    print(f"Error: Expected {size} elements, but got {len(elements)}.")
else:
#Display the cube of each element
    for element in elements:
        print(element ** 3)
