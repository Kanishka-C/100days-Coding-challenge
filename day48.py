#Array duplicate elements removal
size = int(input('Enter the size of array: '))
arr = []
unique_elements = set()

print('Enter the elements of array:')
for i in range(size):
    element = input()
    if element not in unique_elements:  # Check if the element is already seen
        unique_elements.add(element)   # Mark the element as seen
        arr.append(element)            # Add to the result list

print('Array after removing duplicates:', arr)
