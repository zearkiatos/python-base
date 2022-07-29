def areCollinearPoints(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
    earring1 = earring(x1, x2, y1, y2)
    earring2 = earring(x2, x3, y2, y3)
    return earring1 == earring2


def earring(x1: int, x2: int, y1: int, y2: int) -> float:
    return (y2-y1)/(x2-x1)


print(areCollinearPoints(-5, 3, -1, -3, 1, -6))

print(areCollinearPoints(-5, 3, -1, -3, 1, 6))
