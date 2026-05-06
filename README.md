# Superstore Sales & Profit Analysis

## About
End-to-end data analysis project on 9,994 rows of retail sales data 
to identify root causes of profit loss. Used Python to load data into 
SQL Server, wrote SQL queries for analysis, and built interactive 
Tableau dashboards to visualise key business insights.

## Tools & Technologies
- Python (Pandas, PyODBC) — data ingestion
- SQL Server Express / SSMS — database & querying
- Tableau Desktop — visualisation & dashboards

## Key Findings
- Tables and Machines sub-categories generate high sales but negative profit due to excessive discounting
- Consumer segment in the Central region is the highest loss driver at -$34,630
- Same Day shipping in the South region is the only loss-making shipping combination at -8.39% margin

## Project Structure
| File | Description |
|---|---|
| `Superstore.xlsx` | Source dataset (9,994 rows) |
| `load_superstore.py` | Python script to load data into SQL Server |
| `query1_discount_profit.sql` | Discount impact on profit by sub-category |
| `query2_loss_by_region.sql` | Loss-making orders by region and segment |
| `query3_shipmode_profit.sql` | Ship mode profitability by region |
| `query1_discount_profit.csv` | Query 1 results |
| `query2_loss_by_region.csv` | Query 2 results |
| `query3_shipmode_profit.csv` | Query 3 results |
| `Superstore_Analysis.twbx` | Tableau workbook with 7 sheets and 2 dashboards |

## Dashboards
- **Superstore Sales & Profit Overview** — regional sales, profit trends, sub-category performance
- **Superstore Profit Analysis** — discount impact, loss by segment, shipping profitability

## Live Dashboard
[View on Tableau Public](https://public.tableau.com/app/profile/avnisha.naugain/vizzes)
