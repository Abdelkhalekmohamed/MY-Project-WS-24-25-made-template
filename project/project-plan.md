### **Project Plan**

#### **Title**
Deforestation and Carbon Emissions in the Amazon - MADE Project

---

#### **Main Question**
How has rainforest degradation in the Brazilian Amazon contributed to carbon emissions (CO2) and climate change?

---

#### **Description**
The Brazilian Amazon, known as the "lungs of the Earth," plays a crucial role in global climate stability. However, it faces escalating threats from deforestation and fire activity, which degrade its carbon absorption capacity and release substantial amounts of CO2, exacerbating climate change.  

This project investigates the relationship between firespot activity and CO2 emissions in the Brazilian Amazon from 1999 to 2019. The study focuses on:  
- Analyzing trends in firespot activity and emissions.  
- Correlating these trends to understand their interplay.  
- Highlighting the broader implications for climate systems and policy.  

The analysis aims to uncover insights into the environmental consequences of deforestation and contribute to sustainable forest management strategies.

---

#### **Datasources**

1. **FAOSTAT and UNFCCC Emissions Data**  
   - **Metadata URL**: [https://www.fao.org/faostat/en/#data/GT/metadata](https://www.fao.org/faostat/en/#data/GT/metadata)  
   - **Data URL**: [https://bulks-faostat.fao.org/production/Emissions_Totals_E_Americas.zip](https://bulks-faostat.fao.org/production/Emissions_Totals_E_Americas.zip)  
   - **Data Type**: CSV  
   - **Description**:  
     This dataset provides CO2 emissions data segmented by sources (e.g., forest fires, savanna fires) from 1999 to 2019. It integrates FAOSTAT and UNFCCC data for comprehensive coverage, filtered to include only Brazil and aligned with Amazon firespot data.  
   - **Structure**:  
     Tabular format with columns for emission sources, years, and CO2 values (metric tons).  
   - **Licensing**:  
     Licensed under **CC BY 4.0 International**. Attribution to UNFCCC and FAOSTAT is maintained.  
     [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

2. **Amazon Fires Dataset (Kaggle)**  
   - **Metadata URL**: [Brazilian Amazon Rainforest Degradation 1999-2019](https://www.kaggle.com/datasets/mbogernetto/brazilian-amazon-rainforest-degradation)  
   - **Data URL**: Not applicable (downloaded using KaggleHub).  
   - **Data Type**: CSV  
   - **Description**:  
     This dataset records firespot counts in the Brazilian Amazon from 1999 to 2019, highlighting temporal patterns in fire activity.  
   - **Structure**:  
     Tabular format with columns for years and firespot counts.  
   - **Licensing**:  
     Licensed under **CC0 1.0 Universal**.  
     [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)

---

#### **Work Packages**

1. **Data Collection and Preparation**  
   - **Description**: Download and organize datasets for analysis.  
   - **Tasks**:  
     1. Download FAOSTAT emissions and Kaggle Amazon Fires datasets.  
     2. Validate and store datasets in a structured directory.  

2. **Initial Data Exploration**  
   - **Description**: Inspect datasets for structure, missing values, and initial patterns.  
   - **Tasks**:  
     1. Load and preview datasets to identify inconsistencies.  
     2. Document initial observations for subsequent cleaning steps.  

3. **Data Cleaning**  
   - **Description**: Standardize datasets and handle inconsistencies.  
   - **Tasks**:  
     1. Align formats, standardize variable names, and normalize units.  
     2. Address missing or zero-value data points.  

4. **Data Analysis and Integration**  
   - **Description**: Analyze trends and correlations between firespot activity and emissions.  
   - **Tasks**:  
     1. Filter and integrate datasets for Brazil-specific data.  
     2. Perform correlation analysis to explore relationships between emissions and firespots.  

5. **Data Visualization**  
   - **Description**: Present findings using graphs and visual aids.  
   - **Tasks**:  
     1. Create time-series graphs and scatterplots to highlight trends.  
     2. Annotate visualizations to emphasize key findings.  

6. **Final Report**  
   - **Description**: Compile a comprehensive report summarizing the study.  
   - **Tasks**:  
     1. Write a detailed report covering methods, results, and insights.  
     2. Include visualizations and actionable recommendations for forest management.  

