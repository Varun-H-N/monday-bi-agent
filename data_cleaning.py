import pandas as pd

COLUMN_MAPPING = {
    "color_mm5ngxgb": "Owner Code",
    "dropdown_mm5n8mgh": "Client Code",
    "color_mm5ncs0n": "Deal Status",
    "date_mm5npzy3": "Close Date",
    "color_mm5nbk6": "Closure Probability",
    "numeric_mm5nx5ss": "Deal Value",
    "date_mm5ne27y": "Tentative Close Date",
    "color_mm5n3d0q": "Deal Stage",
    "color_mm5nvdae": "Product Deal",
    "color_mm5n2f6a": "Sector/Service",
    "date_mm5nsa35": "Created Date"
}

def board_to_dataframe(board_json):
    boards = board_json.get("data", {}).get("boards") or []

    if not boards:
        return pd.DataFrame()

    items = boards[0].get("items_page", {}).get("items", [])

    rows = []

    for item in items:
        row = {"Lead Name": item.get("name")}

        for column in item.get("column_values", []):
            row[column.get("id")] = column.get("text")

        rows.append(row)

    df = pd.DataFrame(rows)

    df.rename(columns=COLUMN_MAPPING, inplace=True)

    return df
