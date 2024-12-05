import unittest
import os
import pandas as pd
import sqlite3

class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Define paths for test output files
        self.processed_data_dir = "../data/processed/"
        self.merged_data_path = os.path.join(self.processed_data_dir, "Merged_Data.csv")
        self.database_path = os.path.join(self.processed_data_dir, "data_pipeline.db")

    def test_output_files_exist(self):
        """
        Test if the required output files are created by the pipeline.
        """
        self.assertTrue(os.path.isfile(self.merged_data_path), "Merged data CSV file is missing.")
        self.assertTrue(os.path.isfile(self.database_path), "SQLite database file is missing.")

    def test_csv_content(self):
        """
        Test if the merged data CSV contains valid data and correct column names.
        """
        if os.path.isfile(self.merged_data_path):
            merged_data = pd.read_csv(self.merged_data_path)
            self.assertGreater(len(merged_data), 0, "Merged data CSV is empty.")
            self.assertIn("Year", merged_data.columns, "CSV is missing 'Year' column.")
            self.assertIn("Emissions", merged_data.columns, "CSV is missing 'Emissions' column.")
            self.assertIn("firespots", merged_data.columns, "CSV is missing 'firespots' column.")
            self.assertIn("Reasons of Emission", merged_data.columns, "CSV is missing 'Reasons of Emission' column.")
            self.assertNotIn("Unit", merged_data.columns, "CSV should not have 'Unit' column.")

    def test_sqlite_content(self):
        """
        Test if the SQLite database contains the required table and data.
        """
        if os.path.isfile(self.database_path):
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()
            
            # Check if the table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='MergedData';")
            table_exists = cursor.fetchone()
            self.assertIsNotNone(table_exists, "Table 'MergedData' is missing in SQLite database.")

            # Check if the table has data
            merged_data = pd.read_sql_query("SELECT * FROM MergedData", conn)
            conn.close()
            self.assertGreater(len(merged_data), 0, "SQLite table 'MergedData' is empty.")
            self.assertIn("Year", merged_data.columns, "Table is missing 'Year' column.")
            self.assertIn("Emissions", merged_data.columns, "Table is missing 'Emissions' column.")
            self.assertIn("firespots", merged_data.columns, "Table is missing 'firespots' column.")
            self.assertIn("Reasons of Emission", merged_data.columns, "Table is missing 'Reasons of Emission' column.")
            self.assertNotIn("Unit", merged_data.columns, "Table should not have 'Unit' column.")

    def test_firespots_proportionality(self):
        """
        Test if firespots are distributed proportionally across rows within the same year.
        """
        if os.path.isfile(self.merged_data_path):
            merged_data = pd.read_csv(self.merged_data_path)

            # Group by Year and sum firespots
            firespots_sum_by_year = merged_data.groupby("Year")["firespots"].sum().to_dict()

            # Verify that firespots in the merged dataset match the expected totals from Amazon Fires data
            amazon_fires_path = os.path.join(self.processed_data_dir, "Amazon_Fires.csv")
            if os.path.isfile(amazon_fires_path):
                amazon_fires_data = pd.read_csv(amazon_fires_path)
                expected_firespots = amazon_fires_data.set_index("year")["firespots"].to_dict()

                for year, total_firespots in firespots_sum_by_year.items():
                    self.assertAlmostEqual(
                        total_firespots, 
                        expected_firespots.get(year, 0), 
                        delta=0.01,  # Allow for minor rounding differences
                        msg=f"Firespot total mismatch for year {year}."
                    )

if __name__ == "__main__":
    unittest.main()

