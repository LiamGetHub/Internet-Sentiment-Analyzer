import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("mood_history.csv", names=["timestamp", "site", "sentiment"])
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.dropna(subset=['sentiment'])  # Drop rows with missing sentiment
df['sentiment'] = df['sentiment'].astype(float)

# === Line Plot: Sentiment Over Time ===
plt.figure(figsize=(10, 5))
for site in df['site'].unique():
    if site != "OVERALL":
        site_df = df[df['site'] == site]
        plt.plot(site_df['timestamp'], site_df['sentiment'], label=site)

plt.title("Sentiment Over Time per News Site")
plt.xlabel("Timestamp")
plt.ylabel("Sentiment")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# === Bar Plot: Latest Sentiment per Site ===
latest_timestamp = df['timestamp'].max()
latest_df = df[df['timestamp'] == latest_timestamp]
latest_df = latest_df[latest_df['site'] != "OVERALL"]

plt.figure(figsize=(8, 5))
plt.bar(latest_df['site'], latest_df['sentiment'], color='skyblue')
plt.title(f"Latest Sentiment by Site ({latest_timestamp.strftime('%Y-%m-%d %H:%M')})")
plt.xlabel("News Site")
plt.ylabel("Sentiment Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
