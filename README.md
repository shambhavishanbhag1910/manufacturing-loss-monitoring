# Manufacturing Loss Monitoring using Snowflake and Grafana

## Project Overview

This project is a compact manufacturing analytics MVP built using **Snowflake** and **Grafana**.

The objective of this project is to monitor manufacturing performance by analyzing production output, machine downtime, scrap quantity, downtime cost, and scrap cost. The project converts basic shop-floor data into business KPIs that can help plant teams identify which machines, lines, or shifts are causing the highest operational and financial loss.

This project uses synthetic manufacturing data representing production, downtime, and cost master data.

---

## Business Problem

Manufacturing plants generate large amounts of operational data from production lines, machines, shifts, quality checks, and maintenance activities.

However, this data is often scattered across MES, ERP, machine logs, Excel files, and maintenance systems. Because of this, plant teams may struggle to answer simple but important questions:

- Which machine is causing the highest downtime?
- Which production line is underperforming?
- Which shift has lower quality output?
- What is the cost impact of downtime?
- What is the cost impact of scrap?
- Where is the plant losing money?

This project solves this problem by creating a Snowflake-based analytics layer and Grafana dashboards for manufacturing loss visibility.

---

## Solution

The solution follows a simple analytics flow:

```text
Synthetic Manufacturing CSV Data
        ↓
Snowflake Raw Tables
        ↓
Snowflake SQL KPI Views
        ↓
Grafana Dashboard
        ↓
Manufacturing Loss Visibility