import numpy as np
import matplotlib.pyplot as plt

from .graph_data import COLORS, COLORS_TUPLE, BAR_TAGS, BAR_TYPES, dt

def make_plots( FIG_SIZE = 5 ):
    fig, ax = plt.subplots( 2, figsize = ( FIG_SIZE, FIG_SIZE ) )
    fig.canvas.set_window_title('Epidemic Simulator - Statistical Results')
    ax[ 0 ].set_title("Number of units per category over time")
    return fig, ax

def plot_stats( population ):
    fig, ax = make_plots()
    plot_data = []
    np_stats = np.array( population.stats )
    for i in range( population.ntypes ):
        plot_data.append( list( np.linspace( 0, len( population.stats ) * dt, len( population.stats ) ) ) )
        plot_data.append( np_stats[ :, i ] )
        plot_data.append( COLORS[ i ] )

    number_bars = population.ntypes
    ax[ 0 ].plot( *plot_data )
    bar_data = np.array( [ len( population.units[ t ] ) for t in range( population.ntypes ) ] )
    plt.bar( np.arange( number_bars ), bar_data[ 0:number_bars ], color = COLORS_TUPLE[ 0:number_bars ] )
    plt.xticks( np.arange( number_bars ), BAR_TAGS[ 0:number_bars ] )
    plt.show()
