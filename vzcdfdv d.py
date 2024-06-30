def calculate_structure_sum(*args):
    total_sum = 0
    total_len = 0

    for item in args:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_len += len(item)
        elif isinstance(item, tuple) or isinstance(item, list):
            args_sum, args_len = calculate_structure_sum(*item)
            total_sum += args_sum
            total_len += args_len
        elif isinstance(item, dict):
            args_sum, args_len = calculate_structure_sum(*item.values())
            total_sum += args_sum
            total_len += args_len

    return total_sum, total_len

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result_sum, result_len = calculate_structure_sum(*data_structure)
result = result_sum + result_len
print(result)
