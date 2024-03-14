----
cubetools
----

Python tools for working with Gaussian-style .cube files. This library includes functions to:
- Read and write Gaussian .cube files
- Rescale .cube files from e/voxel to e/bohr<sup>3</sup> (for CASTEP-generated charge densities)
- Translate and rotate .cube data
- Integrate around a particular atom
- Integrate within a spherical region
- Integrate the whole .cube file
- Take the planar average
- Add/subtract/multiply .cube files

Planar averages are outputted as a column of distance and electrons. It is normalized to give the total number of electrons.

Integrating around an atom or reference point requires xyz coordinates as an input. They must be given as Angstroms. This holds true for the chosen reference point too.  

Requires numpy and scipy. If you have pip, you can just run
```
pip install git+https://github.com/mmojsak/cubetools
```
to install the ``cubetools`` module and an executable of the same name into the currently preferred Python package installation directories.

Alternatively, you can clone the repository manually and run
```
pip install -r requirements.txt
```
to install all the requirements.

The code should be run from the command line, but can also be used as a library (all functions are defined in the ``cubetools.py`` module). While no documentation currently exists for use as a library, runing from the command line uses the following arguments:

positional arguments:
  Files                 Input .cube files

optional arguments:
* -h, --help            Show this help message and exit
* -rs, --rescale        Rescale a CASTEP .cube file to e/bohr^3
* -a, --add             Add two or more cube files together
* -s, --subtract        Subtract two or more cube files together
* -M, --multiply        Multiply two or more cube files together
* -p [POWER], --power [POWER]  Raise the cube file to a certain power. Any number of cube files can be specified and they will all be raised to the power defined. Default is to square the cube file(s).
* -t TRANSLATE TRANSLATE TRANSLATE, --translate TRANSLATE TRANSLATE TRANSLATE  Translate a cube file. Requires a translation vector as an argument.
* -i INTEGRATE, --integrate INTEGRATE  Integrate over the entire cube file.
* -ia INTEGRATE, --integrate INTEGRATE atomId Radius  Integrate a sphere around an atom. Requires atom ID and the radius of the sphere
* -ir INTEGRATE, --integrate INTEGRATE x y z Radius  Integrate a sphere around a point. Requires x y z coordinate of point and the radius of the sphere
* -e EXPAND EXPAND EXPAND, --expand EXPAND EXPAND EXPAND  Make a supercell of the specified cube file
* -m MEAN, --mean MEAN  Calculate planar average of a cube file along a particular axis. Normalized to give the total number of electrons (particles). Arguments are necessarily x,y or z.


usage: cube_tools.py [-h] [-rs] [-a] [-s] [-p [POWER]] [-t TRANSLATE TRANSLATE TRANSLATE] Files [Files ...]
