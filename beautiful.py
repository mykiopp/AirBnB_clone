def calculate_square_area(side_length):
    """
    Calculate the area of a square given the side length.
    """
    area = side_length ** 2
    return area

side_length = 5
square_area = calculate_square_area(side_length)
print(f"The area of a square with side length {side_length} is {square_area}")
