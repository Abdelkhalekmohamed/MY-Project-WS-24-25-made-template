# Analyzing Rainforest Degradation and CO2 Emissions in the Brazilian Amazon

## Introduction
The Brazilian Amazon, often called the "lungs of the Earth," plays a critical role in global climate stability. However, it faces significant threats from deforestation and fires, which degrade its ability to absorb carbon dioxide and release large amounts of CO2, a major driver of climate change. This project explores the connection between firespot activity and carbon emissions in the Brazilian Amazon between 1999 and 2019. The goal is to uncover trends and insights to better understand the broader implications of these changes for global climate systems.

## Main Question
**How has rainforest degradation in the Brazilian Amazon contributed to carbon emissions (CO2) and climate change?**

## Data Sources
The analysis integrates three key datasets:

1. **FAOSTAT and UNFCCC Emissions Data**:
   - Metadata URL: https://www.fao.org/faostat/en/#data/GT/metadata
   - Data URL: https://bulks-faostat.fao.org/production/Emissions_Totals_E_Americas.zip
   - Description: This dataset provides annual CO2 emissions segmented by causes, such as forest fires and savanna fires, from 1999 to 2019. It combines FAOSTAT and UNFCCC data for increased granularity.
   - License: https://creativecommons.org/licenses/by/4.0/

2. **Amazon Fires Dataset (Kaggle)**:
   - Metadata URL: https://www.kaggle.com/datasets/mbogernetto/brazilian-amazon-rainforest-degradation
   - Description: Contains firespot counts in the Brazilian Amazon, highlighting temporal fire activity patterns from 1999 to 2019.
   - License: https://creativecommons.org/publicdomain/zero/1.0/

## Data Pipeline
This project includes an automated data pipeline to preprocess, clean, and merge datasets:
1. **Download Datasets**:
   - FAOSTAT emissions data is downloaded and filtered for Brazil.
   - Kaggle firespot data is retrieved using `kagglehub`.
2. **Filter and Process Data**:
   - Data is filtered for years 1999–2019.
   - Columns are standardized, missing values removed, and outliers handled.
3. **Merge Datasets**:
   - Firespot and CO2 emissions data are merged into a single dataset.
   - Firespot data is aligned proportionally to CO2 emissions for consistency.
4. **Store Processed Data**:
   - The final cleaned dataset is stored as a CSV file and in an SQLite database.

## Work Packages
1. **Data Exploration**:
   - Analyze and clean the raw datasets.
   - Investigate missing or invalid data and handle accordingly.

2. **Pipeline Development**:
   - Build an automated data pipeline for downloading, cleaning, and merging data.
   - Ensure reproducibility by logging all steps.

3. **Visualization and Analysis**:
   - Generate visualizations such as trends, scatterplots, and flowcharts to analyze data.
   - Conduct correlation analysis to explore relationships between emissions and firespots.

4. **Final Report and Presentation**:
   - Summarize findings in the final report and presentation slides.
   - Record a 10-minute presentation video highlighting the project.

## Key Findings
1. **Trends**:
   - CO2 emissions decreased significantly between 2005 and 2015, likely due to deforestation control policies.
   - Firespot activity showed a volatile pattern, with peaks in 2002 and 2004 and a decline after 2010.

2. **Correlation Analysis**:
   - A weak positive correlation (Pearson coefficient ~0.2) was found between firespot activity and CO2 emissions, indicating that fires alone do not fully explain emission variations.

3. **Broader Insights**:
   - Industrial processes, agriculture, and policy changes play significant roles in driving CO2 emissions alongside deforestation and fires.

## Limitations
- Aggregated annual data may mask finer temporal trends (e.g., monthly or seasonal).
- Other emission sources, such as industrial processes, were not separately analyzed.
- Missing or incomplete data may affect results.

## Conclusion
This project highlights the complex dynamics between firespot activity and CO2 emissions in the Brazilian Amazon. While fires contribute to emissions, other factors significantly impact the observed trends. These findings underscore the need for more detailed data and integrated approaches to tackle rainforest degradation and its environmental consequences.

## How to Run This Project
1. Place raw datasets in the `data/raw` directory.
2. Run the `data_pipeline.py` script to preprocess and clean data.
3. View processed data in `data/processed` as a CSV or SQLite database.

## License
This project is licensed under https://creativecommons.org/licenses/by/4.0/

