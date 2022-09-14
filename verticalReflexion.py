def image_reflexion(image: list) -> list:
    image_reflexioned = []
    for row in range(0, len(image)):
        image_reflexioned[row] = []
        column = len(image[row])
        while(column > 0):
            image_reflexioned[row].append(image[row][column])
            column -= 1

    return image_reflexion
