import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the merged data
merged_data_path = "../data/processed/Merged_Data.csv"
merged_data = pd.read_csv(merged_data_path)

# Ensure the data is loaded successfully
if merged_data.empty:
    print("Merged data is empty. Check the data pipeline.")
else:
    print("Merged data loaded successfully.")

# Aggregate total emissions and firespots by year
yearly_data = merged_data.groupby("Year", as_index=False).agg({
    "Emissions": "sum",
    "firespots": "sum"
})

# Ensure visualization directory exists
visualizations_dir = "../data/processed/visualizations/"
os.makedirs(visualizations_dir, exist_ok=True)

# 1. Line Plot: CO2 Emissions Over Time
plt.figure(figsize=(10, 6))
plt.plot(yearly_data["Year"], yearly_data["Emissions"], color="blue", linewidth=2, label="Total CO2 Emissions")
plt.title("Trends in Total CO2 Emissions (1999-2019)")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (metric tons)")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(visualizations_dir, "co2_emissions_trends.png"))
plt.show()

# 2. Line Plot: Firespots Over Time
plt.figure(figsize=(10, 6))
plt.plot(yearly_data["Year"], yearly_data["firespots"], color="red", linewidth=2, label="Total Firespots")
plt.title("Trends in Total Firespots (1999-2019)")
plt.xlabel("Year")
plt.ylabel("Firespots")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(visualizations_dir, "firespots_trends.png"))
plt.show()

# 3. Combined Trends of Emissions and Firespots
plt.figure(figsize=(10, 6))
plt.plot(yearly_data["Year"], yearly_data["Emissions"], label="Total CO2 Emissions", color="blue", linewidth=2)
plt.plot(yearly_data["Year"], yearly_data["firespots"], label="Total Firespots", color="red", linestyle="--", linewidth=2)
plt.title("Trends of Emissions and Firespots Over Time")
plt.xlabel("Year")
plt.ylabel("Counts (Metric Tons / Firespots)")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(visualizations_dir, "combined_trends.png"))
plt.show()

# 4. Scatterplot: Correlation Between Total Emissions and Firespots
plt.figure(figsize=(8, 6))
sns.scatterplot(data=yearly_data, x="firespots", y="Emissions", color="green", s=100)
plt.title("Correlation Between Total Emissions and Firespots")
plt.xlabel("Total Firespots")
plt.ylabel("Total CO2 Emissions (metric tons)")
plt.grid(True)
plt.savefig(os.path.join(visualizations_dir, "correlation_emissions_firespots.png"))
plt.show()
