def numbertest( population ):
    initial_size = population.size
    cur_size = sum( [ len( population.units[ t ] ) for t in range( population.ntypes ) ] )
    assert initial_size == cur_size
