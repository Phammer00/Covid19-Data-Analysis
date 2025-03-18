import pandas as pd
import matplotlib.pyplot as plt

# 1) Load dataset
df = pd.read_csv("C:/Users/Hammp/Desktop/covid_de.csv")
print("Dataset loaded successfully:")
print(df.head())

# 2) Handle missing values
df["age_group"] = df["age_group"].fillna("Unknown")
df["gender"] = df["gender"].fillna("Unknown")
print("Missing values handled:")
print(df.isna().sum())

# 3) Convert date to datetime
df["date"] = pd.to_datetime(df["date"])
print("Date column converted:")
print(df.dtypes)

# 3) Aggregate cases by date
df_daily_cases = df.groupby("date")["cases"].sum().reset_index()
print("Aggregated daily cases:")
print(df_daily_cases.head())

# 4) Calculate 7-day moving average
df_daily_cases["avg_7_days"] = df_daily_cases["cases"].rolling(window=7).mean()
print("Calculated 7-day moving average:")
print(df_daily_cases.head(10))

# 4.1) Plot daily cases and 7-day moving average
plt.figure(figsize=(16, 8))
plt.plot(df_daily_cases["date"], df_daily_cases["cases"], label="Daily cases", color="red", alpha=0.5)
plt.plot(df_daily_cases["date"], df_daily_cases["avg_7_days"], label="7-Day Moving Average", color="blue")
plt.title("COVID-19 Daily Cases in Germany")
plt.xlabel("Date")
plt.ylabel("Daily Cases")
plt.legend()
plt.grid(True)
plt.show()

# 5) Compare total COVID-19 cases per state
df_states = df.groupby("state")["cases"].sum().reset_index().sort_values(by="cases", ascending=False)

# Standardize state names
state_mapping = {
    "Baden-Wurttemberg": "Baden-Württemberg",
    "Thuringen": "Thüringen",
    "Sachsen Anhalt": "Sachsen-Anhalt",
}
df_states["state"] = df_states["state"].replace(state_mapping)
print("Cases by state:")
print(df_states)

# 5.1) Plot total cases per state
plt.figure(figsize=(16, 20))
plt.bar(df_states["state"], df_states["cases"], color="purple")
plt.title("COVID-19 Cases per German State")
plt.xlabel("State")
plt.ylabel("Total Cases")
plt.xticks(rotation=20)
plt.grid(axis="y")
plt.show()

# 6) Gender-specific analysis
gender_analysis = df.groupby("gender")[["cases", "deaths", "recovered"]].sum().reset_index()
print("Gender-specific COVID-19 analysis:")
print(gender_analysis)

# 6) Bar plot for gender analysis
gender_analysis.plot(x="gender", kind="bar", figsize=(12, 7), color=["skyblue", "salmon", "lightgreen"])
plt.title("COVID-19 Impact by Gender in Germany")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.grid(axis="y")
plt.show()

# 7) Pie charts for gender analysis
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
colors = ["#66b3ff", "#ff9999", "#99ff99"]

axes[0].pie(gender_analysis["cases"], labels=gender_analysis["gender"], autopct='%1.1f%%', colors=colors)
axes[0].set_title("Cases by Gender")

axes[1].pie(gender_analysis["deaths"], labels=gender_analysis["gender"], autopct='%1.1f%%', colors=colors)
axes[1].set_title("Deaths by Gender")

axes[2].pie(gender_analysis["recovered"], labels=gender_analysis["gender"], autopct='%1.1f%%', colors=colors)
axes[2].set_title("Recovered by Gender")

plt.suptitle("COVID-19 Gender Distribution in Germany")
plt.show()

