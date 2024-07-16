def calculate_structure_sum(data):
    total_sum = 0
    total_len = 0

    if isinstance(data, int):
        total_sum += data
    elif isinstance(data, str):
        total_len += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            sub_sum, sub_len = calculate_structure_sum(item)
            total_sum += sub_sum
            total_len += sub_len
    elif isinstance(data, dict):
        for key, value in data.items():
            key_sum, key_len = calculate_structure_sum(key)
            value_sum, value_len = calculate_structure_sum(value)
            total_sum += key_sum + value_sum
            total_len += key_len + value_len

    return total_sum, total_len


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "hello",
    ((), [{(2, 'urban', ('urban2', 35))}])
]

result_sum, result_len = calculate_structure_sum(data_structure)
result = result_sum + result_len
print(result)