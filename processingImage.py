def filter_color_applied(image: list, conserve: tuple) -> list:
    new_image = []
    height = len(image)
    width = len(image['0'])

    for i in range(height):
        new_row = []
        for j in range(width):
            r, g, b = image[i][j]
            temp = [r, g, b]
            for k in range(3):
                if not conserve[k]:
                    temp[k] = 0.0
            new_pixel = (temp[0], temp[1], temp[2])
            new_row.append(new_pixel)
        new_image.append(new_row)
    
    return new_image
