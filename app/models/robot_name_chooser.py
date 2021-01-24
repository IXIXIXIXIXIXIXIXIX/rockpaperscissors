import random
from app.data.robot_names import robot_names

def robot_name_chooser():
    return random.choice(robot_names)