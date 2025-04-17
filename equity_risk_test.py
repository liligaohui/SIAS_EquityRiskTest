import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf
import numpy as np

# Part 1: Active Weight Calculation

sias_df = pd.read_excel("SIAS_portfolio.xlsx")
bm_df = pd.read_excel("BM_portfolio.xlsx")

sias_df['Portfolio_Weight'] = sias_df['Market_Value'] / sias_df['Market_Value'].sum()
bm_df['Benchmark_Weight'] = bm_df['Market_Value'] / bm_df['Market_Value'].sum()

merged = pd.merge(sias_df[['Ticker', 'Portfolio_Weight']],
                  bm_df[['Ticker', 'Benchmark_Weight']],
                  on='Ticker', how='outer').fillna(0)
merged['Active_Weight'] = merged['Portfolio_Weight'] - merged['Benchmark_Weight']

merged.to_excel("Active_Weights.xlsx", index=False)
print("Active weight calculation completed. Output saved to 'Active_Weights.xlsx'.")


# Part 2: Annualized Volatility and Portfolio Volatility

# # Step 1: Define date range
# end_date = datetime.today().strftime('%Y-%m-%d')
# start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

# # Step 2: Load tickers
# df = pd.read_excel("SIAS_portfolio.xlsx")
# tickers = df['Ticker'].dropna().unique().tolist()

# # Step 3: Download price data
# data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
# returns = data.pct_change().dropna()

# # Step 4: Individual annualized volatilities
# volatility = returns.std() * (252 ** 0.5)
# volatility = volatility.rename("1Y_Annualized_Volatility")

# # Step 5: Merge volatility back into portfolio data
# df = df.merge(volatility, left_on='Ticker', right_index=True, how='left')

# # Step 6: Filter only valid tickers (downloaded successfully)
# valid_tickers = returns.columns
# df_valid = df.set_index('Ticker').loc[valid_tickers]

# # Step 7: Recalculate weights using only valid tickers
# weights = df_valid['Market_Value'] / df_valid['Market_Value'].sum()

# # Step 8: Portfolio covariance matrix
# cov_matrix = returns[valid_tickers].cov() * 252

# # Step 9: Portfolio volatility calculation
# portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
# print(f"Estimated portfolio annualized volatility: {portfolio_vol:.4%}")

# # Step 10: Save result
# df.to_excel("SIAS_with_volatility.xlsx", index=False)
