def function_with_improved_error_handling(data):
    if isinstance(data, dict):
        try:
            result = data['key']
            return result
        except KeyError:
            return 'Key not found'
    else:
        return 'Input data is not a dictionary' 

# Example usage
data1 = {'key': 'value'}
data2 = {}
data3 = 123

print(function_with_improved_error_handling(data1))  # Output: value
print(function_with_improved_error_handling(data2))  # Output: Key not found
print(function_with_improved_error_handling(data3))  # Output: Input data is not a dictionary