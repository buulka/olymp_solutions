def sort(number):
    array = [5, 11, 13, 3, 7, 9]
    operation = 0
    array.append(number)

    for i in range(len(array)):
        for k in range(len(array) - i - 1):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                operation += 1
    if operation == 11:
        return array, operation, number


for number in range(10):
    print(sort(number))
