var lsib = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
var countryNames = lsib.aggregate_array('country_na').sort().getInfo();
print(countryNames);

var countrySelectStyle = {
  width:'300px'
};

function renderCountry(selectedCountry){
  Map.layers().reset();
  print(selectedCountry);
  var country = lsib.filter(ee.Filter.eq('country_na',selectedCountry));
  Map.addLayer(country.style({color:'red', fillColor:'ff000050'}));
  Map.centerObject(country);
}

var renderDropdown = ui.Select({
  items:countryNames, 
  placeholder:'Select a Country', 
  onChange:renderCountry,
  style:countrySelectStyle
});

var panelStyle = {
  backgroundColor:'pink'
};

var leftPanel = ui.Panel({style:panelStyle});
leftPanel.add(renderDropdown);
ui.root.insert(0, leftPanel);


