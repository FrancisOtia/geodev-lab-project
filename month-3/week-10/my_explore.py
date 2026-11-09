import geopandas as gpd

print(gpd.list_layers("data/processed/settlement_extents_utm32.gpkg"))

settlements = gpd.read_file("data/processed/settlement_extents_utm32.gpkg", layer="settlement_extents_utm32")

print(settlements.head())
print("Rows and Columns:", settlements.shape)
print(settlements.geom_type.value_counts())
print("CRS:", settlements.crs)
print("Bounds:", settlements.total_bounds)