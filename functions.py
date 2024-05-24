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
    fig1.update_layout(xaxis_title='Zeit / s')

     # Aktualisiere den Namen der ersten Linie (PowerOriginal)
    fig1.data[0].name = 'Leistung'
    fig1.data[0].showlegend = True

    return fig1

make_plot(df)
# %%

value = df["PowerOriginal"]
power_level = 18
time = df["Time"]

def calculate_duration(df, power_level):
    durations =[]
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
    powerlevel_durations = {}
    
    unique_powerlevels = df["PowerOriginal"]
    
    for power_level in unique_powerlevels:
        durations = []
        start = 0
        end = 0
        
        for index, row in df.iterrows():
            value = row["PowerOriginal"]
            time = row["Time"]
            if value > power_level and start is None:
                start = time
            if value < power_level and start is not None:
                end = time
                durations.append(end-start) 
                start = None
        
        if start is not None:
            durations.append(end - start)
        
        max_duration = max(durations) if durations else 0
        powerlevel_durations[power_level] = max_duration
    
    return pd.DataFrame(list(powerlevel_durations.items()), columns=["PowerOriginal", "MaxDuration"])

calc_maxdurationpower(df)





# %%
