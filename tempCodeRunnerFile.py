   if indicator == 'Simple Moving Average' and time == "Date-wise":
        fig = px.line(df_date, x='date', y=['close','SMA_5', 'SMA_15'], labels={'value': 'Values'}, title='Simple Moving Average (date-wise) Chart')
        return fig
    
    elif indicator == 'Simple Moving Average' and time == "Minute-wise":
        fig = px.line(iso_data, x='time', y=['close','SMA_5', 'SMA_15'], labels={'value': 'Values'}, title='Simple Moving Average (minute-wise) Chart')
        return fig