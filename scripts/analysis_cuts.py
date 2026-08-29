
import pandas as pd
import matplotlib.pyplot as plt

TARGET_KEYS = ["id","prefix_id", "seq", "cut" ,"trace_arm" , "letters"]
SHOW_PLOTS = False
PRINT_Q = False

def printer(*item):
    if PRINT_Q:
        print(*item)
    
df_raw = pd.read_json("runs/resample_cuts_2026-08-25_1503.jsonl", lines=True)

df = df_raw[df_raw.columns.intersection(TARGET_KEYS)]



print("*"*50)
print("*"*50)
counts = df.groupby("prefix_id").size()
if counts.eq(25).all():
    print("Sanity check: pass")
else:
    print("Sanity check: NOT pass. The total count of each run is expected to be 25.")
print("*"*50)
print("*"*50)


df["letters"] = df["letters"].apply(tuple)


df_trace_cut = df.groupby(["trace_arm","cut"])["letters"].value_counts().reset_index(name = "count")
print(df_trace_cut)

total_shared = (df["trace_arm"] == "shared").sum()
total_shared_C = ((df["trace_arm"] == "shared") & (df["letters"] == ("C",))).sum()
total_shared_E = ((df["trace_arm"] == "shared") & (df["letters"] == ("E",))).sum()
total_shared_other = ((df["trace_arm"] == "shared") & (df["letters"] != ("E",))& (df["letters"] != ("C",))).sum()

P_C_baseline = total_shared_C / total_shared
P_E_baseline = total_shared_E / total_shared
P_other_baseline = total_shared_other / total_shared


summary_table = []
summary_table.append(["base line of C trace", float(P_C_baseline)])
summary_table.append(["base line of E trace", float(P_E_baseline)])
summary_table.append(["base line of other trace", float(P_other_baseline)])


printer("-"*50)
printer("-"*50)
printer("-"*50)
printer("baseline")
printer(P_C_baseline,P_E_baseline,P_other_baseline)
printer("-"*50)
printer("branches")
all_C_cut = df.loc[df["trace_arm"] == "c004", "cut"].unique()
all_E_cut = df.loc[df["trace_arm"] == "e036", "cut"].unique()

printer("-"*50)
for item in all_C_cut:
    printer(item)
    total_occurance = ((df["trace_arm"] == "c004") & (df["cut"] == item)).sum()
    C_occurance = ((df["trace_arm"] == "c004") & (df["cut"] == item) & (df["letters"] == ("C",))).sum()
    summary_table.append([f"P(C|C-trace and cut at {item}) = ", float(C_occurance/total_occurance)])
    printer("C_occurance = ", C_occurance)
    printer("total_occurance = ", total_occurance)
    printer(f"P(C|C-trace and cut at {item}) = ", C_occurance/total_occurance)

printer("-"*50)
for item in all_E_cut:
    printer(item)
    total_occurance = ((df["trace_arm"] == "e036") & (df["cut"] == item)).sum()
    E_occurance = ((df["trace_arm"] == "e036") & (df["cut"] == item) & (df["letters"] == ("E",))).sum()
    summary_table.append([f"P(E|E-trace and cut at {item}) = ", float(E_occurance/total_occurance)])
    printer("x1 = ", E_occurance)
    printer("total_occurance = ", total_occurance)
    printer(f"P(E|E-trace and cut at {item}) = ", E_occurance/total_occurance)

printer("-"*50)


df_summary = pd.DataFrame(summary_table)
print(df_summary)
df_summary.to_csv("probability_summary", index = False)


if SHOW_PLOTS:
    def format_letters(x):
        if len(x) == 0:
            return "None"
        return ",".join(x)

    df_trace_cut["letters"] = df_trace_cut["letters"].apply(format_letters)
    def plot_bar_chart(trace_str):
        plot_df = df_trace_cut[df_trace_cut["trace_arm"] == trace_str]
        plot_df = (
            plot_df
            .pivot(index="cut", columns="letters", values="count")
            .fillna(0)
        )


        # Plot
        plot_df.plot(
            kind="bar",
            stacked=True,
            width = 0.5
        )

        plt.title(trace_str)
        plt.xlabel("Cut")
        plt.ylabel("Count")
        plt.legend(title="Letters")
        plt.tight_layout()

        plt.show()

    plot_bar_chart("c004")
    plot_bar_chart("e036")

    plot_df = df_trace_cut[df_trace_cut["trace_arm"] == "shared"]

    pie_df = plot_df.groupby("letters")["count"].sum()




    total = pie_df.sum()

    labels = [
        f"{letter} ({value / total * 100:.0f}%)"
        for letter, value in pie_df.items()
    ]
    pie_df.plot(
        kind="pie",
        labels=labels,
        startangle=0,
        labeldistance=0.50
    )

    plt.title("Shared")
    plt.show()