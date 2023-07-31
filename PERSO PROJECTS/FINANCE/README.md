# CODE 1: STUDY 1 - Stock Selection and Portfolio Optimization

This code performs the following tasks:

Selects a list of ticker symbols for different stocks.
Downloads historical stock price data for the selected tickers.
Calculates the yearly dividends yield for each stock.
Interpolates the yearly dividends to get daily dividend yield.
Computes daily returns and combines them with the dividend yield to create a combined dataset.
Plots the buy (top) and sell (bottom) area for different tickers based on their returns and volatility over the specified period.
Performs portfolio optimization using the Sharpe ratio on a Monte Carlo simulation to find the optimal portfolio weights for the selected tickers.
Plots the results of the Monte Carlo simulation.

# CODE 2: STUDY 2 - Stock Price Forecasting using LSTM

This code performs the following tasks:

Downloads historical stock price data for a selected ticker.
Computes the RSI (Relative Strength Index) for the stock.
Scales the data using MinMaxScaler.
Generates input and output sequences for the LSTM model.
Fits the LSTM model to the data using a bidirectional architecture.
Generates forecasts for the future stock prices.
Organizes the results in a data frame and plots the forecasted prices.

# OVERBOUGHT-OVERSOLD AREA:

This code performs the following tasks:

Extracts stock price data from the downloaded data.
Removes noise from the data using a filter based on the moving average.
Plots the candlestick chart for the stock along with volume bars.
Plots an overbought-oversold area based on the noise-filtered stock price data.
