
import geopandas as gpd
import matplotlib.pyplot as plt

# Read layers
wards = gpd.read_file("data/processed/Ogbia_Wards_utm32.gpkg")

settlements = gpd.read_file(
    "data/processed/settlement_extents_utm32.gpkg"
)

points = gpd.read_file(
    "data/processed/settlement_points.gpkg",
    layer="settlement_points"
)

# Create map
fig, ax = plt.subplots(figsize=(9, 10))

# Base layer: Ogbia wards
wards.plot(
    ax=ax,
    color="#F2F2E9",
    edgecolor="#555555",
    linewidth=0.8
)

# Settlement polygons
settlements.plot(
    ax=ax,
    color="#E6F2F3",
    edgecolor="#037E8E",
    linewidth=0.5
)

# Settlement centroid points
points.plot(
    ax=ax,
    color="#094923",
    markersize=12
)

# Map title and formatting
ax.set_title("Ogbia Settlements", fontsize=14)
ax.set_axis_off()

# Save map
fig.savefig(
    "month-3/week-10/my_ogbia_settlement_map.png",
    dpi=150,
    bbox_inches="tight"
)

print("Map saved: my_ogbia_settlement_map.png")
