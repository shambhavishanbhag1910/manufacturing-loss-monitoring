import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# -----------------------------
# Basic manufacturing setup
# -----------------------------

np.random.seed(42)

plants = ["Plant_1"]

lines = ["Line_1", "Line_2", "Line_3"]

machines = {
    "Line_1": ["M01", "M02", "M03"],
    "Line_2": ["M04", "M05", "M06"],
    "Line_3": ["M07", "M08", "M09"]
}

shifts = ["A", "B", "C"]

downtime_reasons = [
    "Machine Breakdown",
    "Tool Change",
    "Material Shortage",
    "Quality Hold",
    "Setup Delay",
    "Planned Maintenance"
]

start_date = datetime(2026, 5, 1)
days = 30

# -----------------------------
# 1. Create cost master data
# -----------------------------

cost_master_records = []

for line, machine_list in machines.items():
    for machine_id in machine_list:
        downtime_cost_per_minute = np.random.randint(500, 1200)
        scrap_cost_per_unit = np.random.randint(150, 700)

        cost_master_records.append({
            "machine_id": machine_id,
            "downtime_cost_per_minute": downtime_cost_per_minute,
            "scrap_cost_per_unit": scrap_cost_per_unit
        })

cost_master_df = pd.DataFrame(cost_master_records)

cost_master_df.to_csv("data/cost_master.csv", index=False)

# -----------------------------
# 2. Create production data
# -----------------------------

production_records = []

for day in range(days):
    production_date = start_date + timedelta(days=day)

    for plant in plants:
        for line in lines:
            for machine_id in machines[line]:
                for shift in shifts:

                    planned_qty = np.random.randint(800, 1200)

                    # Actual quantity slightly lower than planned
                    actual_qty = int(planned_qty * np.random.uniform(0.82, 1.02))

                    # Rejected quantity between 1% to 8%
                    rejected_qty = int(actual_qty * np.random.uniform(0.01, 0.08))

                    good_qty = actual_qty - rejected_qty

                    production_records.append({
                        "production_date": production_date.strftime("%Y-%m-%d"),
                        "plant": plant,
                        "line": line,
                        "machine_id": machine_id,
                        "shift": shift,
                        "planned_qty": planned_qty,
                        "actual_qty": actual_qty,
                        "good_qty": good_qty,
                        "rejected_qty": rejected_qty
                    })

production_df = pd.DataFrame(production_records)

production_df.to_csv("data/production_data.csv", index=False)

# -----------------------------
# 3. Create downtime data
# -----------------------------

downtime_records = []

for day in range(days):
    event_date = start_date + timedelta(days=day)

    for plant in plants:
        for line in lines:
            for machine_id in machines[line]:
                for shift in shifts:

                    # 70% chance machine has downtime in a shift
                    has_downtime = np.random.choice([True, False], p=[0.7, 0.3])

                    if has_downtime:
                        downtime_reason = np.random.choice(downtime_reasons)

                        # More serious downtime for breakdown
                        if downtime_reason == "Machine Breakdown":
                            downtime_minutes = np.random.randint(45, 180)
                        elif downtime_reason == "Planned Maintenance":
                            downtime_minutes = np.random.randint(30, 120)
                        else:
                            downtime_minutes = np.random.randint(10, 75)

                        downtime_records.append({
                            "event_date": event_date.strftime("%Y-%m-%d"),
                            "plant": plant,
                            "line": line,
                            "machine_id": machine_id,
                            "shift": shift,
                            "downtime_reason": downtime_reason,
                            "downtime_minutes": downtime_minutes
                        })

downtime_df = pd.DataFrame(downtime_records)

downtime_df.to_csv("data/downtime_data.csv", index=False)

# -----------------------------
# Print summary
# -----------------------------

print("Data generation completed successfully.")
print("--------------------------------------")
print(f"production_data.csv rows: {len(production_df)}")
print(f"downtime_data.csv rows: {len(downtime_df)}")
print(f"cost_master.csv rows: {len(cost_master_df)}")
print("--------------------------------------")
print("Files saved inside /data folder.")