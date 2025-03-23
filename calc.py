def add(*nums):
    return sum(nums)


def sub(*nums):
    result = nums[0]
    for num in nums[1:]:
        result -= num
    return result


def multi(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


def divide(*nums):
    try:
        result = nums[0]
        for num in nums[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result /= num
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"
def calculator():
    while True:
        operation = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")

        if operation == "q":
            print("Exiting calculator. Goodbye!")
            break
        try:

            numbers = list(
                map(float, input("enter numbers separated by space:").split()))
            if not numbers:
                raise ValueError("No numbers entered! ")
        except ValueError:
            print("Error: Please enter valid numbers separated by space!")
            continue

        if operation == "+":
            print(f"Result: {add(*numbers)}")
        elif operation == "-":
            print(f"Result: {sub(*numbers)}")
        elif operation == "*":
            print(f"Result: {multi(*numbers)}")
        elif operation == "/":
            print(f"Result: {divide(*numbers)}")
        else:
            print("Invalid operation! Please enter +, -, *, /, or 'q'.")


calculator()
