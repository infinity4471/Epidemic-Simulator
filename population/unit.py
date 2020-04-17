from math import sqrt
from random import randrange, random
import numpy as np
from numpy.random import normal

from .unit_data import POI_SIDE, POINT_RADIUS
from .quarantine import make_quarantine

CHOICE_THRES = 0.01

class unit:
    def __init__( self, x, y, t = 0, r = 0, prob = ( 0, 0, 0 ), poi = [], test_mode = False ):
        #prob[ 0 ] -> probability of infection
        #prob[ 1 ] -> probability of recovery
        #prob[ 2 ] -> probability of death
        self.x, self.y, self.type, self.radius = x, y, t, r
        self.p_transmit, self.p_recover, self.p_death = prob
        self.choice = False
        self.poi = poi

    def in_quarantine( self, RANGE_X, RANGE_Y ):
        quarantine,_,_ = make_quarantine( RANGE_X, RANGE_Y )
        if self.x >= quarantine[ 0 ] - POINT_RADIUS and self.y <= quarantine[ 1 ] + POINT_RADIUS:
            return True
        return False

    def move_poi( self, poi, RANGE_X, RANGE_Y ):
        if self.dist( unit( self.poi[ 0 ], self.poi[ 1 ] ) ) < POI_SIDE / 2.0:
            if self.poi != poi:
                self.poi = poi
            else:
                self.poi = [ random() * RANGE_X, random() * RANGE_Y ]
                self.choice = False
        else:
            direction = randrange( 2 )
            if direction == 0:
                self.x += np.sign( self.poi[ 0 ] - self.x ) * abs( normal( 0, 1 ) )
            else:
                self.y += np.sign( self.poi[ 1 ] - self.y ) * abs( normal( 0, 1 ) )

    def random_walk( self, MIN_X, MAX_X, MIN_Y, MAX_Y ):
        self.x += normal( 0, 1 )
        self.y += normal( 0, 1 )
        self.x = min( MAX_X, self.x )
        self.x = max( MIN_X, self.x )
        self.y = min( MAX_Y, self.y )
        self.y = max( MIN_Y, self.y )

    def move_quarantine( self, RANGE_X, RANGE_Y ):
        upper_left, _, _ = make_quarantine( RANGE_X, RANGE_Y )
        if not self.in_quarantine( RANGE_X, RANGE_Y ):
            self.random_walk( upper_left[ 0 ], RANGE_X, 0, upper_left[ 1 ] )
        else:
            self.x, self.y = ( upper_left[ 0 ] + RANGE_X ) / 2.0, ( upper_left[ 1 ] ) / 2.0

    def move( self, RANGE_X, RANGE_Y, poi = [] ):
        if self.type == 'Q':
            self.move_quarantine( RANGE_X, RANGE_Y )
        choice = random()
        if choice < CHOICE_THRES:
            self.choice = True
        if poi and self.choice: #if point of interest move
            self.move_poi( poi, RANGE_X, RANGE_Y )
        else: #random walk if no point of interest
            self.random_walk( 0, RANGE_X, 0, RANGE_Y )
        if self.type != 'Q':
            upper_left,_,_ = make_quarantine( RANGE_X, RANGE_Y )
            if abs( upper_left[ 0 ] - self.x ) < POINT_RADIUS:
                self.x = upper_left[ 0 ] - 2 * POINT_RADIUS
            if abs( upper_left[ 1 ] - self.y ) < POINT_RADIUS:
                self.y = upper_left[ 1 ] + 2 * POINT_RADIUS

    def dist( self, other_p ):
        return sqrt( ( other_p.x - self.x ) ** 2 + ( other_p.y - self.y ) ** 2 )

    def change_type( self, new_type ):
        self.type = new_type
