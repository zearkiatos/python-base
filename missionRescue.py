def missionRescue(loadSaber: int, shildEnergy: int) -> None:
    if not ((loadSaber) >= 90 and (shildEnergy >= 100)):
        print("Your attack don't have effect, the dragon 🐉 the dragon will burn 🔥 you until left you crush")
    else:
        print(
            "You have finall defend the dragon, you can rescue to the beautiful pricess 👸")


def missionRescue2(loadSaber: int, shildEnergy: int) -> None:
    if ((loadSaber) < 90 or (shildEnergy < 100)):
        print("Your attack don't have effect, the dragon 🐉 the dragon will burn 🔥 you until left you crush")
    else:
        print(
            "You have finall defend the dragon, you can rescue to the beautiful pricess 👸")


def missionRescue3(loadSaber: int, shildEnergy: int) -> None:
    if ((loadSaber) >= 90 or (shildEnergy >= 100)):
        print(
            "You have finall defend the dragon, you can rescue to the beautiful pricess 👸")
    else:
        print("Your attack don't have effect, the dragon 🐉 the dragon will burn 🔥 you until left you crush")


missionRescue(80, 120)

missionRescue(200, 50)

missionRescue(100, 120)

missionRescue2(80, 120)

missionRescue3(80, 120)
