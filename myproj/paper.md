---

title: 'gee-kgcc.js: A Google Earth Engine codebase for Koppen-Geiger climate classification' 
tags:
- JavaScript  
- Google Earth Engine  
- Koppen-Geiger climate classification  
- climate  
- ecosystem

authors:
- name: Andrew T. Fullhart  
  orcid: 0000-0003-1223-6451  
  equal-contrib: true  
  affiliation: 1  
- name: Shang Gao  
  orcid: 0000-0001-8641-2433  
  equal-contrib: true  
  affiliation: 1  
- name: Guillermo E. Ponce-Campos  
  orcid: 0000-0003-4332-338X  
  equal-contrib: true  
  affiliation: 1  
- name: Gerardo Armendariz  
  orcid: 0000-0003-1130-3392  
  equal-contrib: true  
  affiliation: 2

affiliations:
- name: School of Natural Resources and the Environment, University of Arizona, United States  
  index: 1  
- name: Southwest Watershed Research Center, USDA-ARS, United States  
  index: 2

date: 13 August 2017  
bibliography: paper.bib

---

# Summary

This work presents a codebase for calculating and visualizing the Koppen-Geiger (KGCC) climate classification in Google Earth Engine (GEE). The KGCC has thirty global climate type definitions that use thresholds of seasonal temperature and precipitation to delineate geographic regions with similar climates. The codebase includes a template for creating a KGCC map that can be applied to several publicly listed data products. The template was used to build a basic web app hosted by GEE, the code for which is provided so that a user may launch their own instance of the app in an Online Code Editor session. The app visualizes KGCC maps derived from climate projections to predict how KGCC regions may change over time based on the high-resolution NEX-DCP30 dataset for the CMIP5 ensemble of global climate models (GCMs), with coverage of the contiguous US. Taking advantage of the ability to process large collections of climate images in GEE, ensemble-based uncertainty maps can be viewed that quantify the likelihood of a climate type existing at a given time and location. In addition to being a generalized characterization of climate, the resulting KGCC visualizations are a means of understanding the range of outcomes given by GCMs and climate scenarios. As an example of a use-case, an analysis was done to estimate the percentage of land in the US that is projected to see a transition in climate type, having implications for land management, agriculture, and other climate dependent sectors.

# Statement of need

Climate datasets are often very large and require intensive processing to derive factors of interest. However, decision-makers often lack the resources and ability to do such processing. Therefore, it becomes desirable to have a web platform available to access relevant information (Hewitson et al., 2017). The Koppen-Geiger climate classification (KGCC) is one such climate factor that delineates global climate types and provides a general characterization of climate [@beck:2023]. The KGCC was developed to be correlative with vegetation communities, therefore often coinciding with ecosystem regions. Also, KGCC is a factor that can be applied in the context of climate change because it is determinable for historical and future periods alike. As such, using KGCC in the decision-making process can allow for incorporation of standardized climate projections and other datasets.

The computational resources of GEE are an advantage for this by quickly processing large climate datasets, enabling assessment of a range of outcomes given by GCM ensembles and various fossil fuel emission scenarios (Gorelick et al., 2017). This is particularly useful for determining ensemble statistics and deriving uncertainties that allow for a more comprehensive assessment of risk and better justification of decisions. Another benefit of GEE is that all calculations done by this codebase are fast enough to be performed on-the-fly, which means that it is not necessary for client-side storage of outputs.

# Koppen-Geiger Climate Classification

The Koppen-Geiger Climate Classification (KGCC) is a widely used global climate classification first developed by Wladimir Koppen in the 19th century and later refined by Rudolf Geiger (Kottek et al., 2006). The KGCC requires input data with at least monthly-scale temporal resolution to calculate 30 global climate types. Generally, a minimum reference period of 30 years should be used in order to represent climate. According to KGCC, there are 5 main divisions of climate: tropical (A), arid (B), temperate (C), continental (D), and polar (E) that correspond to the first letter in the labeling scheme. Then, these are further divided into second and third-order classifications, indicated by the number of letters in their respective labels. Divisions are made using a number of temperature and precipitation thresholds. This requires the data to be statistically reduced in different ways, such as by season, by maximum and minimum monthly or seasonal values, by average annual precipitation, and other intermediate statistical values. Literature works involving KGCC commonly include definitions of individual climate types (e.g., Beck et al. 2023), and additionally, Kottek et al. (2006) have good discussion of strategy for calculating the entire classification.

# The gee-kgcc.js codebase

The [gee-kgcc.js](https://github.com/ARS-SWRC/GEE-KGCC) codebase includes three scripts that use two different high-resolution, monthly-scale climate datasets freely available on the GEE catalog, and other datasets may be applied including datasets with other temporal resolutions, such daily-scale, if they are first aggregated to monthly-scale images. The two climate datasets were selected primarily because they have at least \~1 km spatial resolution, which makes them ideal for showing climate gradients over small distances. The `minimal_classification.js` script makes use of the global WorldClim dataset that, in the GEE catalog, is already monthly averaged for a 31-year period (hijmans et al., 2005). This reduces the pre-processing steps needed to prepare the data, as well as the number of possible input options to handle (e.g. date range, projection scenario, etc.), which would otherwise necessitate the main code block to be placed inside a function and passing input options as arguments. As such, this script is suitable for demonstration purposes and represents the minimum code needed for use in other applications. Furthermore, the script includes options to queue a download of the resulting map output to Google Drive, as well as to change the spatial extent of the map to a different geographic region of interest. The other two scripts that will be discussed, `spatial_analysis_trends.js` and `viz.js`, involve the second climate dataset, NEX-DCP30, which consists of climate projections for the contiguous US consisting of 33 GCMs from the CMIP5 ensemble (Thrasher et al., 2013).

# Determining KGCC by processing climate images

To illustrate the strategy for processing KGCC in GEE, the following code snippet demonstrates how the third-order BSk (cold semi-arid) type is delineated, which is a common type globally that contains rangeland and steppe environments. The snippet shows use of intermediate images for applying the criteria of each type, which will be described in-text. Otherwise, the code snippet shows only the final steps necessary for delineating the higher order types and BSk itself.

```` ```js client ````  
`//E`  
`var e_im = tw_im.lt(10.0);`

`//B`  
`var sin_e_im = tw_im.gte(10.0);`  
`var con_b_im = zero_im.where(pann_im.lt(pthr_im.multiply(10.0)), 1);`  
`var mix_im = con_b_im.add(sin_e_im);`  
`var b_im = mix_im.eq(2.0);`

`//BS`  
`var con_bs_im = zero_im.where(pann_im.gt(pthr_im.multiply(5.0)), 1);`  
`var mix_im = b_im.add(con_bs_im);`  
`var bs_im = mix_im.eq(2.0);`

`//BSk`  
`var con_bsk_im = zero_im.where(tann_im.lt(18.0), 1);`  
`var mix_im = bs_im.add(con_bsk_im);`  
`var bsk_im = mix_im.eq(2.0);`  
```` ``` ````

The main E division (polar and high mountain climates) is delineated first because its criteria exclude thresholds for precipitation and only a temperature threshold involving the average temperature of the warmest calendar month (`tw_im`) is used, resulting in potential overlap with other types. Therefore, the arid main climate type, B division, is considered present where the criteria for B are met (represented in the binary image, `con_b_im`) and where type E is not already present (the absence of E is represented in the binary image, `sin_e_im`). The integer image, `mix_im`, is the summation of the two binary images, such that type B is present where `mix_im` is equal to 2, and a binary image representing this condition, `b_im`, is created. The `zero_im` image is used as the initial blank binary image with only zero integer values onto which the binary conditions of each division are added.

The first and second-order divisions for B involve thresholds for a seasonal dryness metric, `p_thr_im`, such that BS is defined as having annual precipitation, `pann_im`, between upper and lower limit values of this metric. Finally, the third-order division depends on thresholds for mean annual temperature, `tann_im`. In this way, BSk and the other sub-divisions are delineated by creating binary images representing threshold conditions at each division that are summed to determine overlapping areas where all conditions are met. The map panels in Figure 1 show the binary images that are created for E, B, BS, and BSk in respective panels.

# Spatial analysis with KGCC maps

The `gee-kgcc.js` codebase includes `spatial_analysis_trends.js`, which creates a chart of a basic spatial analysis as an example of one possible way to obtain useful information from the maps in the context of climate change. Shown in Figure 2, the purpose of this analysis is to show a timeline of transitions in climate type within a given area. In this case, the entire coverage area of NEX-DCP30 is analyzed (being the continuous US) and includes the outputs of one GCM and four climate scenarios. Note that it is possible to change the processing extent in `spatial_analysis_trends.js` so that the same analysis can be repeated for a selected area of interest.

By providing a range of trends according to different emission scenarios known as Representative Concentration Pathways (RCP4.5), uncertainty bounds can be reasonably estimated, aiding the understanding of the range of outcomes. Note that these values are substantially greater than reported by Beck et al. (2023) in their global analysis of KGCC in climate projections because their analysis considered a different dataset and showed change occurring only across the 5 main climate types rather than across any of the 30 sub-order types. It is also possible that the US experiences greater rates of change in climate type than what occurs globally due to the high diversity of climates. Although, in the eastern US, some have noted lack of specificity in KGCC definitions for temperate and humid climates in the eastern US, and modified climate classifications, such as the Köppen–Trewartha climate classification, have been developed to address this issue (Belda et al. 2014).

# Web Application

The GEE platform has basic widgets in its API for creating the features of a web application that uses GEE as a backend. We include a script, `viz.js`, showing the code used to make the app hosted at [https://deductive-water-293819.projects.earthengine.app/view/koppen-climate-map](https://deductive-water-293819.projects.earthengine.app/view/koppen-climate-map), which visualizes climate change projections from NEX-DCP30. Additionally, the script can be launched from the online GEE code editor, which results in the same maps and widgets appearing as in the web app. The app features are aimed at enabling the user to do basic analysis for an area of interest and understanding the GCM ensemble and related uncertainties.

The following are the main features included in the app:

* Selection of a 30-year date range.  
* Selection of RCP emission scenarios.  
* Selection of GCM.  
* Uncertainties based on percentage of agreement of GCMs for each climate type given the selected date range and emission scenario.  
* Clickable map layer to show a timeline of KGCC types at the point clicked.  
* Tool to define polygon for which a timeline is produced of change in KGCC types by land area.  
* Toggle EPA Level IV Ecoregions base layer.

# Figures

![BSk-demo](https://raw.githubusercontent.com/ARS-SWRC/GEE-KGCC/f0c69fbe5a83896f14dc52d7be51afbebb1d53c1/Figures/BSk-Demo.png)
Figure 1: Example of BSk delineation showing intermediate maps and a final KGCC map. The panels are as follows: (a) map coverage area, (b) `e_im`, c) `b_im`, (d) `bs_im`, (e) `bsk_im`, (f) final KGCC map. 

![ee-chart](https://raw.githubusercontent.com/ARS-SWRC/GEE-KGCC/19e7aa6f58a715b8e0007242c515e69788c72d8c/Figures/ee-chart.png)
Figure 2: Timeline of the percentage of land area that changes its climate type over a 130 year reference period with different RCPs represented.

# Acknowledgements

We acknowledge providers of open-access climate data, which were relied on to produce this work.

# References
