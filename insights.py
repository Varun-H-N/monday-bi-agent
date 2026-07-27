def total_pipeline_value(df):
    return df["Deal Value"].sum()


def deals_by_stage(df):
    return df["Deal Stage"].value_counts()


def deals_by_owner(df):
    return df.groupby("Owner Code")["Deal Value"].sum().sort_values(ascending=False)


def top_5_deals(df):
    return df.sort_values(
        by="Deal Value",
        ascending=False
    )[["Lead Name", "Deal Value"]].head(5)


def sector_wise_value(df):
    return df.groupby(
        "Sector/Service"
    )["Deal Value"].sum().sort_values(ascending=False)


def product_wise_value(df):
    return df.groupby(
        "Product Deal"
    )["Deal Value"].sum().sort_values(ascending=False)