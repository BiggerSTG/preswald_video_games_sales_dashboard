from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px

# Load the data
connect()
df = get_df("video_games_sales_cleaned_csv")

# Find all games with Global Sales greater than 25 million
top_sellers_sql = """
SELECT Name, Platform, Genre, Publisher, Global_Sales
FROM video_games_sales_cleaned_csv
WHERE Global_Sales > 25
ORDER BY Global_Sales DESC
"""
top_sellers_df = query(top_sellers_sql, "video_games_sales_cleaned_csv")

# Drop rows with NaN in critical columns
df = df.dropna(subset=["Global_Sales", "NA_Sales", "EU_Sales", "Critic_Score", "User_Score", "Rating"])

# Remove "tbd" user scores
df = df[df["User_Score"] != "tbd"]

# Convert User_Score safely to float
df["User_Score"] = df["User_Score"].astype(float)

# Title
text("# 🎮 Video Game Sales Dashboard")

# Display Top Sellers
text("## 🏆 Top Selling Games (Above 25M Sales)")
table(top_sellers_df, title="Top Sellers")

# Add an interactive Threshold Slider
threshold = slider("Set Global Sales Threshold (in Millions)", min_val=0, max_val=100, default=25)
table(df[df["Global_Sales"] > threshold], title="Games Above Threshold")

# Scatter plot of NA Sales vs EU Sales
fig_scatter = px.scatter(
    df,
    x="NA_Sales",
    y="EU_Sales",
    size="Global_Sales",
    color="Genre",
    hover_name="Name",
    title="Sales Comparison: North America vs Europe"
)
plotly(fig_scatter)

# Bar chart of Global Sales by Platform
fig_bar = px.bar(
    df.groupby("Platform")["Global_Sales"].sum().reset_index(),
    x="Platform",
    y="Global_Sales",
    title="Total Global Sales by Platform",
    labels={"Global_Sales": "Total Sales (M)"}
)
plotly(fig_bar)

# Critic Score vs Global Sales
fig_critic = px.scatter(
    df,
    x="Critic_Score",
    y="Global_Sales",
    color="Rating",
    trendline="ols",
    title="Critic Score vs Global Sales (Colored by Rating)",
    hover_name="Name"
)
plotly(fig_critic)

# User Score vs Global Sales
fig_user = px.scatter(
    df,
    x="User_Score",
    y="Global_Sales",
    color="Rating",
    trendline="ols",
    title="User Score vs Global Sales (Colored by Rating)",
    hover_name="Name"
)
plotly(fig_user)

# Distribution of Global Sales by Game Rating
fig_box = px.box(
    df,
    x="Rating",
    y="Global_Sales",
    title="Distribution of Global Sales by Game Rating"
)
plotly(fig_box)