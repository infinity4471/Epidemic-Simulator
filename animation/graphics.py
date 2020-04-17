import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .graph_data import COLORS, COLOR_DOTS, POI_SIDE, BAR_TAGS, POINT_RADIUS, dt
from .quarantine import make_quarantine

def make_plots( population, FIG_SIZE = 15 ):
    fig, ax = plt.subplots( 2, figsize = ( 2*FIG_SIZE, FIG_SIZE + 3 ) )
    fig.canvas.set_window_title('Epidemic Simulator - Watch People Die!')
    ax[ 0 ].set_title("Real Time Simulation")
    ax[ 0 ].set_xticks([])
    ax[ 0 ].set_yticks([])
    ax[ 0 ].set_xlim( -POINT_RADIUS, population.RANGE_X + POINT_RADIUS )
    ax[ 0 ].set_ylim( -POINT_RADIUS, population.RANGE_Y + POINT_RADIUS )
    ax[ 1 ].set_title("Number of units over time per category")
    return fig, ax

def init_animation( population ):
    lines, point_data = [], []
    plt.style.use('dark_background')
    fig, ax = make_plots( population, POINT_RADIUS )
    if population.poi:
        rect = Rectangle( ( population.poi[ 0 ] - float( POI_SIDE / 2 ), \
                population.poi[ 1 ] - float( POI_SIDE / 2 ) ), POI_SIDE, POI_SIDE )
        ax[ 0 ].add_patch( rect )
    if population.test_mode == True:
        quarantine, side1, side2 = make_quarantine( population.RANGE_X, population.RANGE_Y )
        rect = Rectangle( (  quarantine[ 0 ] + POINT_RADIUS, -POINT_RADIUS ), side1, side2, fill = False )
        ax[ 0 ].add_patch( rect )
    stats = [ population.get_stats() ]
    for t in range( population.ntypes ):
        lines.extend( [ [], [] ] )
        xdata, ydata = [], []
        for unit in population.units[ t ]:
            xdata.append( unit.x )
            ydata.append( unit.y )
        point_data.extend( [ xdata, ydata, COLOR_DOTS[ t ] ] )
    lines[ population.ntypes: ] = ax[ 0 ].plot( *point_data )
    return fig, lines


def update_animation( population, lines, _, time_frame = 3 ):
    plot_data = []
    left_limit, right_limit = 0, 0
    if population.is_over():
        plt.close()
        return
    np_stats = np.array( population.stats )
    population.move()
    for i in range( population.ntypes ):
        ydata = np_stats[ :, i ]
        initial_len = len( ydata )
        elements = int( time_frame / dt )
        if elements <= initial_len:
            ydata = ydata[ -elements: ]
        xdata = list( np.linspace( max( initial_len * dt - time_frame, 0 ), initial_len * dt, len( ydata ) ) )
        plot_data.extend( [ xdata, ydata, COLORS[ i ] ] )
        left_limit, right_limit = xdata[ 0 ], xdata[ -1 ]

    if left_limit != right_limit:
        plt.xlim( left = left_limit )
        plt.xlim( right = right_limit )
    lines[ 0:population.ntypes ] = plt.plot( *plot_data )
    plt.legend( lines[ 0:population.ntypes ], BAR_TAGS[ 0:population.ntypes ], bbox_to_anchor=(0.5, -0.1), \
                fancybox=True, shadow=True, loc='upper center', ncol = population.ntypes )
    for t in range( population.ntypes ):
        xdata, ydata = [], []
        for unit in population.units[ t ]:
            xdata.append( unit.x )
            ydata.append( unit.y )
        lines[ population.ntypes + t ].set_data( xdata, ydata )
    return lines
