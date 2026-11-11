import geopandas as gpd
import matplotlib.pyplot as plt

# Read layers
wards = gpd.read_file(
    "data/processed/Ogbia_Wards_utm32.gpkg"
)

settlements = gpd.read_file(
    "data/processed/settlement_extents_utm32.gpkg",
    layer="settlement_extents_utm32"
)

waterways = gpd.read_file(
    "data/processed/waterway_river_and_stream_utm32.gpkg",
    layer="waterways"
)

# Create 200 m dissolved waterway buffer
waterway_buffer = waterways.buffer(200).union_all()

# Separate settlements
within_200m = settlements[
    settlements.intersects(waterway_buffer)
]

outside_200m = settlements[
    ~settlements.intersects(waterway_buffer)
]

# Create map (wider figure to leave room for the side panel)
fig, ax = plt.subplots(figsize=(12, 10))

# Base layer: Ogbia wards
wards.plot(
    ax=ax,
    color="#F2F2E9",
    edgecolor="#555555",
    linewidth=0.8,
    label="Ogbia Wards"
)

# 200 m waterway buffer
gpd.GeoSeries(
    waterway_buffer,
    crs=waterways.crs
).plot(
    ax=ax,
    color="#B7DDE5",
    alpha=0.5,
    label="200 m Waterway Buffer"
)

# Settlements outside 200 m
outside_200m.plot(
    ax=ax,
    color="#E6F2F3",
    edgecolor="#037E8E",
    linewidth=0.5,
    label="Outside 200 m"
)

# Settlements within 200 m
within_200m.plot(
    ax=ax,
    color="#D62828",
    edgecolor="#7A1010",
    linewidth=0.5,
    label="Within 200 m"
)

# Waterways
waterways.plot(
    ax=ax,
    color="#094923",
    linewidth=0.6,
    label="Waterways"
)

# Map title
ax.set_title(
    "Ogbia Settlements Within 200 m of Waterways",
    fontsize=14
)

# Legend: outside the map, top of the right-hand panel
ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.02, 1.0),
    fontsize=9,
    title="Legend",
    title_fontsize=10,
    frameon=True,
    facecolor="white",
    edgecolor="#555555",
    borderaxespad=0
)

# Statistics: outside the map, bottom of the right-hand panel
stats = (
    "SETTLEMENT STATISTICS\n"
    "Within 200 m: 630\n"
    "Total settlements: 1,066\n"
    "Outside 200 m: 436"
)

ax.text(
    1.02, 0.0,
    stats,
    transform=ax.transAxes,
    fontsize=9,
    verticalalignment="bottom",
    horizontalalignment="left",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="#555555",
        alpha=0.9
    )
)

# Map formatting
ax.set_axis_off()

# Save map (bbox_inches="tight" keeps the side panel in the saved image)
fig.savefig(
    "month-3/week-11/my_ogbia_waterways_map_2.png",
    dpi=150,
    bbox_inches="tight"
)

print("Map saved: my_ogbia_waterways_map_2.png")