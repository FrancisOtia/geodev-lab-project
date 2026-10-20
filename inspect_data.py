import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    areas = []
    for row in rows:
        raw_area = row[column].strip()
        if raw_area == "":
            continue
        areas.append(float(raw_area))
        
    return {
        "Smallest":  min(areas),
        "Largest": max(areas),
        "Count": len(areas),
    }
area_stats = inspect_column("settlement_extent.csv", "area_sqm")
print("About to process area stats")
print(area_stats)

elevation_stats = inspect_column("settlement_extent.csv", "elevation_mean_m")
print("About to process elevation stats")
print(elevation_stats)
