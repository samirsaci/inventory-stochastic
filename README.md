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
This analysis will be based on the M5 Forecasting dataset of Walmart stores' sales records ([Link](https://www.kaggle.com/c/m5-forecasting-accuracy)).

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

## About me 🤓
Senior Supply Chain and Data Science consultant with international experience working on Logistics and Transportation operations.\
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://www.logi-green.com/)\
Please have a look at my personal blog: [Personal Website](https://samirsaci.com)

