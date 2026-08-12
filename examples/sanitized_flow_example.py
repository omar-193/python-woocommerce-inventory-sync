"""Small, non-runnable illustration of simple products versus variations."""

fake_map = {
    "DEMO-SKU-SIMPLE": {"id": 101, "parent_id": 0},
    "DEMO-SKU-VARIATION": {"id": 202, "parent_id": 200},
}

groups = {"products": [], "variations": {}}
for sku, item in fake_map.items():
    if item["parent_id"] == 0:
        groups["products"].append(sku)
    else:
        groups["variations"].setdefault(item["parent_id"], []).append(sku)

# API calls, credentials, cache writes, and database access are omitted.
