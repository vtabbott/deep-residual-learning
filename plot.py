"""Visualizes training and evaluation metrics."""

import os
import numpy as np
from matplotlib import pyplot as plt


def plot(graph, info):
    for path, label, color in info:
        test_errors = np.load(os.path.join(path, 'test_errors.npy'))
        train_errors = np.load(os.path.join(path, 'train_errors.npy'))
        graph.plot(test_errors[0], test_errors[1] * 100, label=label, color=color)
        graph.plot(train_errors[0], train_errors[1] * 100, color=color, alpha=0.1)
    graph.legend()


def format_plot(graph):
    graph.set_ylabel('Error (%)')
    graph.set_ylim(0, 30)
    graph.set_xlabel('Epoch')
    graph.set_xlim(0, 160)
    graph.spines['top'].set_visible(False)
    graph.spines['right'].set_visible(False)


def plain_vs_residual(show=False):
    fig, ax = plt.subplots(1, 1)
    info = (
        ('models/CifarResNet-20-P/03_06_2022/19_13_20',     'Plain-20', 'orange'),
        ('models/CifarResNet-20-R-A/03_06_2022/20_20_51',   'Option A', 'purple'),
        ('models/CifarResNet-20-R-B/03_07_2022/19_58_56',   'Option B', 'violet')
    )
    format_plot(ax)
    plot(plt, info)
    plt.tight_layout()
    plt.savefig('plain_vs_residual')
    if show:
        plt.show()


def side_by_side(show=False):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    for p in axs:
        format_plot(p)
    plain, residual = axs

    sizes = (20, 32, 44, 56)
    colors = ('orange', 'blue', 'green', 'red')
    plain_paths = (
        'models/CifarResNet-20-P/03_06_2022/19_13_20',
        'models/CifarResNet-32-P/03_06_2022/22_03_09',
        'models/CifarResNet-44-P/03_07_2022/17_48_36'
    )
    plot(plain, zip(plain_paths, [f'Plain-{x}' for x in sizes], colors))

    residual_paths = (
        'models/CifarResNet-20-R-A/03_06_2022/20_20_51',
        'models/CifarResNet-32-R-A/03_06_2022/23_27_14',
        'models/CifarResNet-44-R-A/03_07_2022/21_10_40'
    )
    plot(residual, zip(residual_paths, [f'Residual-{x}' for x in sizes], colors))

    plt.tight_layout()
    plt.savefig('side_by_side')
    if show:
        plt.show()


if __name__ == '__main__':
    s = False
    plain_vs_residual(show=s)
    side_by_side(show=s)