# SMA Crossover Backtest (Python)

A clean, **quant-trading** starter to backtest a **Simple Moving Average (SMA) crossover** strategy with transaction costs and slippage. 
Includes a **parameter grid search** with a Sharpe heatmap. Offline-friendly (can synthesize data) and plug-and-play with `yfinance` for live historical pulls.

---

## 🚀 Features
- SMA **fast/slow** crossover (default 50/200)
- Transaction **costs** (bps) + **slippage** (bps per edge)
- Metrics: **Total Return, CAGR, Sharpe, Max Drawdown, Win Rate, #Trades, Avg Trade**
- **Grid search** for (fast, slow) with a Sharpe **heatmap**
- Offline mode (synthetic GBM) if market data unavailable
- Minimal dependencies and clear code structure

```
sma-crossover-backtest/
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── strategy.py
├── main.py                # single backtest run
├── grid_search.py         # parameter sweep + heatmap
├── reports/               # CSV outputs
└── figures/               # saved plots
```

---

## 🛠 Installation
```bash
git clone <your-repo-url>.git
cd sma-crossover-backtest
python -m venv .venv && source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📈 Quick Start

### 1) Single backtest
Run SMA(50/200) on SPY since 2015. Set `--offline` to synthesize data when offline.
```bash
python main.py --ticker SPY --start 2015-01-01 --end 2025-01-01 --fast 50 --slow 200 --offline
```
**Outputs**
- `reports/report.csv` — metrics table
- `figures/equity_curve.png` — equity vs. buy & hold

### 2) Parameter sweep (Sharpe heatmap)
```bash
python grid_search.py --ticker SPY --start 2015-01-01 --end 2025-01-01 --fast_range 10,20,30,50,100 --slow_range 100,150,200,250,300 --offline
```
**Outputs**
- `reports/grid_search.csv` — all (fast, slow) results
- `figures/grid_sharpe_heatmap.png` — Sharpe heatmap

---

## 📊 Metrics Explained
- **Total Return:** Growth of $1 – 1
- **CAGR:** Annualized return from equity curve
- **Sharpe:** Mean(daily)/Std(daily) × √252 (risk-free = 0)
- **Max Drawdown:** Min(Equity / Equity cummax − 1)
- **Win Rate:** % profitable trades (approximate)
- **# Trades:** Count of completed long cycles
- **Avg Trade Return:** Mean return across trades

> Note: This simple backtester is for **educational** purposes. For production, consider position sizing, risk management, fee schedules, borrow costs, corporate actions, and latency/market impact modeling.

---

## 🧠 Author
**Mohammed Saif Wasay**  
*Data Analytics Graduate — Northeastern University*  
*Machine Learning Enthusiast | Passionate about turning data into insights*

🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/mohammed-saif-wasay-4b3b64199/)
