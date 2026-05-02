import pandas as pd
import numpy as np
from datetime import datetime

CITIES = ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]
PROPERTY_TYPES = ["Residential", "Commercial", "Land"]

NEIGHBORHOODS = {
    "Nairobi": ["Westlands", "Karen", "Kilimani", "Eastleigh", "Gigiri"],
    "Mombasa": ["Nyali", "Bamburi", "Tudor", "Likoni", "Mtwapa"],
    "Kisumu": ["Milimani", "Nyalenda", "Kondele", "Riat", "Mamboleo"],
    "Nakuru": ["Milimani", "Section 58", "Lanet", "Shabab", "Racecourse"]
}

def generate_market_data():
    np.random.seed(42)
    
    base_prices = {
        "Nairobi": {"Residential": 12500000, "Commercial": 45000000, "Land": 25000000},
        "Mombasa": {"Residential": 8500000, "Commercial": 28000000, "Land": 15000000},
        "Kisumu": {"Residential": 5500000, "Commercial": 18000000, "Land": 8000000},
        "Nakuru": {"Residential": 6500000, "Commercial": 22000000, "Land": 10000000}
    }

    quarters = [
        "Q1 2022", "Q2 2022", "Q3 2022", "Q4 2022",
        "Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023",
        "Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"
    ]

    records = []

    for city in CITIES:
        for prop_type in PROPERTY_TYPES:
            base = base_prices[city][prop_type]
            for i, quarter in enumerate(quarters):
                growth = 1 + (0.02 * i) + np.random.uniform(-0.01, 0.03)
                price = base * growth
                records.append({
                    "City": city,
                    "Property_Type": prop_type,
                    "Quarter": quarter,
                    "Avg_Price_KES": round(price),
                    "Rental_Yield": round(np.random.uniform(5.5, 9.5), 2),
                    "Occupancy_Rate": round(np.random.uniform(70, 95), 1),
                    "Transactions": np.random.randint(50, 500),
                    "Price_Per_Sqft": round(price / np.random.uniform(800, 2000))
                })

    return pd.DataFrame(records)


def get_city_summary(df, city):
    latest_quarter = df["Quarter"].iloc[-1]
    city_data = df[(df["City"] == city) & (df["Quarter"] == latest_quarter)]
    return city_data

def get_price_trends(df, city, property_type):
    filtered = df[
        (df["City"] == city) & 
        (df["Property_Type"] == property_type)
    ]
    return filtered[["Quarter", "Avg_Price_KES"]]

def get_market_overview(df):
    latest_quarter = df["Quarter"].iloc[-1]
    return df[df["Quarter"] == latest_quarter]

def get_top_performing_city(df):
    latest = get_market_overview(df)
    top = latest.groupby("City")["Rental_Yield"].mean().idxmax()
    return top

def get_summary_stats(df):
    latest = get_market_overview(df)
    return {
        "avg_price": round(latest["Avg_Price_KES"].mean(), 2)/1000000,
        "avg_rental_yield": round(latest["Rental_Yield"].mean(), 2),
        "avg_occupancy": round(latest["Occupancy_Rate"].mean(), 1),
        "total_transactions": int(latest["Transactions"].sum()),
        "top_city": get_top_performing_city(df)
    }