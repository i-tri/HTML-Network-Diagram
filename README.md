# HTML-Network-Diagram
This program plots a network with sites and links.


# Network Map Plotter

## Overview
This Python program reads a CSV file containing site and link information and plots a network map using OpenStreetMap. The links are color-coded based on the communication medium (e.g., Microwave, Fibre, etc.). The generated map is saved as an HTML file and can be viewed in a web browser.

## Features
- Reads a CSV file with site and link details.
- Automatically assigns different colors for each link medium.
- Uses OpenStreetMap (via Folium) to plot the network.
- Adds labeled markers for each site.
- Saves the generated network map as an HTML file.
- Opens the map in the default web browser upon completion.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:
```sh
pip install pandas folium tkinter
```

## Usage
1. Run the script:
   ```sh
   python HTML_Network_Plot.py
   ```
2. Select the CSV file when prompted.
3. Choose a location to save the output HTML file.
4. The network map will be generated and opened in your web browser.

## CSV Format
The input CSV file should contain the following columns:
```
Link ID | Site A | Latitude A | Longitude A | Site B | Latitude B | Longitude B | New Link Name | Medium
```
### Example Data:
```
1, SiteX, -36.8485, 174.7633, SiteY, -37.8136, 144.9631, Link1, Fibre
2, SiteA, -33.8688, 151.2093, SiteB, -31.9505, 115.8605, Link2, Microwave
```

## Output
- The script generates an interactive HTML map file.
- Each site is labeled and linked with colored lines representing the communication medium.
- The file is automatically opened upon completion.

## License
This project is open-source and available under the MIT License.

## Author
Stephan Nawn

