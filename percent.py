# number = float(input("Enter number: "))
# percentage = float(input("Enter percente: "))
# result = (number * percentage) / 100
#
# print(f"{percentage}% from  {number} = {result}")


def calculate_percentage(number: float, percentage: float) -> float:
    return (number * percentage) / 100

if __name__ == "__main__":
    number = float(input("Enter number: "))
    percentage = float(input("Enter percentage: "))
    result = calculate_percentage(number, percentage)
    print(f"{percentage}% from {number} = {result}")
