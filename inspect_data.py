import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    values = []
    non_numeric = 0
    
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        try:
            values.append(float(raw))
        except ValueError:
            non_numeric += 1
        
    if not values:
        return "No valid values found"
        
    return {
        "Smallest":  min(values),
        "Largest": max(values),
        "Count": len(values),
        "Average": sum(values) / len(values),
        "Non-numeric values": non_numeric
    }
area_stats = inspect_column("settlement_extent.csv", "area_sqm")
print("About to process area stats")
print(area_stats)

elevation_stats = inspect_column("settlement_extent.csv", "elevation_mean_m")
print("About to process elevation stats")
print(elevation_stats)
