def image_binarization(image: list, umbral: float) -> list:
    image_binarizated = []
    for row in range(0, len(image)):
        image_binarizated.append([])
        for column in range(0, len(image[row])):
            red, green, blue = image[row][column]

            average = red + green + blue / 3

            if (average >= umbral):
                image_binarizated[row].append((1, 1, 1))
            
            if (average < umbral):
                image_binarizated[row].append((0, 0, 0))

    return image_binarizated