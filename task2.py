import random

#task 2

def get_numbers_ticket(min: int, max: int, quantity: int):
    # validation
    if not isinstance(max, int) or not isinstance(min, int) or not isinstance(quantity, int):
        raise ValueError("All params mus be integer.")
    if min > max or min < 0 or max < 0:
        raise ValueError(f"Invalid min or max param(s). min: {min}, max: {max}")

    if quantity <= 0:
        raise ValueError(f"Param quantity must be greater than 0. quantity: {quantity}")

    if (max - min) + 1 < quantity:
        raise ValueError("quantity must be less than max-min or equal to max-min.")
    # end validation

    numbers = list(range(min, max+1))
    result = random.sample(numbers, k=quantity)

    return sorted(result)

# print(get_numbers_ticket(1, 10, 3))