import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD THE DATASET
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "sales_data.csv"

df = pd.read_csv(DATA_FILE)

print("DATASET LOADED SUCCESSFULLY")
print(df.head())

# ==========================================
# 2. PREPARE THE DATA
# ==========================================

df["date"] = pd.to_datetime(df["date"])

df["revenue"] = df["quantity"] * df["unit_price"]

df["cost"] = df["quantity"] * df["unit_cost"]

df["gross_profit"] = df["revenue"] - df["cost"]

print("\nDATA PREPARATION COMPLETE")

print(df.head())

# ==========================================
# 3. IDENTIFY REPORTING PERIODS
# ==========================================

df["period"] = df["date"].dt.to_period("M")

previous_period = pd.Period("2026-09")
current_period = pd.Period("2026-10")

previous_data = df[df["period"] == previous_period]

current_data = df[df["period"] == current_period]

print("\nREPORTING PERIODS IDENTIFIED")

print("Previous period records:", len(previous_data))
print("Current period records:", len(current_data))

# ==========================================
# 4. CALCULATE BUSINESS KPIs
# ==========================================

def calculate_kpis(data):

    total_revenue = data["revenue"].sum()

    total_orders = data["order_id"].nunique()

    gross_profit = data["gross_profit"].sum()

    average_order_value = total_revenue / total_orders if total_orders else 0

    gross_profit_margin = (
        (gross_profit / total_revenue) * 100
        if total_revenue else 0
    )

    return {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "Average Order Value": average_order_value,
        "Gross Profit": gross_profit,
        "Gross Profit Margin": gross_profit_margin
    }


previous_kpis = calculate_kpis(previous_data)

current_kpis = calculate_kpis(current_data)

print("\nPREVIOUS PERIOD KPIs")
print(previous_kpis)

print("\nCURRENT PERIOD KPIs")
print(current_kpis)

# ==========================================
# 5. COMPARE KPI PERFORMANCE
# ==========================================

kpi_rows = []

for kpi in current_kpis:

    previous_value = previous_kpis[kpi]
    current_value = current_kpis[kpi]

    if previous_value != 0:
        percentage_change = (
            (current_value - previous_value)
            / previous_value
        ) * 100
    else:
        percentage_change = 0

    difference = current_value - previous_value

    if difference > 0:
        status = "Improved"
    elif difference < 0:
        status = "Declined"
    else:
        status = "Unchanged"

    kpi_rows.append({
        "KPI": kpi,
        "Previous Period": previous_value,
        "Current Period": current_value,
        "Percentage Change": percentage_change,
        "Status": status
    })

kpi_summary = pd.DataFrame(kpi_rows)

print("\nKPI COMPARISON TABLE")

print(kpi_summary.to_string(index=False))

# ==========================================
# 6. GENERATE BUSINESS EXPLANATIONS
# ==========================================

def generate_explanation(row):

    kpi = row["KPI"]
    change = row["Percentage Change"]
    status = row["Status"]

    if status == "Unchanged":
        return f"{kpi} remained unchanged."

    if kpi == "Gross Profit Margin":
        difference = (
            row["Current Period"] - row["Previous Period"]
        )

        if difference > 0:
            return (
                f"Gross profit margin improved by "
                f"{difference:.2f} percentage points, "
                "indicating slightly better profitability."
            )
        else:
            return (
                f"Gross profit margin declined by "
                f"{abs(difference):.2f} percentage points, "
                "indicating reduced profitability."
            )

    if change > 0:
        return (
            f"{kpi} increased by {change:.2f}%, "
            "showing positive business growth."
        )
    else:
        return (
            f"{kpi} decreased by {abs(change):.2f}%, "
            "requiring management attention."
        )


kpi_summary["Explanation"] = kpi_summary.apply(
    generate_explanation,
    axis=1
)

print("\nMANAGEMENT KPI SUMMARY")

print(kpi_summary.to_string(index=False))

# ==========================================
# 7. EXPORT KPI SUMMARY
# ==========================================

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "kpi_summary.csv"

kpi_summary.to_csv(OUTPUT_FILE, index=False)

print("\nKPI REPORT GENERATED SUCCESSFULLY")

print(f"Report saved to: {OUTPUT_FILE}")
