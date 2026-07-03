import tushare as ts
import json

TUSHARE_TOKEN = "c151f3ef66661c08ee9cd6c20b490b1b53ce39dcfde80dce3ce23f49"
ts.set_token(TUSHARE_TOKEN)
pro = ts.pro_api()

start_date = "20250703"
end_date = "20260703"
print(f"Fetching 京东方A (000725.SZ) data from {start_date} to {end_date}...")

df = pro.daily(ts_code="000725.SZ", start_date=start_date, end_date=end_date)
print(f"Got {len(df)} rows")
print(df.head())

# Sort ascending
df = df.sort_values("trade_date")

# Save as JSON
records = df.to_dict(orient="records")
for r in records:
    # Convert numpy types
    for k, v in r.items():
        if hasattr(v, "item"):
            r[k] = v.item()

json_path = "/Users/newcomer/Desktop/workbuddy本地文件/jingdong_data.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False)
print(f"Saved to {json_path}")
print(f"Total records: {len(records)}")
