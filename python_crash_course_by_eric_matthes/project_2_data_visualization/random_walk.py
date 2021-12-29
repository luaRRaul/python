from random import choice


class RandomWalk:

    def __init__(self, nb_points=5000):
        self.nb_points = nb_points

        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        for i in range(self.nb_points):
            x_dir = choice([-1, 1])
            x_dist = choice([j for j in range(5)])

            y_dir = choice([-1, 1])
            y_dist = choice([j for j in range(5)])

            if x_dir * x_dist == 0 and y_dir * y_dist == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_dir * x_dist)
            self.y_values.append(self.y_values[-1] + y_dir * y_dist)
