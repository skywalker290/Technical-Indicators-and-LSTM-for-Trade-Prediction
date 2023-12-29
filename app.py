import gradio as gr
import numpy as np
import plotly.express as px
import pandas as pd
import pickle

iso_dict=pickle.load(open('datasets/iso_dict.pkl','rb'))
iso_data=pd.DataFrame(iso_dict)

df_dict=pickle.load(open('datasets/df_date.pkl','rb'))
df_date=pd.DataFrame(df_dict)

df_hour=pickle.load(open('datasets/df_hour.pkl','rb'))
df_hour=pd.DataFrame(df_hour)
    
def graph(time, indicator):

    if indicator == 'Simple Moving Average' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['close','SMA_5', 'SMA_15'], labels={'value': 'Values'}, title='Simple Moving Average (date-wise) Chart')
        return fig
    
    elif indicator == 'Simple Moving Average' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['close','SMA_5', 'SMA_15'], labels={'value': 'Values'}, title='Simple Moving Average (minute-wise) Chart')
        return fig
    
    elif indicator == 'Simple Moving Average' and time == "Hour-wise":
        fig = px.line(df_hour, x='time', y=['close','SMA_5', 'SMA_15'], labels={'value': 'Values'}, title='Simple Moving Average (hour-wise) Chart')
        return fig
    
    elif indicator == 'Volume Moving Average' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['Volume','VMA_5', 'VMA_15'], labels={'value': 'Values'}, title='Volume Moving Average (date-wise) Chart')
        return fig
    
    elif indicator == 'Volume Moving Average' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['Volume','VMA_5', 'VMA_15'], labels={'value': 'Values'}, title='Volume Moving Average (minute-wise) Chart')
        return fig
    
    elif indicator == 'Volume Moving Average' and time == "Hour-wise":
        fig = px.line(df_hour, x='time', y=['Volume','VMA_5', 'VMA_15'], labels={'value': 'Values'}, title='Volume Moving Average (hour-wise) Chart')
        return fig
    
    elif indicator == 'Exponential Moving Average' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['close','EMA_5', 'EMA_15'], labels={'value': 'Values'}, title='Exponential Moving Average (minute-wise) Chart')
        return fig
    
    elif indicator == 'Exponential Moving Average' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['close','EMA_5', 'EMA_15'], labels={'value': 'Values'}, title='Exponential Moving Average (date-wise) Chart')
        return fig
    
    elif indicator == 'Exponential Moving Average' and time == "Hour-wise":
        fig = px.line(df_hour, x='time', y=['close','EMA_5', 'EMA_15'], labels={'value': 'Values'}, title='Exponential Moving Average (hour-wise) Chart')
        return fig
    
    elif indicator == 'Relative State Indexing' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['close','RSI_5', 'RSI_15'], labels={'value': 'Values'}, title='Relative State Indexing (date-wise) Chart')
        return fig
    
    elif indicator == 'Relative State Indexing' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['close','RSI_50', 'RSI_150'], labels={'value': 'Values'}, title='Relative State Indexing (minute-wise) Chart')
        return fig
    
    elif indicator == 'Relative State Indexing' and time == "Hour-wise":
        fig = px.line(df_hour, x='time', y=['close','RSI_20', 'RSI_60'], labels={'value': 'Values'}, title='Relative State Indexing (hour-wise) Chart')
        return fig
    
    elif indicator == 'Moving Average Convergence Divergence' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['MACD_line', 'MACD_signal', 'MACD'], labels={'value': 'Values'}, title='Moving Average Convergence Divergence (date-wise) Chart')
        return fig
    
    elif indicator == 'Moving Average Convergence Divergence' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['MACD_line', 'MACD_signal', 'MACD'], labels={'value': 'Values'}, title='Moving Average Convergence Divergence (minute-wise) Chart')
        return fig
    
    elif indicator == 'Moving Average Convergence Divergence' and time == "Hour-wise":
        fig = px.line(iso_data, x='time', y=['MACD_line', 'MACD_signal', 'MACD'], labels={'value': 'Values'}, title='Moving Average Convergence Divergence (hour-wise) Chart')
        return fig
    
    elif indicator == 'Upper and Lower Bollinger Bands' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['close', 'Lower Bollinger Band', 'Upper Bollinger Band'], labels={'value': 'Values'}, title='Upper and Lower Bollinger Bands (minute-wise) Chart')
        return fig
    
    elif indicator == 'Upper and Lower Bollinger Bands' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['close', 'Lower Bollinger Band', 'Upper Bollinger Band'], labels={'value': 'Values'}, title='Upper and Lower Bollinger Bands (date-wise) Chart')
        return fig
    
    elif indicator == 'Upper and Lower Bollinger Bands' and time == "Hour-wise":
        fig = px.line(df_date, x='time', y=['close', 'Lower Bollinger Band', 'Upper Bollinger Band'], labels={'value': 'Values'}, title='Upper and Lower Bollinger Bands (hour-wise) Chart')
        return fig
    
    elif indicator == 'Average True Range' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['ATR_12', 'ATR_3'], labels={'value': 'Values'}, title='Average True Range (minute-wise) Chart')
        return fig
    
    elif indicator == 'Average True Range' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['ATR_12', 'ATR_3'], labels={'value': 'Values'}, title='Average True Range (date-wise) Chart')
        return fig
    
    elif indicator == 'Average True Range' and time == "Hour-wise":
        fig = px.line(df_date, x='time', y=['ATR_12', 'ATR_3'], labels={'value': 'Values'}, title='Average True Range (hour-wise) Chart')
        return fig


styler = df_date.style.highlight_max(color='pink', axis=0)

with gr.Blocks() as demo:
     gr.Label("Nifty 50 Sensex Data")
     gr.Markdown("Nifty Data Date-wise")
     gr.DataFrame(styler)
     with gr.Column():
         with gr.Row():
             time=gr.Radio(choices=["Date-wise", "Minute-wise", "Hour-wise"], label="Time variation:")
             indicator=gr.Radio(
                 ["Simple Moving Average", "Volume Moving Average", "Exponential Moving Average", 
                  "Relative State Indexing", "Moving Average Convergence Divergence", 
                  "Upper and Lower Bollinger Bands", "Average True Range"],
                 label="Select Indicator:"
             )
         btn = gr.Button(value="Plot Chart:")
         chart = gr.Plot()
     btn.click(graph, inputs=[time, indicator], outputs=chart)

demo.launch()