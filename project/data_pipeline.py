import os
import pandas as pd
import kagglehub
import urllib.request
import zipfile

# Define the processed data directory
processed_data_dir = "../data/processed/"
faostat_cleaned_path = os.path.join(processed_data_dir, "FAOSTAT_cleaned.csv")
amazon_fires_cleaned_path = os.path.join(processed_data_dir, "Amazon_Fires_cleaned.csv")

# Ensure processed data directory exists
os.makedirs(processed_data_dir, exist_ok=True)

# Step 1: Download and process FAOSTAT Emissions data
print("Downloading FAOSTAT data...")
faostat_url = "https://bulks-faostat.fao.org/production/Emissions_Totals_E_Americas.zip"
faostat_zip_path = "Emissions_Totals_E_Americas.zip"  # Temporary ZIP file to hold the download
urllib.request.urlretrieve(faostat_url, faostat_zip_path)
print("FAOSTAT data downloaded.")

# Extract the downloaded ZIP file and process the data
with zipfile.ZipFile(faostat_zip_path, 'r') as zip_ref:
    zip_ref.extractall(".")

# Assuming the extracted CSV file is named "Emissions_Totals_E_Americas.csv"
faostat_data = pd.read_csv("Emissions_Totals_E_Americas.csv")

# Print columns to verify column names
print("Columns in FAOSTAT data:", faostat_data.columns)

# Check for 'Area' column and dynamically handle year columns
if "Area" in faostat_data.columns:
    # Filter data to include only rows for Brazil
    faostat_brazil = faostat_data[faostat_data["Area"] == "Brazil"]
    
    # Select year columns (e.g., "Y1999", "Y2000", etc.) within 1999 to 2019, ignoring any non-numeric suffixes
    year_columns = [col for col in faostat_brazil.columns if col.startswith('Y') and col[1:].isdigit() and 1999 <= int(col[1:]) <= 2019]
    
    # Melt the DataFrame to reshape year columns into rows
    faostat_melted = faostat_brazil.melt(id_vars=["Area"], value_vars=year_columns,
                                         var_name="Year", value_name="Value")
    
    # Clean the "Year" column to remove the "Y" prefix and convert to integer
    faostat_melted["Year"] = faostat_melted["Year"].str[1:].astype(int)
    
    # Drop the "Area" column as it's no longer needed
    faostat_cleaned = faostat_melted[["Year", "Value"]]
    
    # Save the cleaned FAOSTAT data
    faostat_cleaned.to_csv(faostat_cleaned_path, index=False)
    print("FAOSTAT data processed and saved to processed directory.")
else:
    print("The expected column 'Area' was not found in the FAOSTAT data. Please check the data format.")

# Step 2: Download and process the Kaggle dataset for Amazon Fires
print("Downloading Brazilian Amazon Rainforest dataset from Kaggle...")
path = kagglehub.dataset_download("mbogernetto/brazilian-amazon-rainforest-degradation")
print("Path to dataset files:", path)

# Load the specific CSV from the Kaggle dataset path and process it
amazon_fires_path = os.path.join(path, "inpe_brazilian_amazon_fires_1999_2019.csv")
amazon_fires_data = pd.read_csv(amazon_fires_path)
amazon_fires_filtered = amazon_fires_data[["year", "latitude", "longitude", "firespots"]]
amazon_fires_filtered.to_csv(amazon_fires_cleaned_path, index=False)
print("Amazon Fires data processed and saved to processed directory.")

# Cleanup: remove the temporary FAOSTAT ZIP file and any extracted CSV files
temp_files = [
    faostat_zip_path,
    "Emissions_Totals_E_Americas.csv",
    "Emissions_Totals_E_Americas_NOFLAG.csv",
    "Emissions_Totals_E_AreaCodes.csv",
    "Emissions_Totals_E_Elements.csv",
    "Emissions_Totals_E_Flags.csv",
    "Emissions_Totals_E_ItemCodes.csv",
    "Emissions_Totals_E_Sources.csv"
]

for file in temp_files:
    if os.path.exists(file):
        os.remove(file)

print("Data pipeline completed successfully, and temporary files cleaned up.")