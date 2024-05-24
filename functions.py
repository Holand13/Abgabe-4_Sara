#%%
import pandas as pd
import plotly.express as px

#%%
data = pd.read_csv("activity.csv",delimiter=",")

data["Time"] = data.index
df = data[["Time","PowerOriginal"]]

def make_plot(df):
    df_subset = df.head(1803)
    fig1 = px.line(df_subset, x="Time", y="PowerOriginal", title='Leistungskurve')
    # Füge die Herzfrequenz als zweite Linie hinzu
    

    # Aktualisiere die y-Achsenbeschriftung
    fig1.update_layout(yaxis_title='Messwerte')
    fig1.update_layout(xaxis_title='Zeit / s')

     # Aktualisiere den Namen der ersten Linie (PowerOriginal)
    fig1.data[0].name = 'Leistung'
    fig1.data[0].showlegend = True

    return fig1

make_plot(df)
print(data)
# %%

value = df["PowerOriginal"]
power_level = 180
time = df["Time"]

def calculate_duration(df, power_level):
    durations =[]
    start = 0
    end = 0
    for index,row in df.iterrows():
        value = row["PowerOriginal"]
        time = row["Time"]
        if value > power_level:
            start = time 
        if value < power_level:
            end = time 
        durations.append(end-start)
    print(durations)
    return max(durations)
calculate_duration(df, power_level)



# %%
