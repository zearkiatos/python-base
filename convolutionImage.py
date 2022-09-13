def convolution_image(image: list, mask: list) -> list:
    height = len(image)
    width = len(image[0])

    mask_size = len(mask)
    div = int(mask_size/2)

    new_image = image.copy()

    for i in range(height):
        for j in range(width):
            color_sum = [0.0, 0.0, 0.0]
            sum_coef_mask = 0.0
            x = 0
            for row in range(i-div, i+div+1):
                y = 0
                for column in range(j-div, j+div+1):
                    if row >= 0 and row < height and column >= 0 and column < height:
                        color_sum[0] += (mask[x][y] * image[row][column][0])
                        color_sum[1] += (mask[x][y] * image[row][column][1])
                        color_sum[2] += (mask[x][y] * image[row][column][2])
                        sum_coef_mask += mask[x][y]
                    y += 1
                x += 1
            if sum_coef_mask != 0:
                new_red = color_sum[0] / sum_coef_mask
                new_green = color_sum[1] / sum_coef_mask
                new_blue = color_sum[2] / sum_coef_mask
            else:
                new_red = color_sum[0]
                new_green = color_sum[1]
                new_blue = color_sum[2]

            new_pixel = (new_red, new_green, new_blue)
            new_image[i][j] = new_pixel

    return new_image
