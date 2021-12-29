import matplotlib.pyplot as plt
# import mpl_squares
from random_walk import RandomWalk


def test_random_walk():
    rw = RandomWalk()
    rw.walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c=range(len(rw.x_values)), cmap=plt.cm.Blues, edgecolor='none', s=10)
    ax.scatter(0, 0, c='green', edgecolor='none', s=20)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=20)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


if __name__ == '__main__':
    # squares = [i ** 2 for i in range(1, 6)]
    # mpl_squares.plot_squares_1(squares)
    # mpl_squares.plot_squares_2(squares)
    # mpl_squares.scatter_squares_1()
    # mpl_squares.scatter_squares_2()
    test_random_walk()
