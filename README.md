## Inventory Management for Retail — Stochastic Demand 📈
*Simulate the impact of safety stock level on inventory management performance metrics, assuming a normal distribution of your demand*

<p align="center">
  <a href="https://www.samirsaci.com/inventory-management-for-retail-stochastic-demand-2/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://miro.medium.com/max/1280/1*qd_L-_YIZwrgwvt9WHkk-w.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

For most retailers, inventory management systems adopt a fixed, rule-based approach to forecasting and order replenishment.

Given the demand distribution, the objective is to develop a replenishment policy that minimises ordering, holding, and shortage costs.

### Article
In this [Article](https://www.samirsaci.com/inventory-management-for-retail-stochastic-demand-2/), we will improve this model and introduce a simple methodology using a discrete simulation model 
built with Python to test several inventory management rules, assuming a normal distribution of the customer demand.

### Youtube Video
Click on the image below to access the video tutorial that explains the concept behind this solution
<div align="center">
  <a href="https://www.youtube.com/watch?v=1oRebt_Q0dY"><img src="https://i.ytimg.com/vi/1oRebt_Q0dY/hqdefault.jpg" alt="Too Much Stock or Empty Shelves: Python Finds the Middle"></a>
</div>

### Problem Statement
As an Inventory Manager at a mid-sized retail chain, you are responsible for setting replenishment quantities in the ERP.

Based on the store manager's feedback, you begin to doubt that the ERP replenishment rules are optimal, particularly for fast-moving items, as your stores are experiencing lost sales due to stockouts.

For each SKU, you would like to build a simple simulation model to test several inventory rules and estimate the impact on:
- Performance Metrics
- Cycle Service Level (CSL): probability to have a stock-out for each cycle (%)
- Item Fill Rate (IFR): percentage of customer demand met without stock-out (%)

### Question
What impacts your logistic performance?

### Data set
This analysis will be based on the M5 Forecasting dataset of Walmart stores' sales records ([Link](https://www.kaggle.com/competitions/m5-forecasting-accuracy)).

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

### Files
- `Inventory Management - Stochastic.ipynb` - Jupyter notebook with step-by-step analysis
- `inventory_stochastic.py` - Standalone Python script

### Getting Started
```bash
pip install -r requirements.txt
python inventory_stochastic.py
```

### Dependencies
- pandas
- matplotlib
- numpy
- scipy
- seaborn
- statsmodels


## Go further

- **The full write-up, with the reasoning behind the code:** [Inventory Management for Retail — Stochastic Demand](https://www.samirsaci.com/inventory-management-for-retail-stochastic-demand-2/?utm_source=github&utm_medium=readme&utm_campaign=inventory-stochastic)
- **The video:** [Too Much Stock or Empty Shelves: Python Finds the Middle](https://youtu.be/1oRebt_Q0dY)
- **Test what you learned:** the [Supply Science App](https://supply-science.com/?utm_source=github&utm_medium=readme&utm_campaign=inventory-stochastic) has lessons and quizzes on inventory management, free and in the browser.
- **100+ case studies with their source code:** [samirsaci.com](https://www.samirsaci.com/?utm_source=github&utm_medium=readme&utm_campaign=inventory-stochastic)

## About me

Samir Saci, supply chain engineer and data scientist with ten years in operations across Asia and Europe. Founder of [LogiGreen](https://www.logi-green.com/), creator of [Supply Science](https://www.youtube.com/@SupplyScience).
For consulting on analytics and sustainable supply chain transformation: [LogiGreen](https://www.logi-green.com/). More about me: [samirsaci.com/about](https://www.samirsaci.com/about/) · [LinkedIn](https://www.linkedin.com/in/samir-saci/)

