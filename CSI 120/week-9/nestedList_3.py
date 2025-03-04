#create nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# how we can display the entire nested list

print("nested list:")
print(nested_list)
# display each inner list separately
print("\nInner_list:") 
for inner_list in nested_list:
    print(inner_list)

