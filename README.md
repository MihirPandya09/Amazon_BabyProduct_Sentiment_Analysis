# Amazon_BabyProduct_Sentiment_Analysis

## Overview

I have performed sentiment analysis on the Amazon Baby Products dataset.

- First, basic preprocessing was performed.  
- Then, the second most-reviewed product was selected, and the following key steps were applied.

### Key Steps:

- Applied **RoBERTa** for sentiment analysis  
- Applied a **summarizer** to sentences containing more than 100 words  
- Used a **stacked LSTM** model for sentiment forecasting  

## Details

- **RoBERTa** provides probabilities for *positive*, *negative*, and *neutral* sentiments.  
- After that, a **stacked LSTM** model is applied to forecast sentiment trends accordingly.

## Evaluation

### Since this is a regression problem, regression metrics were used for evaluation:

- Mean Squared Error (MSE)  
- Mean Absolute Error (MAE)  
- R² Score  
- Root Mean Squared Error (RMSE)

