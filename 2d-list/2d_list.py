# Example of a 2D list

my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Using nested loops to get values from a 2D list

# The first loop, loops through the main list and prints its values
for lists in my_list:
    print(lists)
    
    # The 2nd loop, loops through the inside lists and prints its value
    for row in lists:
        print(row)