# The app.py pulls data from the data.py and gets insights from the ai_insights.py and displays it on a beatiful interactive dashboard
# plotly creates beautiful interactive charts, unlinke matplotlib
import streamlit as st
import plotly.express as px
import pandas as pd
from data import (
    generate_market_data,
    get_city_summary,
    get_price_trend,
    get_market_overview,
    get_summary_stats,
    CITIES,
    PROPERTY_TYPES
)
from ai_insights import generate_market_insights, ask_market_question

st.set_page_config(
    page_title = "Kenya Real Estate Dashboard",
    page_icon="🏠",
    layout="wide"
)

st.title("Kenya Real Estate Market Dashboard")
st.markdown("AI-powered marker intelligence for Kenyan Property Investors")
st.markdown("---")

# Without cache, the once the user clicks the slicer, the data refreshes from the pipeline but with cache, tha data loads from the cache without waiting.

@st.cache_data
def load_data():
    return generate_market_data()

df = load_data()
stats = get_summary_stats(df)

# Dasboard Filters
st.sidebar.title("Dasboard Filters")
st.sidebar.markdown("---")

selected_city = st.sidebar.selectbox(
    "Select City",
    options = ["All Cities"] + CITIES
)

selected_property = st.sidebar.selectbox(
    "Select Propert Type",
    options=["All Types"] + PROPERTY_TYPES
)

st.sidebar.markdown("---")
st.sidebar.markdown("About this Dashboard")
st.sidebar.markdown("Data Covers Q1 2022 TO Q4 2024 across 5 major cities in Kenya")

# This is the subheader of the dasboard
# I have manipulated the data to appear exactly like an executive dashboard
st.subheader("Market Overview - Q4 2024")

col1, col2, col3, col4, col5 = st.ccolumns(5)

with col1:
    st.metric(
        label = "Avg Propert Price",
        value = f"KES {stats['avg_price']: ,}"
    )

with col2:
    st.metric(
        label = "Avg Rental Yield",
        value = f"{stats['rental_yield']}%"
    )

with col3:
    st.metric(
        label = "Avg Occupancy Rate",
        value = f"{stats['occupancy_rate']}%"
    )

with col4:
    st.metric(
        label = "Total Transactions",
        value = f"{stats['transactions']:,}"
    )

with col5:
    st.metric(
        label = "Top Performing City",
        value = stats['top_city']
    )
st.markdown("---")    

#Chart 1 - Price Trends Line Chart
st.subheader("Property Trends Over Time")
col1, col2 = st.columns(2)

with col1: 
    city_for_trend = selected_city if selected_city != "All Cities" else "Nairobi"
    prop_for_trend = selected_property if selected_property != "All Types" else "Residential"

    trend_data = get_price_trend(df, city_for_trend, prop_for_trend)

    fig_line = px.line(
        trend_data,
        x="Quarter",
        y="Ävg_Price_KES",
        title= f"{city_for_trend} - {prop_for_trend} Price Trend",
        labels={"Avg_Price_KES": "Average Price (KES)", "Quarter": "Quarter"},
        markers=True, #Adds a dot to each data point
        color_discrete_sequence=["#2E86AB"]
    )

    fig_line.update_layout(
        plot_bgcolor="white", #white background
        yaxis_tickformat = "," #Formats the Y-axis with commas
    )
    st.plotly_chart(fig_line, use_container_width=True)


    # Chart 2 - City Comparison Bar Chart
    with col2:
        overview_data = get_market_overview(df)

        if selected_property != "All Types": #If selected, make the chart respond to filters dynamically
            overview_data = overview_data[overview_data["Property_Type"] == selected_property]

        fig_bar = px.bar(
            overview_data, 
            x="City",
            y="Avg_Price_KES",
            color = "Property_Type",
            title =  "Current Prices by City and Property Type",
            labels={"Avg_Price_KES": "Average Price (KES)", "City": "City"},
            barmode="group",
            color_discrete_sequence=["#2E86AB", "#A23B72", "#F18F01"] 
        )  

        fig_bar.update_layout(
            plot_bgcolor = "white",
            yaxis_tickformat = ","
        )  

        st.plotly_chart(fig_bar, use_container_width=True)

# Rental Yield HeatMap
# The Pivot table turns your data to a gridformat city as columns, property as rows.
# px.imshow creates a heatmap color Red=low yield, Yellow=medium, Green=high yield.
st.markdown("---")
st.subheader("Rental Yield HeatMap by City and Property Type")

heatmap_data = get_market_overview(df).pivot_table(
    values = "Rental Yield",
    index = "Property Type",
    columns = "City",
    aggfunc = "mean"

).round(2)

fig_heatmap = px.imshow(
    heatmap_data,
    title = "Average Rental Yield - Q4 2024",
    color_continuous_scale = "RdYlGn",
    aspect = "auto",
    text_auto=True
)

fig_heatmap.update_layout(
    plot_bgcolor="white"
)

st.plotly_chart(fig_heatmap, use_container_width=True)