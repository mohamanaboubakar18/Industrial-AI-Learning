from statistics import mean, stdev
import matplotlib.pyplot as plt

# --- Sensor measurements (in °C) ---
# Simulated from sensors on an HV substation
labels = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5"]
temp_measures = [15.23, 25.02, 30.2, 35, 50]

# --- Alert threshold ---
ALERT_THRESHOLD = 40  # °C — critical threshold for HV equipment

# --- Statistical calculations ---
avg = mean(temp_measures)
std_dev = stdev(temp_measures)

print("=" * 45)
print("   HV SUBSTATION THERMAL MONITORING REPORT")
print("=" * 45)
print(f"Average temperature  : {avg:.2f} °C")
print(f"Standard deviation   : {std_dev:.2f} °C")
print(f"Alert threshold      : {ALERT_THRESHOLD} °C")
print("-" * 45)

# --- Anomaly detection ---
anomalies = []
for i, temp in enumerate(temp_measures):
    status = "✅ Normal"
    if temp > ALERT_THRESHOLD:
        status = "🚨 ALERT — Critical temperature"
        anomalies.append(labels[i])
    print(f"{labels[i]} : {temp} °C  →  {status}")

print("-" * 45)
if anomalies:
    print(f"⚠️  {len(anomalies)} anomaly/anomalies detected: {', '.join(anomalies)}")
    print("   Recommended action: immediate inspection")
else:
    print("✅ All sensors within normal range.")
print("=" * 45)

# --- Visualization ---
colors = ["red" if t > ALERT_THRESHOLD else "steelblue" for t in temp_measures]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, temp_measures, color=colors, edgecolor="white", linewidth=0.5)
plt.axhline(y=avg, color="orange", linestyle="--", linewidth=1.5, label=f"Average: {avg:.2f} °C")
plt.axhline(y=ALERT_THRESHOLD, color="red", linestyle=":", linewidth=1.5, label=f"Alert threshold: {ALERT_THRESHOLD} °C")

for bar, temp in zip(bars, temp_measures):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f"{temp} °C", ha="center", va="bottom", fontsize=9)

plt.title("Thermal Monitoring — HV Substation", fontsize=13, fontweight="bold")
plt.ylabel("Temperature (°C)")
plt.ylim(0, max(temp_measures) + 15)
plt.legend()
plt.tight_layout()
plt.savefig("hta_thermal_monitoring.png", dpi=150)
plt.show()
print("\n📊 Chart exported: hta_thermal_monitoring.png")
