def function_with_uncommon_error(data):
    try:
        result = data['key']  # Accessing a key that might not exist
        return result
    except KeyError:
        return 'Key not found'

# Example usage
data1 = {'key': 'value'}
data2 = {}

print(function_with_uncommon_error(data1))  # Output: value
print(function_with_uncommon_error(data2))  # Output: Key not found

#Uncommon Error: The KeyError exception is often caught, but neglecting the possibility of other exceptions
# For example: if data was not a dictionary