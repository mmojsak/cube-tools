#!/usr/bin/env python

import cubetools
from sys import argv


rCube = cubetools.cube(argv[1])
rCube.super_cube([2,2,2])
rCube.write_cube('test.cube')
