
Electric Vehicle (EV) Dataset Analysis
======================================

This project presents an in-depth analysis of a comprehensive dataset containing specifications and performance metrics for modern electric vehicles (EVs). The dataset, originally sourced from Kaggle, includes detailed information on various EV models, covering attributes such as:

- Manufacturer and model
- Battery capacity
- Charging time and type
- Range (WLTP, EPA, or NEDC)
- Power, torque, top speed, and acceleration
- Energy consumption
- Drive type and body style
- Market availability and pricing

Objective
---------

The goal of this analysis is to explore current trends in electric vehicle technology, performance efficiency, and market offerings. The insights are valuable for:

- Data science and machine learning experimentation
- Automotive market research
- Consumer behavior and adoption pattern analysis
- Sustainability and energy efficiency studies

Key Highlights of the Analysis
------------------------------

- Descriptive statistics to summarize core specifications across brands and regions
- Correlation analysis between range, battery size, and energy consumption
- Trend visualization of EV performance over time
- Clustering and segmentation of EVs based on features like range, price, and efficiency
- Regression modeling to predict EV performance metrics (e.g., range or price), using:
  - Linear Regression (with feature scaling)
  - Random Forest Regressor (n_estimators=100)
  - Gradient Boosting Regressor (n_estimators=100)
- Evaluation of model performance using metrics such as R², MAE, and RMSE

Tools & Libraries
-----------------

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Jupyter Notebook
- Scikit-learn (for ML applications)
- GitHub for version control and documentation
