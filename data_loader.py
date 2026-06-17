import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"✅ Loaded data for {len(df)} students.")
    return df