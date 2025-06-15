
var ic = ee.ImageCollection("NASA/NEX-DCP30");
print(ic.first());
print(ic.first().get('model'));
print(ic.first().get('scenario'));

function get_fn(im_obj){
  var im = ee.Image(im_obj);
  var gcm = im.get('model');
  var scn = im.get('scenario');
  var im_list = ee.List([gcm, scn]);
  return ee.Feature(null, {thing:im_list});
}

var big_fc = ee.FeatureCollection(ic.map(get_fn));
print(big_fc.size());

Export.table.toDrive({
  collection: big_fc,
  description: 'big_fc'
});
