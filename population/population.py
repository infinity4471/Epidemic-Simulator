from random import randrange, random


from .unit import unit
from .population_tests import numbertest

types = [ 'S', 'I', 'R', 'D', 'Q' ]
TEST_RATE = 20

#population holds units list
# units[ 0 ] -> susceptible
# units[ 1 ] -> infected
# units[ 2 ] -> recovered
# units[ 3 ] -> dead
# units[ 4 ] -> ( optional ) tested/quarantined

class population:
    def __init__( self, N, radius, prob, poi = None, tests = None, RANGE_X = 100, RANGE_Y = 100 ):
        self.units = [ [] for _ in range( len( types ) ) ]
        self.ntypes = len( types ) - 1
        self.size = sum( N )
        self.test_mode = False
        if tests > 0:
            self.test_mode = True
            self.ntypes += 1
        self.RANGE_X, self.RANGE_Y = RANGE_X, RANGE_Y
        self.poi, self.tests = poi, tests
        for t in range( len( N ) ):
            for i in range( N[ t ] ):
                x, y = randrange( RANGE_X ), randrange( RANGE_Y )
                test_unit = unit( x, y, t = types[ t ], r = radius, prob = prob, poi = poi, test_mode = self.test_mode )
                if self.test_mode:
                    while test_unit.in_quarantine( RANGE_X, RANGE_Y ):
                        x, y = randrange( RANGE_X ), randrange( RANGE_Y )
                        test_unit = unit( x, y, types[ t ], radius, prob, poi, self.test_mode )
                self.units[ t ].append( test_unit )
        self.stats = [ self.get_stats() ]

    def move( self ):
        if self.is_over():
            return
        if len( self.stats ) % TEST_RATE == 0:
            self.do_test()
        for t in range( self.ntypes ):
            for u in self.units[ t ]:
                if u.type != 'D':
                    u.move( self.RANGE_X, self.RANGE_Y, self.poi )
        self.update_status()
        self.stats.append( self.get_stats() )
        numbertest( self )

    def do_test( self ):
        if self.tests == 0:
            return
        group = randrange( self.ntypes - 1 )
        self.tests -= 1
        if group == 1 and self.units[ 1 ]:
            infected = self.units[ 1 ][ 0 ]
            self.units[ 1 ].remove( infected )
            infected.change_type( 'Q' )
            self.units[ 4 ].append( infected )

    def update_status( self ):
        for infected in ( self.units[ 1 ] + self.units[ 4 ] ):
            choice = random()
            if choice < infected.p_recover:
                infected.change_type( 'R' )
            else:
                choice = random()
                if choice < infected.p_death:
                    infected.change_type( 'D' )

        for infected in self.units[ 1 ]:
            if infected.type == 'R':
                self.units[ 1 ].remove( infected )
                self.units[ 2 ].append( infected )
            elif infected.type == 'D':
                self.units[ 1 ].remove( infected )
                self.units[ 3 ].append( infected )

        for quarantined in self.units[ 4 ]:
            if quarantined.type == 'R':
                self.units[ 4 ].remove( quarantined )
                self.units[ 2 ].append( quarantined )
            elif quarantined.type == 'D':
                self.units[ 4 ].remove( quarantined )
                self.units[ 3 ].append( quarantined )

        for infected in self.units[ 1 ]:
            for susceptible in self.units[ 0 ]:
                if infected.dist( susceptible ) < infected.radius:
                    choice = random()
                    if choice < infected.p_transmit:
                        susceptible.change_type( 'I' )

        for susceptible in self.units[ 0 ]:
            if susceptible.type == 'I':
                self.units[ 0 ].remove( susceptible )
                self.units[ 1 ].append( susceptible )

    def is_over( self ):
        if self.ntypes < 5:
            return not self.units[ 1 ]
        else:
            return not self.units[ 1 ] and not self.units[ 4 ]

    def get_stats( self ):
        return [ len( self.units[ t ] ) for t in range( self.ntypes ) ]
