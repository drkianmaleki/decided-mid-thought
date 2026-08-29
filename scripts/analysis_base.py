
import pandas as pd
import matplotlib.pyplot as plt

TARGET_KEYS = ["condition", "letters", "sample" ]
SHOW_PLOTS = False
PRINT_Q = True

def printer(*item):
    if PRINT_Q:
        print(*item)
    
df_raw = pd.read_json("runs/sweep_items_batball_2026-08-19_1623.jsonl", lines=True)

df = df_raw[df_raw.columns.intersection(TARGET_KEYS)]



df["letters"] = df["letters"].apply(tuple)

df_count = df.groupby("condition")["letters"].value_counts()

printer(df_count)

baseline_summary = []

df_counts = df["letters"].value_counts()
print(df_counts)

total_count = len(df)


for val , count in df_counts.items():
    baseline_summary.append([f'P{val} = ', float(count/total_count)])

print(baseline_summary)


baseline_summary = pd.DataFrame(baseline_summary)
print(baseline_summary)
baseline_summary.to_csv("baseline_summary", index = False)
