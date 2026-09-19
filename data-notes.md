# Data notes

## GRID3 Nigeria Operational Wards v3.0
- Source: https://data.grid3.org
- Downloaded: 13/09/2026
- 5,872 features, polygons
- Columns: country (text), iso3 (text), state (text), statecode (text), lga (text) lga_alt_na (text),  ward (text), ward_alt_n (text), ward_v1_gr (text), ward_in_gr (decimal), multipart_ (decimal), source (text), date (date), area_sqkm (decimal)
- No nulls in ward
- Covers my LGA fully

## GRID3 Nigeria Settlement Extents v4.1 (published August 2026)
- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about
- Downloaded: 13/09/2026
- 2,546,560 features, polygons
- Columns: fid (integer), block_id (text), country (text) iso3 (text), block_area_sqm (decimal), block_perimeter (decimal), block_neigbor_count (integer), building_count (integer), building_area_max (decimal), building_area_sum (decimal), building_area_median (decimal), building_area_stdev (decimal), building_area_percentage (decimal), extent_type (text), mgrs_code (text), ndvi_mean (decimal), evi_mean (decimal), building_max_height (decimal), building_mean_height (decimal), blocks_per_settl_extent (integer), building_count_density_quantile_rank (decimal), building_max_area_quantile_rank (decimal), building_count_density (decimal), bd_class (text), ma_class (text), composite_class (text)
- No specific name field
- Covers my LGA fully

## OSM roads, extracted via QuickOSM
- Query: highway=* within Ogbia LGA extent
- Extracted: 13/09/2026
- 3,438 features, lines
- Many have no surface tag, so paved and unpaved cannot be separated everywhere
- Coverage looks good in both built-up area and edges

## OSM stream, extracted via QuickOSM
- Query: waterway=stream within Ogbia LGA extent
- Extracted: 13/09/2026
- 36,632 features, lines
- Coverage looks good in both built-up area and edges

## OSM river, extracted via QuickOSM
- Query: waterway=river within Ogbia LGA extent
- Extracted: 13/09/2026
- 36,632 features, lines
- Coverage looks good in both built-up area and edges

## Elevation — Copernicus DEM (30 m) 
Source — https://portal.opentopography.org - Geotiff  
- Downloaded: 13/09/2026

  ## CRS and preparation
-All source layers arrived in EPSG:4326
-Study area: Ogbia L.G.A., Bayelsa State, Nigeria, extracted from GRID3 wards version v3.0
-All layers reprojected and clipped to study area, EPSG:32632 (WGS84-UTM ZONE 32N)
-Area check: Ogbia L.G.A.: 713.349 square kilometers (does not match published figures which states that Ogbia  has an area of 695 square km). so my computed area is about 18 square km larger than the published record
-working files in data/processed/, raw files untouched and not pushed to GitHub due to large file sizes. Only the processed files were pushed because they have manageable file sizes
