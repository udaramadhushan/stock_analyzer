from process_data import load_and_process_stock_data


df = load_and_process_stock_data('MSFT')
print(df[['close', 'price_change_%']].head(3))