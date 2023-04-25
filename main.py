import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days ")
place = st.text_input("Place : ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select the data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days_local):
    dates = ["2023-25-02", "2023-26-02", "2023-27-02"]
    temperatures = [22, 25, 27]
    temperatures = [days_local * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
