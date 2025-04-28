# Video Game Sales Dashboard

This project is a data-driven interactive dashboard exploring global video game sales, built as part of a coding challenge for Structured Labs.

Using a real-world dataset, the dashboard allows users to:
- View top-selling games globally.
- Dynamically filter games based on customizable global sales thresholds.
- Analyze regional sales trends across North America and Europe.
- Explore relationships between Critic Scores, User Scores, and overall game sales.
- Understand how game ratings (E, T, M) impact global sales distributions.

## Tech Stack

- Python
- Pandas
- Plotly Express
- Preswald SDK

##  Data Cleaning

The original dataset included missing values and non-numeric entries (such as `tbd` for User Scores).  
During preprocessing:
- Rows with missing critical values (`Global_Sales`, `NA_Sales`, `EU_Sales`, `Critic_Score`, `User_Score`, `Rating`) were removed.
- Non-numeric User Scores (`tbd`) were filtered out, and the `User_Score` column was safely converted to float.

## Project Structure

- `app.py` — Main dashboard script.
- `data/video_games_sales_cleaned.csv` — Cleaned video game sales dataset.
