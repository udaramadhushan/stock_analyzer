from process_data import load_and_process_stock_data

def build_change_dict(symbols, frequency = 'weekly'):
    result = {}

    for symbol in symbols:
        df = load_and_process_stock_data(symbol, frequency)
        latest = df['price_change_%'].iloc[0]
        result[symbol] = latest
        
    return result
        