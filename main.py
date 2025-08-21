# (c) 2025 Mohammed Saif Wasay
# Run a single SMA crossover backtest and save figures/reports.
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from src.strategy import load_price_data, backtest

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", type=str, default="SPY")
    p.add_argument("--start", type=str, default="2015-01-01")
    p.add_argument("--end", type=str, default="2025-01-01")
    p.add_argument("--fast", type=int, default=50)
    p.add_argument("--slow", type=int, default=200)
    p.add_argument("--offline", action="store_true", help="Use synthetic data if set.")
    p.add_argument("--cost_bps_roundtrip", type=float, default=10.0)
    p.add_argument("--slip_bps", type=float, default=5.0)
    args = p.parse_args()

    df = load_price_data(args.ticker, args.start, args.end, offline=args.offline)
    bt, perf = backtest(df, args.fast, args.slow, args.cost_bps_roundtrip, args.slip_bps)

    # Save report
    report = pd.DataFrame({
        "Metric": ["Total Return","CAGR","Sharpe","Max Drawdown","Win Rate","# Trades","Avg Trade Return"],
        "Value": [perf.total_return, perf.cagr, perf.sharpe, perf.max_drawdown, perf.win_rate, perf.num_trades, perf.avg_trade_return]
    })
    report_path = "reports/report.csv"
    report.to_csv(report_path, index=False)

    # Plot equity
    plt.figure(figsize=(10,5))
    plt.plot(bt.index, bt["equity"], label="SMA Crossover Strategy")
    plt.plot(bt.index, bt["buyhold"], label="Buy & Hold")
    plt.title(f"{args.ticker} SMA Crossover ({args.fast}/{args.slow})")
    plt.xlabel("Date"); plt.ylabel("Equity (Growth of $1)")
    plt.legend(); plt.tight_layout()
    fig_path = "figures/equity_curve.png"
    plt.savefig(fig_path, dpi=150)

    print("Saved:")
    print(f"- {report_path}")
    print(f"- {fig_path}")
    print("Performance:", perf)

if __name__ == "__main__":
    main()
