import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the Next Days ")
place = st.text_input("Place : ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select the data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:  # if place is provided on then call the function
    # Get the temperature/ sky
    try:
        filtered_content = backend.get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_content]  # dict is a variable
            dates = [dict["dt_txt"] for dict in filtered_content]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_content]  # 1. Sky is stored under main
            # variable 2. [0] because weather is dictionary with only one entity in which main or sky is mentioned
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
    except KeyError:
        st.write("Entered Place Does Not Exists !!")
