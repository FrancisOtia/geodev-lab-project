
import pandas as pd
import geopandas as gpd

# 1. Read settlement points CSV
table = pd.read_csv("data/processed/settlement_points.csv")

print(table.head(3))

# 2. Create GeoDataFrame using Easting and Northing
settlements = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(
        table["Easting"],
        table["Northing"]
    ),
    crs="EPSG:32632"
)

# 3. Inspect the GeoDataFrame
print(settlements.head(3))
print(settlements.crs)

# 4. Export to GeoPackage
settlements.to_file(
    "data/processed/settlement_points.gpkg",
    layer="settlement_points",
    driver="GPKG"
)

print("Saved", len(settlements), "settlement points")
