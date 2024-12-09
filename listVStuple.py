#list
my_list = [1, 2, 3]
print("Original List:", my_list)

# Modify the list (mutability)
my_list[0] = 10
my_list.append(4)
print("Modified List:", my_list)

# Tuple example
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# Trying to modify the tuple will raise an error (immutability)
my_tuple[0] = 10  # This will raise a TypeError
print("Tuple:", my_tuple)

