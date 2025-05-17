import csv
from datetime import datetime

def log_sweep_result(site_results, total_avg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("mood_history.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for site, avg_score in site_results.items():
            writer.writerow([timestamp, site, avg_score])
        writer.writerow([timestamp, "OVERALL", total_avg])
