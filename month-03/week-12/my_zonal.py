import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("data/processed/cop_dem_30m_utm32/cop_dem_30m_utm32.tif") as src:
    wards = gpd.read_file(
        "data/processed/Ogbia_Wards_utm32.gpkg",
        layer="Ogbia_Wards_utm32"
    ).to_crs(src.crs)

    means = []

    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means, 1)

results = wards[["ward", "mean_elevation_m"]]

print(results)

results.to_csv("month-03/week-12/my_zonal_stats.csv", index=False)

print("Saved my_zonal_stats.csv in month-03/week-12/my_zonal_stats.csv")