# Architecture Notes

The integration follows a read, compare, plan, and apply shape:

- Read: obtain stock quantities by SKU from SQL Server.
- Compare: compare returned quantities with a local synchronization snapshot.
- Plan: classify changes as simple-product or variation updates.
- Apply: send bounded WooCommerce REST API batches only outside dry-run mode.
- Record: persist a new synchronization snapshot only after successful calls.

The distinction between "not returned" and `0` is important. A missing row may
indicate incomplete source data, so it must not silently create an out-of-stock
update. A returned numeric zero is a real business value and can be synchronized.
