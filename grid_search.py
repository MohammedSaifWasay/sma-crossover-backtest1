# (c) 2025 Mohammed Saif Wasay
# Grid search for SMA fast/slow windows; produces CSV and heatmap of Sharpe.
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.strategy import load_price_data, backtest

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", type=str, default="SPY")
    p.add_argument("--start", type=str, default="2015-01-01")
    p.add_argument("--end", type=str, default="2025-01-01")
    p.add_argument("--offline", action="store_true")
    p.add_argument("--fast_range", type=str, default="10,20,30,50,100")
    p.add_argument("--slow_range", type=str, default="100,150,200,250,300")
    p.add_argument("--cost_bps_roundtrip", type=float, default=10.0)
    p.add_argument("--slip_bps", type=float, default=5.0)
    args = p.parse_args()

    fasts = [int(x) for x in args.fast_range.split(",")]
    slows = [int(x) for x in args.slow_range.split(",")]

    df = load_price_data(args.ticker, args.start, args.end, offline=args.offline)

    results = []
    for f in fasts:
        for s in slows:
            if f >= s:
                continue
            _, perf = backtest(df, f, s, args.cost_bps_roundtrip, args.slip_bps)
            results.append({"fast": f, "slow": s, "sharpe": perf.sharpe, "cagr": perf.cagr, "max_dd": perf.max_drawdown})

    res_df = pd.DataFrame(results)
    csv_path = "reports/grid_search.csv"
    res_df.to_csv(csv_path, index=False)

    # Pivot and plot heatmap of Sharpe
    pivot = res_df.pivot(index="fast", columns="slow", values="sharpe")
    plt.figure(figsize=(8,6))
    plt.imshow(pivot.values, aspect="auto")
    plt.colorbar(label="Sharpe")
    plt.xticks(ticks=np.arange(len(pivot.columns)), labels=pivot.columns.astype(str), rotation=45)
    plt.yticks(ticks=np.arange(len(pivot.index)), labels=pivot.index.astype(str))
    plt.title(f"Sharpe Heatmap: {args.ticker} SMA Grid")
    plt.tight_layout()
    fig_path = "figures/grid_sharpe_heatmap.png"
    plt.savefig(fig_path, dpi=150)

    print("Saved:")
    print(f"- {csv_path}")
    print(f"- {fig_path}")

if __name__ == "__main__":
    main()
