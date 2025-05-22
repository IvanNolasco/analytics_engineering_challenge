"""
main.py

Main ETL pipeline script for consolidating user, transaction, and delivery data.
Performs the following steps:

1. Extracts raw data from CSV files.
2. Transforms and cleans each dataset according to business rules.
3. Merges users with transactions and deliveries.
4. Validates the final datasets.
5. Saves the results to both CSV files and a SQLite database.

This pipeline ensures clean, analytics-ready data for downstream querying and reporting.
"""

import sys
sys.path.append('./src')

from extract import extract
from transform import transform_users, transform_transactions, transform_deliveries
from merge import merge_data
from load import validate_data, save_to_csv, save_to_sqlite

# -------------------------
# File Paths
# -------------------------
users_fp = "data/raw/user_info.csv"
transactions_fp = "data/raw/transaction_info.csv"
deliveries_fp = "data/raw/package_delivery_info.csv"

# -------------------------
# Extraction
# -------------------------
print("🔄 Extracting data...")
users_df = extract(users_fp)
transactions_df = extract(transactions_fp)
deliveries_df = extract(deliveries_fp)

# -------------------------
# Transformation
# -------------------------
print("🧹 Transforming data...")
users_df = transform_users(users_df)
transactions_df = transform_transactions(transactions_df)
deliveries_df = transform_deliveries(deliveries_df)

# -------------------------
# Merging
# -------------------------
print("🔗 Merging datasets...")
transactions_merged, deliveries_merged = merge_data(users_df, transactions_df, deliveries_df)

# -------------------------
# Validation
# -------------------------
print("✅ Validating merged data...")
validate_data(transactions_merged, primary_key_cols=['user_id', 'transaction_id'])
validate_data(deliveries_merged, primary_key_cols=['user_id', 'package_id'])

# -------------------------
# Load to CSV
# -------------------------
print("💾 Saving merged CSVs...")
save_to_csv(transactions_merged, "data/processed/transactions_merged.csv")
save_to_csv(deliveries_merged, "data/processed/deliveries_merged.csv")

# -------------------------
# Load to SQLite
# -------------------------
print("🗃️ Saving to SQLite database...")
save_to_sqlite(transactions_merged, "data/merged_data.sqlite", "user_transactions")
save_to_sqlite(deliveries_merged, "data/merged_data.sqlite", "user_deliveries")

print("🎉 ETL process completed successfully!")
