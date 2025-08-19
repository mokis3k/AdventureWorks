# AdventureWorks – Sales & Customer Segmentation Analysis  

## Project Overview  
This project explores the **AdventureWorks** dataset provided by Microsoft, which simulates the operations of a bicycle shop.  
The goal was to analyze **sales performance for August 2013**, identify seasonal trends, and segment customers based on purchasing behavior.  

The analysis was conducted using:  
- **Power BI** for data visualization  
- **Python (pandas, scikit-learn)** for customer segmentation  

---

## Dataset  
The dataset is available from Microsoft: [AdventureWorks Sample Database](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms).  

It contains detailed information about:  
- Customers  
- Orders & Sales transactions  
- Products & Product categories  
- Resellers & Sales representatives  
- Geography & Territories  

---

## 🔎 Analysis Workflow  

### 1. Data Preparation  
- Cleaned and transformed raw data.  
- Created calculated metrics required for sales analysis.  

### 2. Sales Analysis (August 2013)  
- Built a **Power BI dashboard** with key metrics and visualizations.  
- Findings:  
  - Drop in **units sold** and **average check**.  
  - Growth in **unique customers** and **number of orders**.  
  - Seasonal revenue decline confirmed by comparing with **August 2012** trend.  

### 3. Customer Segmentation  
- Created a customer-level dataset in **Power Query** with the following features:  
  - `CustomerID`, `TotalQuantity`, `TotalRevenue`, `OrderCount`, `CategoryCount`, `AvgCheck`, `RecencyDays`  
- Applied clustering in **Python** using `pandas` and `scikit-learn`.  
- Segments obtained:  
  - **Least Valuable**  
  - **Frequent Buyers**  
  - **Premium**  

### 4. Customer Segmentation Dashboard  
- Built a second **Power BI page** focusing on customer clusters.  
- Helped the business identify customer behavior patterns during seasonal revenue drops.  

---

## Dashboard Visualizations  

| **Dashboard Page** | **Visualization** | **Description** |
|---------------------|-------------------|-----------------|
| **Total Sales Dashboard** | Revenue overview block | Total monthly revenue with MoM and YoY changes, plus line chart comparing 2012 vs 2013 trends. |
| | KPI changes | Key metrics showing unique customers, order count, total units sold, and average check. |
| | Monthly revenue by category | Bar chart of monthly revenue split by product category with MoM % change. |
| | Regional revenue comparison | Column chart comparing this month’s regional revenue vs previous month. |
| **Customer Segmentation** | Segment overview block | Customer segments (Least Valuable, Premium, Frequent Buyers) with descriptions and MoM changes. |
| | Revenue & Units by segment | Column chart showing average monthly revenue and sold units split by customer segments. |
| | Customers by territory | Bar chart showing change in number of customers in each segment across territories. |


---

## Tech Stack  
- **Database:** MS SQL Server  
- **Data Analysis & Cleaning:** Power Query, Python (pandas)  
- **Machine Learning:** scikit-learn (clustering)  
- **Data Visualization:** Power BI  

---

## Key Outcomes  
- Identified **seasonal sales decline** in August 2013.  
- Segmented customers into **three clusters** for better targeting.  
- Built interactive dashboards providing **actionable insights** for business strategy during seasonal downturns.  

---
