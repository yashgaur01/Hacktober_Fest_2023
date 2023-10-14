# Creating an empty hashmap (dictionary)
hashmap = {}

# Adding key-value pairs to the hashmap
hashmap['key1'] = 'value1'
hashmap['key2'] = 'value2'
hashmap['key3'] = 'value3'

# Accessing values using keys
print("Value associated with 'key1':", hashmap['key1'])
print("Value associated with 'key2':", hashmap['key2'])
print("Value associated with 'key3':", hashmap['key3'])

# Checking if a key is present in the hashmap
key_to_check = 'key2'
if key_to_check in hashmap:
    print(f"'{key_to_check}' is present in the hashmap. Its value is:", hashmap[key_to_check])
else:
    print(f"'{key_to_check}' is not present in the hashmap.")

# Removing a key-value pair from the hashmap
key_to_remove = 'key1'
if key_to_remove in hashmap:
    del hashmap[key_to_remove]
    print(f"'{key_to_remove}' has been removed from the hashmap.")
else:
    print(f"'{key_to_remove}' is not present in the hashmap.")

# Iterating over the keys in the hashmap
print("Keys in the hashmap:")
for key in hashmap:
    print(key)

# Iterating over the values in the hashmap
print("Values in the hashmap:")
for value in hashmap.values():
    print(value)
