def create_figure(position: tuple, size: tuple) -> dict:
    new_figure = {"position": position, "size": size}

    new_figure["corner"] = (0, 0)
    new_figure["thickness"] = 3
    new_figure["internal_color"] = None
    new_figure["line_color"] = (0, 0, 0)
    new_figure["rotation"] = (0, 0, 0)

    return new_figure


