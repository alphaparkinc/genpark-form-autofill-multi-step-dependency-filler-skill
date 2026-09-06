# GenPark AI Agent Skill - Form Autofill Multi-Step Dependency Filler

Plans topological sequential form input sequences for dependent dropdowns and conditional inputs with change event delays.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Form Field Payload & Form Schema] --> B[Dependency Graph Topological Sorter]
    B --> C[Order: Parent Dynamic Dropdown First]
    C --> D[Inject Change Event Propagation Delays]
    D --> E[Subordinate Field Execution Sequence]
```

## Features
- **Topological Cascade Resolution**: Guarantees parent dropdowns are set before child options load.
- **Zero External Dependencies**: Standard Python 3.9+ library implementation.
