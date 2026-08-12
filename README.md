# Python WooCommerce Inventory Sync - Portfolio Case Study

This repository is a sanitized portfolio case study based on concepts used in a
real production inventory synchronization system.

The real production implementation is private. This repository demonstrates the
architecture, engineering approach, technical decisions, safety considerations,
and validation strategy only. It intentionally does **not** include the complete
runnable production implementation.

AI-assisted development tools were used during implementation, research,
debugging, testing, and code review. Solutions were reviewed and validated
before being used in real business operations.

## Architecture at a glance

```text
SQL Server
    | inventory query
SKU / product mapping
    |
Delta comparison against a local stock cache
    | grouped batches
WooCommerce REST API
    |
Logging and operational review
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the data flow and design decisions.

## Technical concepts demonstrated

- SQL Server as the inventory source
- SKU mapping for simple products and variations
- Delta synchronization so unchanged quantities are skipped
- Safe distinction between a missing SKU and an actual quantity of zero
- Batch-oriented WooCommerce updates
- Cache updates only after successful synchronization
- Dry-run planning without sending updates
- Environment-variable configuration
- Retry/backoff as an operational resilience concept

## Public contents

- `ARCHITECTURE.md` - system boundaries, Mermaid flow, and design decisions
- `docs/architecture.md` - additional data-flow notes
- `examples/` - intentionally incomplete pseudocode and flow examples
- `data/product_map.example.json` - fake identifiers only
- `.env.example` - configuration names with placeholders only
- `test_scenarios.md` - validation scenarios and expected outcomes
- `SECURITY.md` - public-data and disclosure boundaries
- `COPYRIGHT.md` - portfolio-only usage notice

## What is intentionally omitted

This showcase does not publish the complete synchronization engine, complete
WooCommerce client, SQL Server data-access implementation, production retry
logic, cache persistence implementation, orchestration loop, production logs,
or company-specific business logic. It is not intended to be cloned, configured,
and run as a complete synchronization system.

## Limitations and future improvements

This is documentation and selected illustrative code, not a production service.
Possible future case-study additions include a mock API contract, a test-data
fixture, structured observability examples, and a deployment decision record —
without exposing private implementation details.

## Privacy note

No company identifiers, production URLs, database names, credentials, API keys,
real SKUs, customer/product data, private endpoints, or local paths are included.
