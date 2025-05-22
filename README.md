
# 📦 Data Analytics Engineering Challenge  
**Victor Nolasco**

This repository presents a complete solution to a real-world Data Analytics Engineering challenge. It demonstrates how to design, implement, and document a clean and modular ETL pipeline that consolidates diverse datasets into analysis-ready tables and answers strategic business questions using SQL.

---

## 🧠 Challenge Overview

You are provided with three independent datasets in CSV format:
- **User Information**
- **Transactional Information**
- **Package Delivery Information**

### 🎯 Requirements

1. **Explore the data**  
   - Create a **data dictionary** and **UML diagram** to define the schema and relationships

2. **Build a merged dataset**  
   - Standardize date formats to `YYYY-MM-DD`
   - Localize timestamps to **Mexico City time**
   - Round numeric fields to two decimal places
   - Truncate text fields to a maximum of 256 characters

3. **Design and justify a DAG**  
   - Explain whether to use **ETL** or **ELT**
   - Describe which pipeline stage deserves the most attention and why

4. **Answer analytical questions** using SQL:
   - How many users are there in total?
   - How many users have transacted?
   - What is the card delivery rate?
   - Which is the most efficient package carrier?
   - Which are the top 10 categories with the most transactions?

---

## 🧭 Solution Strategy

To address the challenge, I followed these structured steps:

1. **Exploration & Profiling**:  
   - Performed initial inspection in a Jupyter notebook
   - Identified data quality issues (e.g., inconsistent formats, duplicates)

2. **Schema Design**:  
   - Documented each dataset in a data dictionary
   - Created a UML diagram to visualize table relationships

3. **ETL Design and Development**:  
   - Designed a modular ETL DAG to represent the pipeline architecture
   - Wrote modular Python scripts to extract, clean, and merge the data
   - Implemented validation and transformation logic
   - Loaded the outputs into both CSV and SQLite

4. **SQL Analysis**:  
   - Wrote queries to answer the business questions using the final database

---

## 📂 Project Structure

```
.
├── data/
│   ├── raw/                 # Original CSVs
│   ├── processed/           # Cleaned & merged CSVs
│   └── merged_data.sqlite   # Final SQLite database
├── src/                     # Modular ETL scripts
│   ├── extract.py
│   ├── transform.py
│   ├── merge.py
│   └── load.py
├── notebooks/
│   └── exploration.ipynb    # Data profiling
├── sql/
│   └── sql_queries.md       # Analytical SQL with answers
├── docs/
│   ├── ETL_DAG.png
│   └── ER_UML.png
├── data_dictionary.md
├── main.py
├── requirements.txt
└── README.md
```

---

## 📘 Data Dictionary

See [`data_dictionary.md`](data_dictionary.md) for a full column-by-column description, including:
- Data types
- Primary/foreign keys
- Business meaning
- Format issues and fixes

---

## 📐 UML Diagram

The UML diagram outlines the relationships between:
- `users` → `transactions` (1:N)
- `users` → `deliveries` (1:N)

📍 View: [`docs/ER_UML.png`](docs/ER_UML.png)

---

## 🔄 ETL Pipeline Summary

**Extract**:  
- Load CSVs with Pandas

**Transform**:  
- Clean column formats (dates, timestamps, strings)
- Deduplicate based on primary keys
- Validate schema rules
- Join users to each fact table

**Load**:  
- Save outputs to processed CSVs and a SQLite database

Each script (`src/`) is reusable and testable.  
The DAG visually represents this modular flow.

⚠️ While the DAG diagram (below) shows a professional, task-based orchestration structure (ideal for tools like Prefect), the actual implementation is kept simple and script-driven, aligning well with the scope of the challenge while still reflecting production-ready modularity.

---

## 🧠 Why Two Tables Instead of One?

Although the challenge asked for a “merged dataset,” I chose to produce **two separate merged tables**:

- `user_transactions`: combines users with their transactions
- `user_deliveries`: combines users with their deliveries

This design follows **data modeling best practices**:
- **Avoids NULL bloat**: many users may have transactions but no deliveries (or vice versa)
- **Keeps each table semantically consistent**: one for financial behavior, one for logistics
- **Improves flexibility**: allows for targeted analysis (e.g., delivery metrics alone)
- **Aligns with normalized schema design**: simpler joins and cleaner SQL

---

## 📊 DAG Explanation

The DAG separates processing into two parallel branches:
- One for merging **user + transaction**
- Another for **user + delivery**

This approach:
- Enhances modularity and reusability
- Enables independent validation and debugging
- Reflects the schema and data model
- Would support parallelization in a production workflow

📍 See DAG: [`docs/ETL_DAG.png`](docs/ETL_DAG.png)

---

## 🧩 ETL vs ELT

I chose an **ETL** approach over ELT for the following reasons:

- The source data is flat files (not queryable)
- Transformation logic is non-trivial and needs to happen before loading
- SQLite is not suitable for in-database transformation
- Loading raw, unclean data would create redundancy and noise

Transforming data **before loading** guaranteed that the final SQLite database was clean, reliable, and ready for analysis.

---

## ✅ SQL Analysis

SQL queries were executed against the merged tables in SQLite to answer:

- Total number of users
- Number of users who transacted
- Card delivery rate
- Most efficient courier
- Top 10 transaction categories

See: [`sql/sql_queries.md`](sql/sql_queries.md)

---

## 🚀 How to Run the Project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the full ETL pipeline:

```bash
python main.py
```

3. Explore the resulting data:
- CSV outputs in `data/processed`
- SQLite file in `data/merged_data.sqlite`

---

## 🙌 Final Notes

This project simulates a realistic analytics engineering workflow:
- Modular, validated ETL pipeline
- Clear transformation rules
- Clean, well-modeled final outputs
- SQL logic that answers real business questions
- Documentation to support clarity and future scalability

Feel free to fork the repo, adapt the pipeline, or reach out with questions!
