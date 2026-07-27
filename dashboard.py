from insights import *

def founder_summary(df):

    summary = f"""
================ BUSINESS DASHBOARD ================

Total Pipeline Value:
{total_pipeline_value(df):,.2f}

----------------------------------------------------

Owner Performance

{deals_by_owner(df)}

----------------------------------------------------

Deals by Stage

{deals_by_stage(df)}

----------------------------------------------------

Sector Analysis

{sector_wise_value(df)}

----------------------------------------------------

Product Analysis

{product_wise_value(df)}

----------------------------------------------------

Top 5 Deals

{top_5_deals(df)}

====================================================
"""

    return summary