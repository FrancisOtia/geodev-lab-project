import pandas as pd
import geopandas as gpd

settlements = gpd.read_file("data/processed/settlement_extents_utm32.gpkg",layer="settlement_extents_utm32")
points = pd.read_csv("data/processed/settlement_points.csv")

first_try = settlements.merge(
    points,
    left_on="settlement_extents_utm32_settl_id",
    right_on="settl_id",
    how="left"
)

matched = first_try["Easting"].notna().sum()
print("Matched on first try:", matched, "of", len(settlements), "settlements")

def clean_name(name):
    return str(name).strip().upper().replace("-", " ")

settlements["join_key"] = settlements["settlement_extents_utm32_settl_id"].apply(clean_name)
points["join_key"] = points["settl_id"].apply(clean_name)

joined = settlements.merge(points, on="join_key", how="left")
matched = joined["Easting"].notna().sum()

print("Matched after cleaning:", matched, "of", len(settlements), "settlements")
print(joined[["settlement_extents_utm32_settl_id", "Easting", "Northing"]])
