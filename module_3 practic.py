def counting_data(data):
    quantity = 0


    for i in data:
        if isinstance(i, int):
            quantity += 1
    return quantity
counting_data([1,12,3])
