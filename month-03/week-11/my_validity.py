
from shapely.validation import explain_validity
import geopandas as gpd

wards = gpd.read_file("data/processed/Ogbia_Wards_utm32.gpkg")

print("Valid:", wards.is_valid)
print("Why:", [explain_validity(geom) for geom in wards.geometry])

valid_count = wards.is_valid.sum()
invalid_count = (~wards.is_valid).sum()

print("Valid geometries:", valid_count)
print("Invalid geometries:", invalid_count)
print("Total geometries:", len(wards))

layer = wards.copy()
layer["geometry"] = layer.make_valid()

print("Valid now:", layer.is_valid.all())
print("New type:", layer.geom_type.iloc[0])


