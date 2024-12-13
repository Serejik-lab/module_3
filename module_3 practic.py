def counting_data(data):
    quantity = 0


    for i in data:
        if isinstance(i, int):
            quantity += i
        elif isinstance(i, str):
            quantity += len(i)
        elif isinstance(i, list):
            quantity += counting_data(i)
        elif isinstance(i, dict):
            quantity += counting_data(i.keys())
            quantity += counting_data(i.values())
        elif isinstance(i, tuple):
            quantity += counting_data(i)
        elif isinstance(i, set):
            quantity += counting_data(i)
    return quantity

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = counting_data(data_structure)
print(result)

