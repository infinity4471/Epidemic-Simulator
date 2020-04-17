import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functools import partial

from .graphics import init_animation, update_animation
from .plotter import plot_stats

def render( fig, ln, population ):
    ani = FuncAnimation( fig, partial( update_animation, population, ln ) )
    plt.show()

def simulate( population ):
    fig, ln = init_animation( population )
    render( fig, ln, population )
    plot_stats( population )
