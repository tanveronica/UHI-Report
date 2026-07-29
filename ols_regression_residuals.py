import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ── Data ────────────────────────────────────────────────────────────────────

positions = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5",
]

zones = ["A"]*5 + ["B"]*5 + ["C"]*5

ISF = np.array([
    0, 33, 0, 0, 0,          # Zone A
    100, 87, 95, 92, 100,   # Zone B
    55, 60, 65, 100, 78     # Zone C
], dtype=float)

LST = np.array([
    12.92, 13.88, 13.30, 13.74, 12.60,   # Zone A
    18.58, 17.54, 18.60, 17.30, 18.62,   # Zone B
    14.62, 16.04, 16.30, 16.38, 15.70    # Zone C
], dtype=float)

# ── Regression ───────────────────────────────────────────────────────────────

slope, intercept, r_value, p_value, std_err = stats.linregress(ISF, LST)

r_squared = r_value ** 2

print("=" * 45)
print("       BURWOOD UHI — REGRESSION RESULTS")
print("=" * 45)
print(f"  Slope (m)       : {slope:.4f} °C per 1% ISF")
print(f"  Intercept (b)   : {intercept:.4f} °C")
print(f"  R               : {r_value:.4f}")
print(f"  R²              : {r_squared:.4f}")
print(f"  p-value         : {p_value:.2e}")
print(f"  Std error       : {std_err:.4f}")
print("=" * 45)
print(f"\n  Regression equation:")
print(f"  LST = {slope:.4f} × ISF + {intercept:.4f}")
print()

# ── Plot ─────────────────────────────────────────────────────────────────────

zone_colours = {"A": "#2ecc71", "B": "#e74c3c", "C": "#3498db"}
zone_labels  = {"A": "Zone A — Burwood Park", "B": "Zone B — High-rises", "C": "Zone C — Residential streets"}

fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor("#f9f9f9")
ax.set_facecolor("#f9f9f9")

# Scatter — one legend entry per zone
for zone in ["A", "B", "C"]:
    mask = np.array(zones) == zone
    ax.scatter(
        ISF[mask], LST[mask],
        color=zone_colours[zone],
        label=zone_labels[zone],
        s=90, zorder=5, edgecolors="white", linewidths=0.8
    )

# Regression line
x_line = np.linspace(ISF.min() - 5, ISF.max() + 5, 200)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, color="#2c3e50", linewidth=2,
        label=f"Regression: LST = {slope:.3f}×ISF + {intercept:.3f}")

# Confidence band (95%) for the mean regression line
n = len(ISF)
x_mean = ISF.mean()

y_pred = slope * ISF + intercept
residuals = LST - y_pred
residual_std_error = np.sqrt(np.sum(residuals**2) / (n - 2))

se_line = residual_std_error * np.sqrt(
    1/n + (x_line - x_mean)**2 / np.sum((ISF - x_mean)**2)
)

t_crit = stats.t.ppf(0.975, df=n-2)

ax.fill_between(
    x_line,
    y_line - t_crit * se_line,
    y_line + t_crit * se_line,
    alpha=0.15,
    color="#2c3e50",
    label="95% confidence band"
)

# Annotations
ax.set_xlabel("Impervious Surface Fraction — ISF (%)", fontsize=12)
ax.set_ylabel("Nighttime Land Surface Temperature — LST (°C)", fontsize=12)
ax.set_title(
    "Burwood North Metro Precinct\nLST vs ISF Regression",
    fontsize=13, fontweight="bold", pad=14
)

stats_text = (
    f"R  = {r_value:.3f}\n"
    f"R² = {r_squared:.3f}\n"
    f"p  = {p_value:.2e}\n"
    f"n  = {n}"
)
ax.text(0.03, 0.97, stats_text,
        transform=ax.transAxes,
        verticalalignment="top",
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8))

ax.legend(fontsize=9, loc="lower right")
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("burwood_regression.png", dpi=150, bbox_inches="tight")
plt.show()
print("Plot saved to burwood_regression.png")

# Predicted LST and residuals
predicted_LST = slope * ISF + intercept
residuals = LST - predicted_LST

# Residual plot
plt.figure(figsize=(8, 5))
plt.scatter(predicted_LST, residuals)
plt.axhline(0, linestyle="--")
plt.xlabel("Predicted LST (°C)")
plt.ylabel("Residual (°C)")
plt.title("Residual Analysis of OLS Regression")
plt.grid(True, alpha=0.4)
plt.show()

