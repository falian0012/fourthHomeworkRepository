def func(number):
    count = 0
    summary = 1
    while count < number:
        count += 1
        summary *= count
        yield summary

temp_value = 1
for item in func(5):
    print(f'{temp_value} : {item}')
    temp_value += 1
