## Month-3 Week 11: reprojection and spatial operations
- Learnt to reproject from EPSG:4326 to EPSG:32632 with to_crs
- Mapped Ogbia settlements within 200 m of rivers and streams using GeoPandas.
- All week 11 example files are in order

### What's in the folder
- `area_wrong_and_right.py`
- `clip_dissolve.py`
- `coverage_gap.py`
- `fix_geometry.py`
- `my_counts.py`
- `my_crs.py`
- `my_ogbia_waterways_map.png`
- `my_ogbia_waterways_map_2.png`
- `my_reach.py`
- `my_unmatched_settlements_optional.png`
- `my_unmatched_settlements_optional2.png`
- `my_validity.py`
- `my_week11_map.py`
- `nearest.py`
- `one_point.py`
- `README.md`
- `set_vs_to.py`
- `spatial_ops.py`

### How to run it
- Run it with `uv run month-03/week-11/filename.py`
- E.g `uv run month-03/week-11/my_counts.py`

### What I found and what went wrong
- 3 Settlements were not matched
- 1063 out of 1066 settlements matched
- The remaining 3 settlements failed to match because they were located at the extreme edges of the ward boundaries, resulting in unmatched spatial joins.