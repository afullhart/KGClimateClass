# GEEKGCC
GEEKGCC is a code base for calculating the Koppen-Geiger Climate Classification (KGCC), a widely used global climate classification, using the Google Earth Engine API (gee). The inputs are long-term average monthly precipitation and temperature. A simple Earth Engine package using the Python gee API is available, as is the code for a web-based demonstration using an Earth Engine hosted website:

https://deductive-water-293819.projects.earthengine.app/view/koppen-climate-map

## Description
This Python-based package creates KGCC maps from monthly climate images prepared by the user. The gee dependency handles these images as Earth Engine image collection objects. Besides loading resulting KGCC maps to memory, the package can download KGCC geotif maps to Google Drive. Additionally, when the geemap library is installed, the maps may be visualized. 

While this tool kit is useful for doing batch queries, a website for querying single locations can be accessed at: https://apps.tucson.ars.ag.gov/cligenpar

## Requirements
- Google Account
- Google Earth Engine Account
- Python 3.9 minimum
- earthengine-api
- geemap (optional for visualization)

## Setup
In Google Colab, all setup requirements are already met. The earthengine-api (ee) depency is automatically installed with geekgcc and Colab. When using Colab, prepend an exclamation mark (!) to the beginning of the following two code lines.
**To install the geekgcc Python package using Git and Pip:**
```bash
git clone https://github.com/ARS-SWRC/GEE-KGCC
pip install GEE-KGCC/geekgcc_package
```
**To install the geekgcc Python package locally from a downloaded clone of the repository, use the following steps.** In an environment tool like conda, activate your Python environment and navigate to the top of the geekgcc_package sub-directory, which should contain a .toml file. Then, run the following Pip command:
```bash
pip install .
```
**For visualization, additionally install the geemaps library. In Colab, this library is pre-installed.**
https://geemap.org/

**To authenticate ee and import necessary libraries, use the following steps.** Start by importing, authenticating, and initializing ee, then import geekgcc.
```python
import ee
#This will open a web browser for log-in steps.
ee.Authenticate()
geeusername = 'andrewfullhart' #Enter your GEE username.
ee.Initialize(project='ee-' + geeusername)
#ee should be initialized before importing geekgcc.
import geekgcc
```
The the string argument for ee.Initialize() assumes the default project name assigned by Earth Engine. If some other project name is used, modify the code accordingly. The web browser log-in steps may assist with creating and choosing a project, or a project may be created using the online ee code editor.

## User Inputs
The user must provide ee image collections of long-term average monthly precipitation and temperature (12 images each). These should be overlapping images and should exist enitrely within a hemisphere (i.e., not in both hemispheres, such that at least two operations are needed to produce global coverage). WGS84 coordinate system is assumed in geekgcc, so climate images should be reprojected if they are in some other coordinate system.

The following methods are included in geekgcc: `classify()`, `download()`, and `get_vis_params()`.



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
