import ee
import geekgcc
import geemap

ee.Authenticate()
geeusername = 'andrewfullhart' #Enter your GEE username.
ee.Initialize(project='ee-' + geeusername)

vis = True
dl = False

###############
#PRE-PROCESSING
###############
worldclim_path = 'WORLDCLIM/V1/MONTHLY'
ic = ee.ImageCollection(worldclim_path)

#Northern hemi-sphere
custom_geo = ee.Geometry.BBox(-180.00, 0.00, 179.99, 89.99)
#Southern hemi-sphere
#custom_geo = ee.Geometry.BBox(-180.00, 0.00, 179.99, -89.99)

def clip_fn(im_obj):
  im = ee.Image(im_obj)
  clip_im = im.clip(custom_geo)
  return clip_im

ic_clip = ee.ImageCollection(ic.map(clip_fn))
t_scaled_ic = ee.ImageCollection(ic_clip.select('tavg'))

def unit_scaling_fn(im_obj):
  scaled_im = ee.Image(im_obj)
  im = scaled_im.multiply(0.1)
  return im

#Monthly mean precipitation (12 images)
p_ic = ee.ImageCollection(ic_clip.select('prec'))
#Monthly mean temperature (12 images)
t_ic = ee.ImageCollection(t_scaled_ic.map(unit_scaling_fn))

###############
#CLASSIFICATION
###############
type_im = geekgcc.KGCC.classify(p_ic, t_ic, 'north')

############
#DOWNLOADING
############
if dl == True:
  #Scale is a client-side object that can be determined from
  #the first image in the collection used to calculate p_ic and t_ic.
  scale = ic.first().projection().nominalScale().getInfo()
  #client-side object of the downloaded geotif file name.
  file_name = 'test_kgcc_map'
  geekgcc.KGCC.download(type_im, custom_geo, scale, file_name)

############
#VISUALIZING
############
if vis == True:
  vis_params = geekgcc.KGCC.get_vis_params()
  geemap.ee_initialize()
  Map = geemap.Map(center=[40,-100], zoom=3)
  Map.addLayer(type_im, vis_params)

  #Use Map.save() can be used when running on a desktop-based code editor.
  #this will save the map widget as an html doc in the working directory
  Map.save('map.html')

  #Use Map when an online web-based editor like Google Colab.
  #Map
