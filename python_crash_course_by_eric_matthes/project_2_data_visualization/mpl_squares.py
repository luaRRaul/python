from math import sqrt

import matplotlib.pyplot as plt


def plot_squares_1(squares: [int]):
    fig, ax = plt.subplots()
    ax.plot(squares)

    plt.show()


def plot_squares_2(squares: [int]):
    # using a style
    plt.style.use('seaborn')

    fig, ax = plt.subplots()
    ax.plot([sqrt(val) for val in squares], squares, linewidth=3)

    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of Value', fontsize=14)

    ax.tick_params(axis='both', labelsize=14)

    plt.show()


def scatter_squares_1():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(2, 4)

    plt.show()


def scatter_squares_2():
    x_values = range(1, 1001)
    y_values = [i ** 2 for i in x_values]
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    # c can also be tuple that represents RGB
    # ax.scatter(x_values, y_values, c='red', s=10)

    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of Value', fontsize=14)

    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.axis([0, 1100, 0, 1_100_000])

    plt.show()
    # to save a plot replace the show() call with a savefig() call
    # OBS: savefig() after show() yields a white image being saved
    plt.savefig('name.png', bbox_inches='tight')
