import numpy as np
import matplotlib.pyplot as plt

# ── Data Compilation ─────────────────────────────────────────────────────────
distance = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160])
temperature = np.array([13.52, 15.48, 15.40, 16.40, 17.58, 18.68, 17.48, 16.28, 17.54])

# Labels for specific landmarks to plot along the curve
landmarks = {
    0: "Burwood\nPark\nBoundary",
    20: "Concrete\nPath",
    40: "Low-rise\nopen\nroad",
    60: "High-Mass\nInterface",
    80: "High-rise\nBuilding",
    100: "High-desnity\nCommercial Area\n(Chicken Store)",
    120: "Urban\nCanyon",
    140: "Commercial\nBuilding",
    160: "Commercial\nBuilding\n(End)"
}

# ── Plot Customization ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor("#f9f9f9")
ax.set_facecolor("#f9f9f9")

# Plotting the continuous microclimatic wave line
ax.plot(distance, temperature, color="#2c3e50", linewidth=2.5, marker="o", 
        markersize=7, markerfacecolor="#e74c3c", markeredgecolor="white", 
        label="Mean Nighttime LST (°C)")

# Adding visual text markers for your real-world geographic features
for dist, label in landmarks.items():
    idx = np.where(distance == dist)[0][0]
    ax.annotate(label, (dist, temperature[idx]), textcoords="offset points", 
                xytext=(0,10), ha='center', fontsize=8, fontweight="bold",
                color="#34495e", arrowprops=dict(arrowstyle="->", color="#bdc3c7", lw=0.8))

# Formatting Axes and Titles
ax.set_xlabel("Transect Linear Distance (m)", fontsize=12, fontweight="medium")
ax.set_ylabel("Land Surface Temperature — LST (°C)", fontsize=12, fontweight="medium")
ax.set_title("160m Continuous Microclimatic Transect Profile\nThermal Trajectory away from Parkland Control Baseline", 
             fontsize=13, fontweight="bold", pad=16)

# Aesthetics
ax.set_xlim(-10, 170)
ax.set_ylim(12.5, 20.0)
ax.grid(True, linestyle="--", alpha=0.4, zorder=1)
ax.legend(loc="upper left", fontsize=10)

plt.tight_layout()
plt.savefig("transect_wave_profile.png", dpi=150, bbox_inches="tight")
plt.show()
print("Transect line profile successfully saved as 'transect_wave_profile.png'!")
