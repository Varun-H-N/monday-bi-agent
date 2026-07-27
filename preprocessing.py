import pandas as pd

def clean_dataframe(df):

    # Convert Deal Value to number
    df["Deal Value"] = pd.to_numeric(
        df["Deal Value"],
        errors="coerce"
    )

    # Convert dates
    df["Created Date"] = pd.to_datetime(
        df["Created Date"],
        errors="coerce"
    )

    df["Tentative Close Date"] = pd.to_datetime(
        df["Tentative Close Date"],
        errors="coerce"
    )

    df["Close Date"] = pd.to_datetime(
        df["Close Date"],
        errors="coerce"
    )

    # Replace empty strings with NA
    df.replace("", pd.NA, inplace=True)

    return df