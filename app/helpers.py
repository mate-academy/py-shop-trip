import json
import math

def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)
