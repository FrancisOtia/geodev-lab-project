import numpy as np
import rasterio
import matplotlib.pyplot as plt

folder = "data/processed/ogbia_landsat/"
prefix = "ogb_"
scene = "LC08_L2SP_189057_20240117_20240130_02_T1"

with rasterio.open(folder + prefix + scene + "_SR_B4.TIF") as src:
    red_raw = src.read(1).astype("float32")
    profile = src.profile

with rasterio.open(folder + prefix + scene + "_SR_B5.TIF") as src:
    nir_raw = src.read(1).astype("float32")

valid = (red_raw > 0) & (nir_raw > 0)

red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

ndvi = np.full(red.shape, -9999, dtype="float32")
total = nir + red
ok = valid & (total != 0)

ndvi[ok] = (nir[ok] - red[ok]) / total[ok]

low = round(float(ndvi[ok].min()), 3)
high = round(float(ndvi[ok].max()), 3)

print("NDVI range:", low, "to", high)
print("Mean NDVI:", round(float(ndvi[ok].mean()), 3))

profile.update(dtype="float32", nodata=-9999, count=1)

with rasterio.open("data/processed/my_ogbia_ndvi.tif", "w", **profile) as dst:
    dst.write(ndvi, 1)

print("Saved data/processed/my_ogbia_ndvi.tif")

# Plot NDVI
ndvi_masked = np.ma.masked_equal(ndvi, -9999)

fig, ax = plt.subplots(figsize=(7, 8))
image = ax.imshow(ndvi_masked, cmap="RdYlGn", vmin=-0.2, vmax=0.9)

fig.colorbar(image, ax=ax, label="NDVI")
ax.set_title("Vegetation index, Ogbia L.G.A. of Bayelsa State")
ax.set_axis_off()

fig.savefig(
    "month-03/week-12/my_map.png",
    dpi=150,
    bbox_inches="tight"
)

print("Saved my_map.png in month-03/week-12/my_map.png")