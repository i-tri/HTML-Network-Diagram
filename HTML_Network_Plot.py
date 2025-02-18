#####
# This program plots a network with sites and links.
# The links are colour coded for each medium to distinguish between different mediums for example: Microwave, Fibre, etc.
# Import csv file with columns:
# Link ID | Site A | Latitude A | Longitude A | Site B | Latitude B | Longitude B | New Link Name | Medium
# This will plot a network map on Open StreetView and save it as a HTML
#####

import pandas as pd
import folium
import webbrowser
import os
import random
import tkinter as tk
from tkinter import filedialog

# GUI to select CSV file and save HTML file
root = tk.Tk()
root.withdraw()  # Hide the main window
csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
if not csv_file_path:
    print("No file selected. Exiting...")
    exit()

output_html_path = filedialog.asksaveasfilename(title="Save HTML File As", defaultextension=".html", filetypes=[("HTML Files", "*.html")])
if not output_html_path:
    print("No output file selected. Exiting...")
    exit()

# Read the CSV file
df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")

# Generate unique colors for each unique Medium type
unique_mediums = df["Medium"].unique()
color_palette = ["red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue", "darkgreen",
                 "cadetblue", "darkpurple", "white", "pink", "lightblue", "lightgreen", "gray", "black", "lightgray"]
medium_color_map = {medium: color_palette[i % len(color_palette)] for i, medium in enumerate(unique_mediums)}

# Calculate the center for the map
center_lat, center_lon = df["Latitude A"].mean(), df["Longitude A"].mean()

# Create a map centered at the average coordinates
m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

# Add points and lines to the map
for _, row in df.iterrows():
    medium = row["Medium"]
    color = medium_color_map.get(medium, "gray")  # Default to gray if Medium is missing

    # Add a bullet-style marker for Site A
    folium.CircleMarker(
        location=[row["Latitude A"], row["Longitude A"]],
        radius=2,  # Size of the bullet
        color="darkblue",
        fill=True,
        fill_color="darkblue",
        fill_opacity=1,
        popup=f"Site A: {row['Site A']}"
    ).add_to(m)

    # Add a label near Site A
    folium.Marker(
        [row["Latitude A"], row["Longitude A"]],
        icon=folium.DivIcon(html=f"""<div style="font-size: 10pt;  color: black;">{row['Site A']}</div>""")
    ).add_to(m)

    # Add a bullet-style marker for Site B
    folium.CircleMarker(
        location=[row["Latitude B"], row["Longitude B"]],
        radius=2,
        color="darkblue",
        fill=True,
        fill_color="darkblue",
        fill_opacity=1,
        popup=f"Site B: {row['Site B']}"
    ).add_to(m)

    # Add a label near Site B
    folium.Marker(
        [row["Latitude B"], row["Longitude B"]],
        icon=folium.DivIcon(html=f"""<div style="font-size: 10pt; color: black;">{row['Site B']}</div>""")
    ).add_to(m)

    # Draw a line between Site A and Site B with Medium-based colors
    folium.PolyLine(
        locations=[
            (row["Latitude A"], row["Longitude A"]),
            (row["Latitude B"], row["Longitude B"])
        ],
        color=color,
        weight=2.5,
        opacity=0.7,
        popup=f"Link ID: {row['Link ID']} - Medium: {medium}"
    ).add_to(m)

# Save the map to an HTML file
m.save(output_html_path)

# Automatically open the generated map in the default web browser
webbrowser.open(f"file://{os.path.abspath(output_html_path)}")

print(f"Map with labeled markers and Medium-based link colors has been saved and opened: {output_html_path}")
