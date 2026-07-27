import pandas as pd


DATE_COLUMNS = ["Created Date", "Tentative Close Date", "Close Date"]


def clean_dataframe(df):
    df = df.copy()

    if df.empty:
        return df

    # Convert Deal Value to number
    if "Deal Value" not in df.columns:
        df["Deal Value"] = 0

    df["Deal Value"] = pd.to_numeric(df["Deal Value"], errors="coerce").fillna(0)

    # Convert dates
    for column in DATE_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    # Replace empty strings with NA
    df.replace("", pd.NA, inplace=True)

    return df
