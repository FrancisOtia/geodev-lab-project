# This script extracts settlement centroids and selected attributes from the settlement extents layer.
# This helps in creating a point representation of settlements for further spatial analysis.
# Specifically, it helps me prepare the datasets I needed to carry out my_points.py exercise.


import geopandas as gpd

# 1. Read settlement layer
settlements = gpd.read_file(
    "data/processed/settlement_extents_utm32.gpkg"
)

# 2. Calculate settlement centroids
centroids = settlements.geometry.centroid

# 3. Extract selected attributes
settlement_points = settlements[
    [
        "OBJECTID",
        "settlement_extents_utm32_settl_id",
        "within_200m_waterway",
        "ward",
        "ZonalSt_settlem1_AREA",
        "ZonalSt_settlem1_MEAN",
        "ZonalSt_settlem1_MIN",
        "ZonalSt_settlem1_MAX"
    ]
].copy()

# 4. Rename fields
settlement_points = settlement_points.rename(
    columns={
        "settlement_extents_utm32_settl_id": "settl_id",
        "ZonalSt_settlem1_AREA": "area",
        "ZonalSt_settlem1_MEAN": "mean_elevation",
        "ZonalSt_settlem1_MIN": "min_elevation",
        "ZonalSt_settlem1_MAX": "max_elevation"
    }
)

# 5. Extract Easting and Northing
settlement_points["Easting"] = centroids.x
settlement_points["Northing"] = centroids.y

# 6. Print summary
print(f"Total settlements: {len(settlements)}")
print(f"Centroid points generated: {centroids.notna().sum()}")

# 7. Export CSV
settlement_points.to_csv(
    "data/processed/settlement_points.csv",
    index=False
)

print("Successfully created settlement_points.csv")
print(f"Total records exported: {len(settlement_points)}")
