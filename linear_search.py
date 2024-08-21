def linear_search(array, target):
    # Iterate over each element in the array by index
    for i in range(len(array)):
        # Check if the current element is equal to the target value
        if array[i] == target:
            # If found, return the index of the target value
            return i
    
    # If the target value is not found in the array, return -1
    return -1  

# Example usage of the linear_search function
index = linear_search([10, 20, 30, 40, 50], 30)

print(index)  
# Output should be 2 (since 30 is at index 2 in the list)
