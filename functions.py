#%%
import pandas as pd
import plotly.express as px

#%%
data = pd.read_csv("activity.csv",delimiter=",")

data["Time"] = data.index
df = data[["Time","PowerOriginal"]]

def make_plot(df):
    df_subset = df.head(1803)
    fig1 = px.line(df_subset, x="Time", y="PowerOriginal", title='Leistung pro Zeit')

    # Aktualisiere die y-Achsenbeschriftung
    fig1.update_layout(yaxis_title='Leistung / W')
    fig1.update_layout(xaxis_title='Zeit / s')
    return fig1

make_plot(df)
# %%

value = df["PowerOriginal"]
power_level = 110
time = df["Time"]

def calculate_duration(df, power_level):
    durations = [0]
    start = None
    end = 0
    for index,row in df.iterrows():
        value = row["PowerOriginal"]
        time = row["Time"]
        if value > power_level and start is None:
            start = time
        if value < power_level and start is not None:
            end = time
            durations.append(end-start) 
            start = None
    return max(durations)
calculate_duration(df, power_level) 


# %%
def calc_maxdurationpower(df):
    unique_powerlevels = df["PowerOriginal"].unique()
    power_duration_list = []

    for power_level in unique_powerlevels:
        duration = calculate_duration(df, power_level)
        power_duration_list.append([power_level, duration])
    
    sortdata = pd.DataFrame(power_duration_list, columns=["PowerOriginal", "MaxDuration"]).sort_values(by = "MaxDuration", ascending=False)
    return sortdata

calc_maxdurationpower(df) 
# %%
sortdata = calc_maxdurationpower(df)  # Hier beide Rückgabewerte zuweisen

# Liniendiagramm der Leistungskurve erstellen
def make_lineplot(sortdata):
    df_subset = sortdata.head(1803)
    fig = px.line(df_subset, x="MaxDuration", y="PowerOriginal", markers=False, 
                  labels={"MaxDuration": "Maximale Dauer", "PowerOriginal": "Leistungsniveau"})

    fig.update_layout(title="Leistungskurve", xaxis_title="Maximale Dauer / s", yaxis_title="Leistung / W")
    return fig
# %%
