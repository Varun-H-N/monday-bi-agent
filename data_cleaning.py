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
    items = board_json["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:
        row = {"Lead Name": item["name"]}

        for column in item["column_values"]:
            row[column["id"]] = column["text"]

        rows.append(row)

    df = pd.DataFrame(rows)

    df.rename(columns=COLUMN_MAPPING, inplace=True)

    return df