import numpy as np

import contextlib
with contextlib.redirect_stdout(None):
    import pygame

BALL_RADIUS = 15   # size of player balls


class Ball(object):
    """
    Player ball in the Duet game.
    """

    def __init__(self, x, y, theta, r, vel):
        """
        Creates a player ball with specified position and velocity.
        """

        self.x = x
        self.y = y
        self.theta = theta

        self.xc = (self.x - r) if self.theta == 0 else (self.x + r)
        self.yc = y

        self.ang_vel = vel
        self.radius = r

    def position(self):
        """
        Returns current position of the ball.
        """
        return (self.x, self.y)

    def spin_left(self):
        """
        Spins the ball counter-clockwise.
        """
        self.theta -= self.ang_vel
        self.theta = self.theta % (2*np.pi)
        self.theta = max(2*np.pi + self.theta, self.theta)
        self.x = self.xc + int(self.radius*np.cos(self.theta))
        self.y = self.yc + int(self.radius*np.sin(self.theta))

    def spin_right(self):
        """
        Spins the ball clockwise.
        """
        self.theta += self.ang_vel
        self.theta = self.theta % (2*np.pi)
        self.theta = max(2*np.pi + self.theta, self.theta)
        self.x = self.xc + int(self.radius*np.cos(self.theta))
        self.y = self.yc + int(self.radius*np.sin(self.theta))

    def collided_with(self, obstacle):
        """
        Checks if the ball has collided with obstacle.
        """
        return self.rect.colliderect(obstacle.get_rect())

    def draw(self, screen, color):
        """
        Draws the ball.
        """
        self.rect = pygame.draw.circle(screen, color,
                                       self.position(), BALL_RADIUS)
