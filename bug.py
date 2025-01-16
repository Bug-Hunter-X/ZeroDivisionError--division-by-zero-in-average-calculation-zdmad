def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with potential error:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#another example of the same error
my_list = [10, 20, 30, 40, 50]
my_list.clear()

average = calculate_average(my_list)
print(f"The average is: {average}")