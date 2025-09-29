# GEEKGCC
GEEKGCC is a code base for calculating the Koppen-Geiger Climate Classification, a widely used global climate classification, using the Google Earth Engine platform. The inputs are long-term monthly average precipitation and temperature. A simple Earth Engine package using the Python API is available, as well as the code for a web-based demonstration using an Earth Engine hosted website:

https://deductive-water-293819.projects.earthengine.app/view/koppen-climate-map

## Description
This Python-based package creates maps for monthly average climate image Google Earth Engine objects given by the user. Besides loading resulting KGCC maps to memory, the package can downloaded geotif format maps to Google Drive, and when the geemap library is additionally installed, the maps may be visualized. 

While this tool kit is useful for doing batch queries, a website for querying single locations can be accessed at: https://apps.tucson.ars.ag.gov/cligenpar

## Requirements
- Python 3.9 minimum
- GDAL/osgeo library 3.10 minimum
- Pandas library
- Pyinstaller command-line tool (if creating exe)

## Directory Setup
```bash
-Current Working Dir CL_Tool.py
   |--list.txt
   |--search_stations.txt
   |--pars
       |--*.par
   |--wind-strings
       |--*.txt
   |--CCSM4.gdb (at least one GDB needed)
   |--CanESM2.gdb (at least one GDB needed)
   |--MIROC5.gdb (at least one GDB needed)
   |--classes
       |--formatting.py
       |--__init__.py
   |--parfiles-2015
       |--*.par
   |--CL_Tool_Standalone.py (if running as Python script only)
   |--CL_Tool.py (run with PyInstaller when compiling exe)
   |--CL_Tool.exe (after compiling exe, move exe from dist folder to here)
   |--build (created by PyInstaller when compiling exe, not needed after compiling)
   |--dist (created by PyInstaller when compiling exe, not needed after compiling)
```
## User Inputs
The user manually modifies `list.txt` with a list of lat/lon points to write *.par files to the `pars` folder for. The `list.txt` file has placeholder entries as examples, with resulting placeholder files inside `pars` and `wind-strings`. The SWPar4.5 dataset includes all required parameters except for wind parameter sets. In order to produce complete *.par files, an option is to put custom *.txt files inside `wind-strings` that contain formatted wind parameter text blocks, which may be taken from ground stations in `parfiles-2015`. It is then necessary to put the names of these *.txt files in `list.txt`. An easier option is using `Search` as the wind option in `list.txt`, which automatically uses wind parameter sets from the nearest station in `parfiles-2015`.

Valid GCM strings:
```sh
CCSM4, CanESM2, MIROC5
```

Valid year window strings:
```sh
1974_2013, 2000_2029, 2010_2039, 2020_2049, 2030_2059, 2040_2069, 2050_2079, 2060_2089, 2070_2099
```

Valid wind options:
```sh
Search, <some_custom_wind_string_name>
```
## Running
The PyInstaller command used to create the EXEs has the windowless option enabled. This means that the created EXEs run in the background. The EXEs were ran successfully if the outputs specified in list.txt appear in either the pars folder or the maps_out folder, depending on which EXE was used. If the expected outputs don't appear, check for errors in the formatting in list.txt and that the directory structure is correct.
