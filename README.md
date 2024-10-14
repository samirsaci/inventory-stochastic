## Inventory Management for Retail — Stochastic Demand 📈
*Simulate the impact of safety stock level on inventory management performance metrics assuming a normal distribution of your demand*

<p align="center">
  <img align="center" src="https://miro.medium.com/max/1280/1*qd_L-_YIZwrgwvt9WHkk-w.png">
</p>

For most retailers, inventory management systems take a fixed, rule-based approach to forecast and replenishment orders management.

Considering the distribution of the demand, the objective is to build a replenishment policy that will minimize your ordering, holding and shortage costs.

### Article
In this [Article](https://towardsdatascience.com/inventory-management-for-retail-stochastic-demand-3020a43d1c14), we will improve this model and introduce a simple methodology using a discrete simulation model 
built with Python to test several inventory management rules assuming a normal distribution of the customer demand.

### Problem Statement
As an Inventory Manager of a mid-size retail chain, you are in charge of setting the replenishment quantity in the ERP.

Based on the feedbacks of the store manager, you start to doubt that the replenishment rules of the ERP are the most optimal especially for the fast runners because your stores are facing lost sales due to stock-outs.

For each SKU, you would like to build a simple simulation model to test several inventory rules and estimate the impact on:
- Performance Metrics
- Cycle Service Level (CSL): probability to have a stock-out for each cycle (%)
- Item Fill Rate (IFR): percentage of customer demand met without stock-out (%)

### Question
What does impact your logistic performance?

### Data set
This analysis will be based on the M5 Forecasting dataset of Walmart stores sales records ([Link](
https://www.kaggle.com/c/m5-forecasting-accuracy)).

## Code
This repository code you will find all the code used to explain the concepts presented in the article.

## About me 🤓
Senior Supply Chain and Data Science consultant with international experience working on Logistics and Transportation operations. \
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://wwww.logi-green.com/). \

Please have a look at my personal blog: [Personal Website](https://samirsaci.com)

