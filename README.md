# Project – Active Weight Analysis (Market Value-Based)

This project calculates the active weight of each stock in a portfolio by comparing the portfolio’s holdings with a benchmark index. The analysis is based on a snapshot of market values and does not involve return-based volatility estimation.

## Objectives

- Convert market values into portfolio weights for both SIAS and benchmark portfolios
- Calculate active weight for each asset to assess deviations from the benchmark
- Identify over- or under-weighted positions for risk management and attribution analysis

## Approach

1. **Data Loading**  
   Market value data for both the SIAS portfolio and benchmark portfolio are imported from Excel files.

2. **Weight Calculation**  
   - Each stock’s weight is calculated by dividing its market value by the total market value of the portfolio.
   - This process is repeated for both SIAS and benchmark holdings.

3. **Active Weight Calculation**  
   - Active Weight = Portfolio Weight – Benchmark Weight
   - A positive active weight indicates overweighting; a negative value indicates underweighting relative to the benchmark.

4. **Export Results**  
   The final dataset containing tickers, weights, and active weights is exported to a new Excel file.

## Tools Used

- Python 3.x
- pandas
- Excel (.xlsx) as input/output format

## Output

- An Excel file `Active_Weights.xlsx` with the following columns:
  - Ticker
  - Portfolio Weight
  - Benchmark Weight
  - Active Weight

## Key Takeaways

- Demonstrated ability to transform raw market value data into meaningful portfolio metrics
- Used Python to automate active weight comparison for performance attribution
- Focused on static (single-date) weight-based analysis suitable for snapshot risk reporting
