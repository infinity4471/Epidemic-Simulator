# Epidemic-Simulator
An Epidemic Simulator with real time charts and statistics using a modified SIR Model.

Made by:

1. [nattienat09](https://github.com/nattienat09)
2. [infinity4471](https://github.com/infinity4471/)

## About the Simulator - Simple Mode

The simulator uses a modified SIR Model which we call SIRDQ. SIRDQ stands for Susceptible, Infectious, Recovered, Deceased, Quarantined.

Once run the application generates a random population of particles on a grid. The default size of the grid is 100x100 but it can be easily modified. In the simple mode every particle moves randomly following a [Brownian Motion](https://en.wikipedia.org/wiki/Brownian_motion). There are 4 particle categories:

:large_blue_circle: Susceptible

:red_circle: Infectious

:green_circle: Recovered

:white_circle: Deceased

Every infectious particle has a specific probability transmitting the infection and a radius of infection which specifies how close two particles have to be for the disease to be transmitted. Furthermore, every particle has a probability of recovering and a probability of dying.

[An example run of simple mode](./img/simple_mode.png)

## Advanced Mode 1 - Point of Interest

In order to better capture some trends we have included a mode where a point of interest is specified. The point of interest is a square of standard side but its center can be modified to be anywhere on the grid. If the point of interest (POI) is specified every particle will move at random times towards it.

[An example run with point of interest](./img/poi_mode.png)

## Advanced Mode 2 - Testing and Quarantine

In this mode we can specify an amount of available tests which we can do to the population. Every time we test an infectious person it is classified as 'Quarantined' and moved to the quarantine until it gets recovered.

No other particles can move into the quarantine and once a quarantined particle gets recovered they move out following their normal movement.

[An example run with testing](./img/poi_test.png)

Of course, the modes can be combined with each other at will.

## :wrench: Setting up and Using the Simulator

You can download the repo locally by running:
```bash
git clone https://github.com/infinity4471/Epidemic-Simulator/
cd Epidemic-Simulator
```
After that you can directly run the simulator by executing
```bash
python3 -B main.py [filename]
```
Where the [filename] can be any text file in which every line is of the following form:
```bash
key=value
```
The key can be any of the following:
```
susceptible, infected, radius, p_infect, p_recover, p_death, poi_x, poi_y, tests
```
An example of an input file can be found on parameters.txt

## Statistical Data

After every simulation the time series of each particle type are previewed in a graph as well as a bar diagram containing the amount of particles in each category at the end of the simulation.

[An example of post simulation analysis](./img/analysis.png)
