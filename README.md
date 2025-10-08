# Amazon_BabyProduct_Sentiment_Analysis

## Overview

This project focuses on building a sentiment forecasting system for Amazon baby product reviews, specifically targeting thermometer products. The goal is to help online sellers understand how their products are performing over time without manually reading thousands of reviews. Since star ratings often fail to capture the true sentiment expressed in text, this project emphasizes text-based sentiment analysis and forecasting future sentiment trends.

I have performed sentiment analysis on the Amazon Baby Products dataset.  
First, basic preprocessing was performed. Then, the second most-reviewed product was selected, and the following key steps were applied.

### Key Steps

- Applied **RoBERTa** for sentiment analysis  
- Applied a **summarizer** to sentences containing more than 100 words  
- Used a **stacked LSTM** model for sentiment forecasting  

## Details

The **RoBERTa** model was used to classify each review into *positive*, *negative*, or *neutral* sentiments and to generate corresponding probabilities. To make the model more domain-specific, I fine-tuned RoBERTa on a manually annotated subset of 300 reviews, improving the F1-score to **0.75** and accuracy to **82%**. This fine-tuned model enabled large-scale automated classification of customer feedback.  

Once sentiments were obtained, they were treated as time series data for forecasting. Initially, statistical models like **ARIMA** were tested, but they failed to capture long-term dependencies. Therefore, a **stacked LSTM** model was developed and optimized using **KerasTuner**, which reduced RMSE by over **90%** and MAE by **88%** compared to ARIMA. This deep learning approach provided a robust method to predict future customer sentiment trends.

## Evaluation

Since this is a regression problem (forecasting sentiment probabilities), regression metrics were used for evaluation:

- **Mean Squared Error (MSE)**  
- **Mean Absolute Error (MAE)**  
- **R² Score**  
- **Root Mean Squared Error (RMSE)**  
