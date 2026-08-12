"""Illustrative pseudocode only; not a complete synchronization implementation."""


def plan_delta(current_by_sku, previous_by_sku, product_map):
    planned = []
    warnings = []
    for sku, product in product_map.items():
        if sku not in current_by_sku:
            warnings.append(f"missing source SKU: {sku}")
            continue
        quantity = current_by_sku[sku]
        if previous_by_sku.get(sku) == quantity:
            continue
        planned.append({"product": product, "stock_quantity": quantity})
    return planned, warnings


# Sending batches, persistence, retries, and orchestration are intentionally omitted.
