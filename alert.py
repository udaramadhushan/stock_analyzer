from config import  ALERT_THRESHOLD_PERCENT

def check_price_alert(symbol, df):
    latest_change = df['price_change_%'].iloc[0]

    if abs(latest_change) >= ALERT_THRESHOLD_PERCENT:
        direction = "up" if latest_change > 0 else "down"
        return f"{symbol} moved {direction} by {latest_change:.2f}%"
    
    return None
