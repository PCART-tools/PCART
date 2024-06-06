# %%
import numpy as np
import pandas as pd

# %%
# Load data
df = pd.read_csv("./data/aggregated/prices_all.csv.gz", compression="gzip")
df.info(verbose=True, null_counts=True)


# %%
# Missing values

# Brand
df["site_brand"].fillna(value="Unknown", inplace=True)
df.info(verbose=True, null_counts=True)
# %%
# Data types
df["siteid"] = df["siteid"].astype(str)
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y%m%d %H:%M")
df.info(verbose=True, null_counts=True)
# %%
# Corr names
df["site_brand"] = (
    df.site_brand.str.lower().str.replace(" ", "_").str.replace(r"/", "")
)
df["fuel_type"] = (
    df.fuel_type.str.lower().str.replace(" ", "_").str.replace("/", "")
)

# %%
# Cleaning prices
# >The price of 9999 denotes fuel stock that is temporarily unavailable
#  e.g. tank empty and awaiting new stock.
# change prices from 9999 to -1
df["price"] = df.price.replace(9999, -1)
# remove prices above 2500, and below 600
df["price"] = np.where(df.price > 2500, np.NaN, df.price)
df["price"] = df.price.replace(-1, 9999)  # revert back for "no fuel" to 9999
df["price"] = np.where(df.price < 600, np.NaN, df.price)
df = df.dropna()
df.info(verbose=True, null_counts=True)
# %%
# remove closed sites
closed_sites = pd.read_csv("./data/aggregated/sites_closed.csv", sep=";")
closed_sites["SiteCode"] = closed_sites["SiteCode"].astype(str)
closed_sites = closed_sites[
    closed_sites.SiteStatus == "Closed"
].SiteCode.tolist()
df_clean = df[~df.siteid.isin(closed_sites)].copy()
# %%
# save it
df_clean.to_csv(
    "./data/aggregated/prices_all_clean.csv.gz",
    index=False,
    compression="gzip",
)
# %%
