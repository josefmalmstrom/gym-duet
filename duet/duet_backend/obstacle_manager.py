import random
from enum import Enum

import contextlib
with contextlib.redirect_stdout(None):
    import pygame

BOARD_HEIGHT = 960
BOARD_WIDTH = 540

OBS_HEIGHT = 50
OBS_VEL = 2

SPAWN_HEIGHT = 0

# Types of obstacles
# (min_left, max_left, min_right, max_right, min_height, max_height)
# MID_COORDS = (195, 235, 308, 345, 70, 70)
MID_COORDS = (215, 215, 325, 325, 70, 70)
LEFT_COORDS = (35, 35, 270, 270, 70, 70)
RIGHT_COORDS = (270, 270, 505, 505, 70, 70)
DOUBLE_COORDS = (30, 30, 190, 190, 70, 70)  # left coords


class ObstacleManager(object):
    """
    Generates and manages obstacles for the Duet game.
    """

    def __init__(self):

        random.seed(221)  # for deterministic sequence

        self.obstacles = []

    def __iter__(self):

        return iter(self.obstacles)

    def new_obstacle_set(self):
        """
        Generates a new obstacle set.
        """

        obs_type = self.random_obstacle_type()

        if obs_type == ObstacleType.MID:
            COORDS = MID_COORDS
        elif obs_type == ObstacleType.LEFT:
            COORDS = LEFT_COORDS
        elif obs_type == ObstacleType.RIGHT:
            COORDS = RIGHT_COORDS
        elif obs_type == ObstacleType.DOUBLE:
            COORDS = DOUBLE_COORDS

        (min_left, max_left, min_right, max_right,
         min_height, max_height) = COORDS

        spawn_x = random.randint(min_left, max_left)
        width = random.randint(min_right, max_right) - spawn_x
        height = random.randint(min_height, max_height)
        spawn_y = SPAWN_HEIGHT - height

        new_obstacle_set = [Obstacle(spawn_x, spawn_y, width, height, obs_type)]

        if obs_type == ObstacleType.DOUBLE:
            spawn_x = BOARD_WIDTH - random.randint(min_left, max_left) - width
            new_obstacle_set.append(Obstacle(spawn_x, spawn_y, width, height, obs_type))

        self.obstacles.append(new_obstacle_set)

    def random_obstacle_type(self):
        """
        Picks a random obstacle type.
        """
        return random.choice(list(ObstacleType))
        # return random.choice([ObstacleType.DOUBLE, ObstacleType.LEFT, ObstacleType.RIGHT])

    def get_obstacles(self):
        """
        Returns the list of obstacle sets.
        """
        return self.obstacles

    def oldest_obstacle_set(self):
        """
        Returns the oldest obstacle set.
        """
        return self.obstacles[0]

    def oldest_out_of_frame(self):
        """
        Checks if the oldest obstacle set has gone out of frame.
        """

        return self.obstacles[0][0].out_of_frame()

    def remove_obstacle_set(self):
        """
        Removes the oldest obstacle set.
        """
        self.obstacles.pop(0)


class ObstacleType(Enum):
    """
    Enum for the different types of obstacles.
    """
    MID = 1
    LEFT = 2
    RIGHT = 3
    DOUBLE = 4


class Obstacle(object):
    """
    An obstacle in the Duet game.
    """

    def __init__(self, x, y, width, height, obs_type):

        self.x = x  # = left
        self.y = y  # = top
        self.width = width
        self.height = height

        self.top = self.y
        self.bottom = self.y - height
        self.left = self.x
        self.right = self.x + width

        self.obs_type = obs_type

    def move(self):
        """
        Moves the obstacle down, towards the player.
        """
        self.y += OBS_VEL
        self.top += OBS_VEL
        self.bottom += OBS_VEL

    def out_of_frame(self):
        """
        Checks if the obstacle has left the game board.
        """
        return (self.top - 5 >= BOARD_HEIGHT)

    def get_rect(self):
        """
        Returns the obstacle as a pygame Rect.
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def x_span(self):
        """
        Returns the interval of x coordinates that
        the obstacle spans.
        """
        return (self.left, self.right)

    def get_top(self):
        """
        Returns y-coordinate of the top of the obstacle.
        """
        return self.top

    def get_bottom(self):
        """
        Returns the y-coordinate of the bottom of the obstacle.
        """
        return self.bottom

    def get_type(self):
        """
        Returns the obstacles type.
        """
        return self.obs_type
