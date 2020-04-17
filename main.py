from animation import simulate
from population import population

import sys

keys = [ 'susceptible', 'infected', 'radius', 'p_infect', 'p_recover', 'p_death', 'poi_x', 'poi_y', 'tests' ]

def main( filename = sys.argv[ 1 ] ):
    with open( filename,"r") as f:
        parameters = {}
        for line in f:
            key_value = line.split("=")
            key_value[ 1 ] = key_value[ 1 ][ :-1 ]
            parameters[ key_value[ 0 ] ] = key_value[ 1 ]

        for v in range(6):
            if keys[ v ] not in parameters.keys():
                print("%s: Not Found in File" % keys[ v ] )
                return
        N = [ int( parameters[ keys[ t ] ] ) for t in range( 2 ) ]
        radius = float( parameters[ keys[ 2 ] ] )
        probs = [ float( parameters[ keys[ t ] ] ) for t in range( 3, 6 ) ]
        poi, tests = None, None
        if keys[ 6 ] in parameters.keys() and keys[ 7 ] in parameters.keys():
            poi = [ float( parameters[ keys[ 6 ] ] ), float( parameters[ keys[ 7 ] ] ) ]
        if keys[ 8 ] in parameters.keys():
            tests = int( parameters[ keys[ 8 ] ] )
        sample_population = population( N=N, radius=radius, prob=tuple( probs ), poi=poi, tests=tests )
        simulate( sample_population )

if __name__ == "__main__":
    main()
