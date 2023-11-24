# Real-time Data Processing with WebSocket in Python

This Python project connects to a WebSocket server and processes real-time data, calculating OLHC (Open, Low, High, Close) data and computing moving averages for different financial instruments.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git

2. Install dependencies:
   
   ```bash
   pip install websockets pandas

## Usage

1. Run the script

    ```bash
    python websocket_client.py

1. The script connects to the WebSocket server (wss://functionup.fintarget.in/ws?id=fintarget-functionup) and starts processing real-time data.

2. OLHC data is recorded in separate CSV files (Nifty_olhc_data.csv, Banknifty_olhc_data.csv, Finnifty_olhc_data.csv).

3. Moving averages are calculated and stored in separate CSV files (Nifty_moving_average.csv, Banknifty_moving_average.csv, Finnifty_moving_average.csv).

## File Structure

* websocket_client.py: Main script for connecting to the WebSocket server and processing real-time data.
* Nifty_olhc_data.csv, Banknifty_olhc_data.csv, Finnifty_olhc_data.csv: CSV files containing OLHC data.
* Nifty_moving_average.csv, Banknifty_moving_average.csv, Finnifty_moving_average.csv: CSV files containing moving averages.

##  Dependencies
* websockets: A library for handling WebSocket connections in Python.
* pandas: A powerful data manipulation library for Python.

