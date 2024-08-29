# Declare List for access data element
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Access element by index
name = list_data[0]
print(name)

# Access element by negative index
last_item = list_data[-1]
print(last_item)

# Check list value is exist on it
if "Bangladesh" in list_data:
    print("Yes key exist")
else:
    print("Key not exist")

# Declare List for access data element
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Print each element of list by loop
for item in list_data:
    print("Item : " + str(item))

# List add item using append function
list_data.append("I have a child as well")
print(list_data)

# Update list item using index
list_data[0] = "Mia Bhai"
print(list_data)


# Remove List Item using name
list_data.remove("Bangladesh")
print(list_data)