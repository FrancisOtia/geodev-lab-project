
import geopandas as gpd

wards = gpd.read_file("data/processed/Ogbia_Wards_utm32.gpkg").to_crs(epsg=32632)
settlements = gpd.read_file(
    "data/processed/settlement_points.gpkg", layer="settlement_points"
).to_crs(epsg=32632)

# count settlements per ward
joined = gpd.sjoin(
    settlements, wards[["ward", "geometry"]], how="inner", predicate="within"
)
counts = joined.groupby("ward_left").size().rename("settlement_count").reset_index()
wards = wards.merge(counts, left_on="ward", right_on="ward_left", how="left")
wards["settlement_count"] = wards["settlement_count"].fillna(0).astype(int)

print(wards[["ward", "settlement_count"]])
print("Total counted:", wards["settlement_count"].sum(), "of", len(settlements), "settlements")

# identify settlements not matched to any ward
check = gpd.sjoin(
    settlements, wards[["ward", "geometry"]],
    how="left", predicate="within"
)

unmatched = check[check["index_right"].isna()]

print("Unmatched settlements:", len(unmatched))
print(unmatched[["settl_id", "ward_left"]])

boundary_check = gpd.sjoin(
    unmatched.drop(columns=["index_right"]),
    wards[["ward", "geometry"]],
    how="left", predicate="intersects"
)

print("Boundary matches:", boundary_check["index_right"].notna().sum())
