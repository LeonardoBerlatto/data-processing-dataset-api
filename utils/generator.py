import random


def generate_new_id():
    part1 = random.randint(100, 999)
    part2 = random.randint(10, 99)
    part3 = random.randint(1000, 9999)
    return f"{part1}-{part2}-{part3}"

