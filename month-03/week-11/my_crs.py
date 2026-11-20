
import geopandas as gpd

settlements = gpd.read_file("data/raw/settlement_extents_epsg4326.gpkg", layer="settlement_extents")
first = settlements.geometry.iloc[0].geoms[0].exterior.coords[0]
print("Original first corner:", first)

recommended_crs = settlements.estimate_utm_crs()
print("Recommended UTM CRS:", recommended_crs)

projected = settlements.to_crs(epsg=32632)
print("After to_crs:", projected.geometry.iloc[0].geoms[0].exterior.coords[0])

wrongly_labelled = settlements.set_crs(epsg=32632, allow_override=True)
print("After set_crs:", wrongly_labelled.geometry.iloc[0].geoms[0].exterior.coords[0])
print("Label now says:", wrongly_labelled.crs)
