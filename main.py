#%%
import functions
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

functions.make_plot(functions.df)

functions.calc_maxdurationpower(functions.df)

tab1 = st.tabs(["Leistung"])

with tab1:
    st.header("Leistung")
    st.write("")

    fig.update_layout(title="Maximale Dauer pro Leistungsniveau", xaxis_title="Leistung / W", yaxis_title="Maximale Dauer / s")
    fig.show()


# %%


tab1, tab2, tab3 = st.tabs(["EKG-Data", "Power-Data", "Auswertung"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)