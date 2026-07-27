import pandas as pd


def _series(df, column):
    if column not in df.columns:
        return pd.Series(dtype="object")

    return df[column]


def total_pipeline_value(df):
    return _series(df, "Deal Value").sum()


def deals_by_stage(df):
    return _series(df, "Deal Stage").dropna().value_counts()


def deals_by_owner(df):
    if "Owner Code" not in df.columns or "Deal Value" not in df.columns:
        return pd.Series(dtype="float64")

    return df.groupby("Owner Code", dropna=True)["Deal Value"].sum().sort_values(ascending=False)


def top_5_deals(df):
    if "Deal Value" not in df.columns:
        return pd.DataFrame(columns=["Lead Name", "Deal Value"])

    columns = [column for column in ["Lead Name", "Deal Value"] if column in df.columns]

    return df.sort_values(
        by="Deal Value",
        ascending=False
    )[columns].head(5)


def sector_wise_value(df):
    if "Sector/Service" not in df.columns or "Deal Value" not in df.columns:
        return pd.Series(dtype="float64")

    return df.groupby(
        "Sector/Service", dropna=True
    )["Deal Value"].sum().sort_values(ascending=False)


def product_wise_value(df):
    if "Product Deal" not in df.columns or "Deal Value" not in df.columns:
        return pd.Series(dtype="float64")

    return df.groupby(
        "Product Deal", dropna=True
    )["Deal Value"].sum().sort_values(ascending=False)
