# AI Business Intelligence Agent using Monday.com & Google Gemini

## 📌 Project Overview

The AI Business Intelligence Agent is a Python-based application that connects to Monday.com using the GraphQL API, retrieves live business data from both the **Deals Board** and **Work Orders Board**, performs data cleaning and business analytics using Pandas, and uses Google Gemini AI to answer natural language business questions.

The system provides executives and managers with business insights, sales analytics, operational summaries, risk analysis, and AI-generated recommendations for better decision-making.

---

# 🚀 Features

### Deals Board Analytics

- Live data retrieval from Monday.com
- Total Pipeline Value
- Owner-wise Performance
- Deal Stage Analysis
- Product-wise Revenue Analysis
- Sector-wise Revenue Analysis
- Top 5 High-Value Deals
- Executive Business Summary
- Business Risk Identification
- AI-powered Business Recommendations

---

### Work Orders Board Analytics

- Live Work Orders retrieval
- Work Order Status Analysis
- Completed vs Pending Work Orders
- Engineer/Owner Workload Analysis
- Priority-wise Work Orders
- Operational Performance Summary
- AI-powered Operational Insights

---

### Artificial Intelligence Features

- Natural Language Question Answering
- Executive Summary Generation
- Business Risk Analysis
- Strategic Recommendations
- Decision Support using Google Gemini

---

# 🛠 Technologies Used

## Programming Language

- Python 3.x

## Libraries

- Pandas
- NumPy
- Requests
- python-dotenv
- Google Generative AI (Gemini)

## AI Model

- Google Gemini 3.5 Flash

## Platform

- Monday.com
- GraphQL API

---

# 📂 Project Structure

```
monday-bi-agent/
│
├── app.py
├── ai_agent.py
├── dashboard.py
├── insights.py
├── preprocessing.py
├── data_cleaning.py
├── monday_api.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ System Workflow

```
                 Monday.com

             Deals Board
                   │
                   │
             Work Orders Board
                   │
                   ▼
          GraphQL API Connection
                   │
                   ▼
          Data Retrieval (JSON)
                   │
                   ▼
        Data Cleaning (Pandas)
                   │
                   ▼
        Business Analytics Engine
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Deals Analytics      Work Orders Analytics
        │                     │
        └──────────┬──────────┘
                   ▼
          Business Dashboard
                   │
                   ▼
          Google Gemini AI
                   │
                   ▼
 Natural Language Answers,
 Business Insights,
 Risks &
 Recommendations
```

---

# 📊 Business Analytics

## Deals Analytics

The application calculates:

- Total Pipeline Value
- Deals by Owner
- Deals by Stage
- Product-wise Revenue
- Sector-wise Revenue
- Top 5 Deals
- Business Summary

---

## Work Orders Analytics

The application provides:

- Total Work Orders
- Work Order Status
- Completed Work Orders
- Pending Work Orders
- Priority Analysis
- Assigned Owner Analysis
- Operational Summary

---

# 🤖 Sample Questions

### Deals

- What is the total pipeline value?
- Which owner has the highest pipeline?
- Which sector generates the highest revenue?
- Which product contributes the most revenue?
- Which deals should management prioritize?
- What are the biggest business risks?
- Give an executive summary.

---

### Work Orders

- How many work orders are pending?
- Which engineer has the highest workload?
- Which work orders are completed?
- What is the current operational status?
- Show high-priority work orders.
- Give an operational summary.

---

# 💡 Sample Output

Question

```
Which owner has the highest pipeline?
```

Answer

```
OWNER_003 has the highest pipeline.

Business Insight

OWNER_003 contributes approximately
84.5% of the total sales pipeline.

Risk

The company is highly dependent on one owner.

Recommendation

Distribute high-value opportunities across multiple owners to reduce business risk.
```

---

# 🔒 Environment Variables

Create a `.env` file.

```
MONDAY_API_KEY=YOUR_MONDAY_API_KEY

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DEALS_BOARD_ID=YOUR_DEALS_BOARD_ID

WORK_ORDERS_BOARD_ID=YOUR_WORK_ORDERS_BOARD_ID
```

**Never upload the `.env` file to GitHub.**

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Varun-H-N/monday-bi-agent.git
```

Move into the project

```bash
cd monday-bi-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file.

Run the application

```bash
python app.py
```

---

# 🎯 Future Enhancements

- Streamlit Dashboard
- Interactive Business Charts
- PDF Report Generation
- Email Business Reports
- KPI Dashboard
- Predictive Sales Forecasting
- Voice-based Business Assistant
- Automated Weekly Reports
- Multi-Board Analytics

---

# 📚 Learning Outcomes

- GraphQL API
- Monday.com API Integration
- Data Cleaning using Pandas
- Business Intelligence
- AI Integration
- Google Gemini API
- Prompt Engineering
- Executive Dashboard Development
- Business Analytics


# 📄 License

This project is developed for educational and learning purposes.