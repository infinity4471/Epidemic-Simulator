from animation import simulate
from population import population

N = 0
radius = 0
probs = 0
poi = 0
tests = 0

f = open("parameters.txt","r")
parameters = []
for line in f:
    dummy = line.split("=")
    dummy[1] = dummy[1][0:len(dummy[1])-1]
    parameters.append(dummy[1])
N = [parameters[0],parameters[1]]
N = list(map(int, N))
radius = int(parameters[2])
probs = (float(parameters[3]),float(parameters[4]),float(parameters[5]))
if len(parameters)>7:
    poi = (int(parameters[6]),int(parameters[7]))
if len(parameters)==9:
    tests = int(parameters[8])

simulate( population( N, radius, probs, poi, tests ))
