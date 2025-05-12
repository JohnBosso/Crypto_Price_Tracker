# Cryptocurrency Price Tracker using CoinMarketCap API

This project fetches real-time cryptocurrency data from the CoinMarketCap API and performs analysis on percentage price changes over time. It includes data visualization using `seaborn` and `matplotlib`, helping users gain quick insights into market movements.

## Features

- Fetches the latest prices for the top 15 cryptocurrencies in USD  
- Aggregates data across multiple time intervals (1h, 24h, 7d, 30d, 60d, 90d)  
- Plots average percent changes using Seaborn point plots  
- Visualizes Bitcoin price trends over time with a line plot  

## Technologies Used

- Python  
- CoinMarketCap API  
- pandas  
- requests  
- seaborn  
- matplotlib  

## How It Works

1. Connects to the CoinMarketCap API using a session-based request.  
2. Normalizes and appends live data into a DataFrame.  
3. Groups and reshapes the data for trend visualization.  
4. Displays comparative plots across selected cryptocurrencies.  

## API Key

To use this script, replace the API key in the code with your own from [CoinMarketCap Developer Portal](https://coinmarketcap.com/api/).
