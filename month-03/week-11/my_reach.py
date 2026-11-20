import geopandas as gpd

# Read datasets (each layer comes from its own GeoPackage)
settlements = gpd.read_file(
    "data/processed/settlement_extents_utm32.gpkg",
    layer="settlement_extents_utm32"
).to_crs(epsg=32632).copy()

waterways = gpd.read_file(
    "data/processed/waterway_river_and_stream_utm32.gpkg",
    layer="waterways"
).to_crs(epsg=32632).copy()

# Create a single dissolved 200 m buffer around all waterways
# (avoids duplicate settlement rows from overlapping buffers)
waterway_buffer = waterways.buffer(200).union_all()  # use .unary_union on geopandas < 1.0

# Identify settlements within 200 m of waterways
within_200m = settlements[settlements.intersects(waterway_buffer)].copy()
outside_200m = settlements[~settlements.intersects(waterway_buffer)].copy()

print("Settlements within 200m:", len(within_200m))
print("Total settlements:", len(settlements))
print("Settlements outside 200m:", len(outside_200m))