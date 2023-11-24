import asyncio
import websockets
import json
from datetime import datetime
import csv
import pandas as pd

olhc_data = {"Nifty": [], "Banknifty": [], "Finnifty": []}
last_moving_avg = {"Nifty": None, "Banknifty": None, "Finnifty": None}

async def connect_to_websocket():
    url = "wss://functionup.fintarget.in/ws?id=fintarget-functionup"
    
    async with websockets.connect(url) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            
            for instrument, value in data.items():
                olhc_data[instrument].append({
                    "Date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "Open": value,
                    "Low": value,
                    "High": value,
                    "Close": value
                })

                print(f"{instrument} OLHC data: {olhc_data[instrument][-1]}")

                # Writing OLHC data to CSV
                for instrument in olhc_data:
                    csv_filename = f"{instrument}_olhc_data.csv"
                    with open(csv_filename, mode='a', newline='') as csv_file:
                        fieldnames = ["Date", "Open", "Low", "High", "Close"]
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        
                        
                        if olhc_data[instrument]:
                            writer.writerow(olhc_data[instrument][-1])

                    # Calculating moving average
                    df = pd.DataFrame(olhc_data[instrument])
                    if len(df) >= 3:
                        df["MovingAverage"] = df["Close"].rolling(window=3).mean()
                        current_moving_avg = df["MovingAverage"].iloc[-1]

                        # Check if the current moving average is different from the last one
                        if current_moving_avg != last_moving_avg[instrument]:
                            print(f"{instrument} Moving Average: {current_moving_avg}")

                            # Writing moving average data to CSV
                            moving_avg_filename = f"{instrument}_moving_average.csv"
                            with open(moving_avg_filename, mode='a', newline='') as moving_avg_file:
                                moving_avg_fieldnames = ["Date", "MovingAverage"]
                                moving_avg_writer = csv.DictWriter(moving_avg_file, fieldnames=moving_avg_fieldnames)
                                
                                # Write moving average data
                                moving_avg_writer.writerow({
                                    "Date": df["Date"].iloc[-1],
                                    "MovingAverage": current_moving_avg
                                })

                            # Updating the last_moving_avg
                            last_moving_avg[instrument] = current_moving_avg

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_websocket())
