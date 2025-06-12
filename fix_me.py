def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total/count
    return average


numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
