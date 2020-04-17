def make_quarantine( RANGE_X, RANGE_Y ):
    quarantine_side1, quarantine_side2 = RANGE_X / 5.0, RANGE_Y / 5.0
    upper_left = [ RANGE_X - quarantine_side1, quarantine_side2 ]
    return upper_left, quarantine_side1, quarantine_side2
