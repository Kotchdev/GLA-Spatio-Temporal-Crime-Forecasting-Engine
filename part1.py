# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:00.964818Z","iopub.execute_input":"2026-02-16T13:47:00.965165Z","iopub.status.idle":"2026-02-16T13:47:00.969976Z","shell.execute_reply.started":"2026-02-16T13:47:00.965137Z","shell.execute_reply":"2026-02-16T13:47:00.968863Z"},"jupyter":{"outputs_hidden":false}}
import pandas as pd

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:00.972193Z","iopub.execute_input":"2026-02-16T13:47:00.972627Z","iopub.status.idle":"2026-02-16T13:47:01.043682Z","shell.execute_reply.started":"2026-02-16T13:47:00.972599Z","shell.execute_reply":"2026-02-16T13:47:01.042514Z"},"jupyter":{"outputs_hidden":false}}
file_path = "/kaggle/input/public-transport-crime-london-dataset/public-transport-crime-london.xlsx"
raw_df = pd.read_excel(file_path, sheet_name="Volume and Rates", header=None)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.045247Z","iopub.execute_input":"2026-02-16T13:47:01.045648Z","iopub.status.idle":"2026-02-16T13:47:01.051539Z","shell.execute_reply.started":"2026-02-16T13:47:01.045607Z","shell.execute_reply":"2026-02-16T13:47:01.050709Z"},"jupyter":{"outputs_hidden":false}}
#raw_df.head(20)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.052670Z","iopub.execute_input":"2026-02-16T13:47:01.053102Z","iopub.status.idle":"2026-02-16T13:47:01.068825Z","shell.execute_reply.started":"2026-02-16T13:47:01.053057Z","shell.execute_reply":"2026-02-16T13:47:01.067482Z"},"jupyter":{"outputs_hidden":false}}
#raw_df.shape

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.071493Z","iopub.execute_input":"2026-02-16T13:47:01.071904Z","iopub.status.idle":"2026-02-16T13:47:01.127703Z","shell.execute_reply.started":"2026-02-16T13:47:01.071863Z","shell.execute_reply":"2026-02-16T13:47:01.126973Z"},"jupyter":{"outputs_hidden":false}}
modes = [
    "Bus",
    "London Underground",
    "Docklands Light Railway",
    "London Underground / Docklands Light Railway",
    "London Overground",
    "London Tramlink",
    "Trams",
    "TfL Rail",
    "Elizabeth Line",
    "All transport modes"
]

mode_rows = raw_df[raw_df.apply(lambda row: row.astype(str).str.contains("|".join(modes)).any(), axis=1)]
#mode_rows.head(20)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.128728Z","iopub.execute_input":"2026-02-16T13:47:01.129201Z","iopub.status.idle":"2026-02-16T13:47:01.176749Z","shell.execute_reply.started":"2026-02-16T13:47:01.129158Z","shell.execute_reply":"2026-02-16T13:47:01.175673Z"},"jupyter":{"outputs_hidden":false}}
fy_rows = raw_df[raw_df.apply(lambda row: row.astype(str).str.contains("Network-wide FY").any(), axis=1)]
#fy_rows

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.178191Z","iopub.execute_input":"2026-02-16T13:47:01.178680Z","iopub.status.idle":"2026-02-16T13:47:01.183869Z","shell.execute_reply.started":"2026-02-16T13:47:01.178635Z","shell.execute_reply":"2026-02-16T13:47:01.182866Z"},"jupyter":{"outputs_hidden":false}}
fy_indices = fy_rows.index.tolist()
fy_indices.append(len(raw_df))
#fy_indices

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.185327Z","iopub.execute_input":"2026-02-16T13:47:01.185705Z","iopub.status.idle":"2026-02-16T13:47:01.204008Z","shell.execute_reply.started":"2026-02-16T13:47:01.185663Z","shell.execute_reply":"2026-02-16T13:47:01.202919Z"},"jupyter":{"outputs_hidden":false}}
blocks = []

for i in range(len(fy_indices) - 1):
    start = fy_indices[i]
    end = fy_indices[i+1]
    block = raw_df.iloc[start:end]
    blocks.append(block)

#blocks[2]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.205373Z","iopub.execute_input":"2026-02-16T13:47:01.205857Z","iopub.status.idle":"2026-02-16T13:47:01.222520Z","shell.execute_reply.started":"2026-02-16T13:47:01.205818Z","shell.execute_reply":"2026-02-16T13:47:01.221220Z"},"jupyter":{"outputs_hidden":false}}
import re

def extract_financial_year(block):
    header_text = str(block.iloc[0, 0])
    match = re.search(r"FY(\d{4}/\d{2})", header_text)
    return match.group(1) if match else None
block0 = blocks[0]
#extract_financial_year(block0)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.224366Z","iopub.execute_input":"2026-02-16T13:47:01.224810Z","iopub.status.idle":"2026-02-16T13:47:01.240175Z","shell.execute_reply.started":"2026-02-16T13:47:01.224766Z","shell.execute_reply":"2026-02-16T13:47:01.239418Z"},"jupyter":{"outputs_hidden":false}}
import pandas as pd

def generate_dates(fin_year):
    start_year = int(fin_year[:4])
    months = pd.date_range(start=f"{start_year}-04-01", periods=12, freq="MS")
    return months

dates0 = generate_dates("2009/10")
#dates0

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.243401Z","iopub.execute_input":"2026-02-16T13:47:01.243750Z","iopub.status.idle":"2026-02-16T13:47:01.260221Z","shell.execute_reply.started":"2026-02-16T13:47:01.243723Z","shell.execute_reply":"2026-02-16T13:47:01.259214Z"},"jupyter":{"outputs_hidden":false}}
def get_mode_rows(block):
    return block.iloc[2:].dropna(subset=[block.columns[0]])


mode_rows0 = get_mode_rows(block0)
#mode_rows0

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.261491Z","iopub.execute_input":"2026-02-16T13:47:01.261920Z","iopub.status.idle":"2026-02-16T13:47:01.278674Z","shell.execute_reply.started":"2026-02-16T13:47:01.261891Z","shell.execute_reply":"2026-02-16T13:47:01.277702Z"},"jupyter":{"outputs_hidden":false}}
#get_mode_rows(blocks[13])

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.279895Z","iopub.execute_input":"2026-02-16T13:47:01.280228Z","iopub.status.idle":"2026-02-16T13:47:01.296809Z","shell.execute_reply.started":"2026-02-16T13:47:01.280193Z","shell.execute_reply":"2026-02-16T13:47:01.295846Z"},"jupyter":{"outputs_hidden":false}}
def split_vol_rate(row):
    values = row.iloc[1:].tolist()  # skip the mode name
    volumes = values[0::2]          # even positions
    rates = values[1::2]            # odd positions
    return volumes, rates

volumes0, rates0 = split_vol_rate(mode_rows0.iloc[0])
#volumes0, rates0

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.297925Z","iopub.execute_input":"2026-02-16T13:47:01.298603Z","iopub.status.idle":"2026-02-16T13:47:01.313689Z","shell.execute_reply.started":"2026-02-16T13:47:01.298575Z","shell.execute_reply":"2026-02-16T13:47:01.312642Z"},"jupyter":{"outputs_hidden":false}}
def build_mode_rows(mode_name, volumes, rates, dates):
    rows = []
    for date, vol, rate in zip(dates, volumes, rates):
        rows.append({
            "date": date,
            "mode": mode_name,
            "volume": vol,
            "rate": rate
        })
    return rows

bus_rows0 = build_mode_rows("Bus", volumes0, rates0, dates0)
#bus_rows0[:3]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.314917Z","iopub.execute_input":"2026-02-16T13:47:01.315338Z","iopub.status.idle":"2026-02-16T13:47:01.341179Z","shell.execute_reply.started":"2026-02-16T13:47:01.315260Z","shell.execute_reply":"2026-02-16T13:47:01.340192Z"},"jupyter":{"outputs_hidden":false}}
def block_to_long(block):
    fin_year = extract_financial_year(block)
    dates = generate_dates(fin_year)
    mode_rows = get_mode_rows(block)

    long_rows = []

    for _, row in mode_rows.iterrows():
        mode_name = row.iloc[0]
        volumes, rates = split_vol_rate(row)
        long_rows.extend(build_mode_rows(mode_name, volumes, rates, dates))

    return pd.DataFrame(long_rows)

long_block0 = block_to_long(block0)
#long_block0

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.342467Z","iopub.execute_input":"2026-02-16T13:47:01.342743Z","iopub.status.idle":"2026-02-16T13:47:01.411933Z","shell.execute_reply.started":"2026-02-16T13:47:01.342713Z","shell.execute_reply":"2026-02-16T13:47:01.411079Z"},"jupyter":{"outputs_hidden":false}}
long_blocks = []

for block in blocks:
    long_df = block_to_long(block)
    long_blocks.append(long_df)

full_long_df = pd.concat(long_blocks, ignore_index=True)
#full_long_df

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.413203Z","iopub.execute_input":"2026-02-16T13:47:01.413785Z","iopub.status.idle":"2026-02-16T13:47:01.429903Z","shell.execute_reply.started":"2026-02-16T13:47:01.413751Z","shell.execute_reply":"2026-02-16T13:47:01.428988Z"},"jupyter":{"outputs_hidden":false}}
#full_long_df["mode"].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.431042Z","iopub.execute_input":"2026-02-16T13:47:01.431393Z","iopub.status.idle":"2026-02-16T13:47:01.449897Z","shell.execute_reply.started":"2026-02-16T13:47:01.431266Z","shell.execute_reply":"2026-02-16T13:47:01.448854Z"},"jupyter":{"outputs_hidden":false}}
#for i, block in enumerate(blocks):
#    print(i, block.iloc[:,0].dropna().tolist())

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.451254Z","iopub.execute_input":"2026-02-16T13:47:01.451609Z","iopub.status.idle":"2026-02-16T13:47:01.467516Z","shell.execute_reply.started":"2026-02-16T13:47:01.451584Z","shell.execute_reply":"2026-02-16T13:47:01.466344Z"},"jupyter":{"outputs_hidden":false}}
#full_long_df

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.468638Z","iopub.execute_input":"2026-02-16T13:47:01.469575Z","iopub.status.idle":"2026-02-16T13:47:01.486585Z","shell.execute_reply.started":"2026-02-16T13:47:01.469533Z","shell.execute_reply":"2026-02-16T13:47:01.485429Z"},"jupyter":{"outputs_hidden":false}}
clean_df = full_long_df.copy()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.487928Z","iopub.execute_input":"2026-02-16T13:47:01.488327Z","iopub.status.idle":"2026-02-16T13:47:01.509250Z","shell.execute_reply.started":"2026-02-16T13:47:01.488262Z","shell.execute_reply":"2026-02-16T13:47:01.508018Z"},"jupyter":{"outputs_hidden":false}}
clean_df["mode"] = clean_df["mode"].replace({
    "London Tramlink": "Tram",
    "Trams": "Tram",
    "Tramlink": "Tram",
    "London Trams": "Tram",
    "London Underground / Docklands Light Railway": "LU+DLR",
    "London Underground": "LU",
    "Docklands Light Railway": "DLR",
    "TfL Rail": "TfL Rail",
    "Elizabeth Line (formerly TfL Rail)": "Elizabeth Line"
})

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.510655Z","iopub.execute_input":"2026-02-16T13:47:01.511044Z","iopub.status.idle":"2026-02-16T13:47:01.524100Z","shell.execute_reply.started":"2026-02-16T13:47:01.511016Z","shell.execute_reply":"2026-02-16T13:47:01.523120Z"},"jupyter":{"outputs_hidden":false}}
#clean_df["mode"].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.525414Z","iopub.execute_input":"2026-02-16T13:47:01.525842Z","iopub.status.idle":"2026-02-16T13:47:01.543214Z","shell.execute_reply.started":"2026-02-16T13:47:01.525803Z","shell.execute_reply":"2026-02-16T13:47:01.542202Z"},"jupyter":{"outputs_hidden":false}}
combined_dates = clean_df.loc[clean_df["mode"] == "LU+DLR", "date"].unique()
#combined_dates[:10]  # preview

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.544556Z","iopub.execute_input":"2026-02-16T13:47:01.544884Z","iopub.status.idle":"2026-02-16T13:47:01.561123Z","shell.execute_reply.started":"2026-02-16T13:47:01.544858Z","shell.execute_reply":"2026-02-16T13:47:01.560273Z"},"jupyter":{"outputs_hidden":false}}
separate_dates = clean_df.loc[clean_df["mode"].isin(["LU", "DLR"]), "date"].unique()
#separate_dates[:10]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.562595Z","iopub.execute_input":"2026-02-16T13:47:01.562862Z","iopub.status.idle":"2026-02-16T13:47:01.579023Z","shell.execute_reply.started":"2026-02-16T13:47:01.562836Z","shell.execute_reply":"2026-02-16T13:47:01.578203Z"},"jupyter":{"outputs_hidden":false}}
separate = clean_df[clean_df["mode"].isin(["LU", "DLR"])]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.580403Z","iopub.execute_input":"2026-02-16T13:47:01.581397Z","iopub.status.idle":"2026-02-16T13:47:01.643025Z","shell.execute_reply.started":"2026-02-16T13:47:01.581367Z","shell.execute_reply":"2026-02-16T13:47:01.642193Z"},"jupyter":{"outputs_hidden":false}}
combined_lu_dlr = (
    separate
    .groupby("date")
    .apply(
        lambda g: pd.Series({
            "mode": "LU+DLR",
            "volume": g["volume"].sum(),
            "rate": (g["volume"] * g["rate"]).sum() / g["volume"].sum()
        }),
        include_groups=False
    )
    .reset_index()
)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.644149Z","iopub.execute_input":"2026-02-16T13:47:01.644459Z","iopub.status.idle":"2026-02-16T13:47:01.655964Z","shell.execute_reply.started":"2026-02-16T13:47:01.644436Z","shell.execute_reply":"2026-02-16T13:47:01.654928Z"},"jupyter":{"outputs_hidden":false}}
clean_df_no_lu_dlr = clean_df[~clean_df["mode"].isin(["LU", "DLR"])]
clean_df_combined = pd.concat([clean_df_no_lu_dlr, combined_lu_dlr], ignore_index=True)
clean_df_combined = clean_df_combined.sort_values(["date", "mode"]).reset_index(drop=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.662777Z","iopub.execute_input":"2026-02-16T13:47:01.663509Z","iopub.status.idle":"2026-02-16T13:47:01.672676Z","shell.execute_reply.started":"2026-02-16T13:47:01.663469Z","shell.execute_reply":"2026-02-16T13:47:01.671421Z"},"jupyter":{"outputs_hidden":false}}
has_all = clean_df_combined["mode"] == "All transport modes"
dates_with_all = clean_df_combined.loc[has_all, "date"].unique()

dates_missing_all = clean_df_combined.loc[
    ~clean_df_combined["date"].isin(dates_with_all),
    "date"
].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.674015Z","iopub.execute_input":"2026-02-16T13:47:01.675679Z","iopub.status.idle":"2026-02-16T13:47:01.693182Z","shell.execute_reply.started":"2026-02-16T13:47:01.675647Z","shell.execute_reply":"2026-02-16T13:47:01.692185Z"},"jupyter":{"outputs_hidden":false}}
clean_df_combined["volume"] = (
    clean_df_combined["volume"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

clean_df_combined["rate"] = (
    clean_df_combined["rate"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.694655Z","iopub.execute_input":"2026-02-16T13:47:01.695071Z","iopub.status.idle":"2026-02-16T13:47:01.715986Z","shell.execute_reply.started":"2026-02-16T13:47:01.695018Z","shell.execute_reply":"2026-02-16T13:47:01.714768Z"},"jupyter":{"outputs_hidden":false}}
clean_df_combined["volume"] = pd.to_numeric(clean_df_combined["volume"], errors="coerce")
clean_df_combined["rate"] = pd.to_numeric(clean_df_combined["rate"], errors="coerce")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.717403Z","iopub.execute_input":"2026-02-16T13:47:01.717851Z","iopub.status.idle":"2026-02-16T13:47:01.735924Z","shell.execute_reply.started":"2026-02-16T13:47:01.717797Z","shell.execute_reply":"2026-02-16T13:47:01.734818Z"},"jupyter":{"outputs_hidden":false}}
subset = clean_df_combined[clean_df_combined["date"].isin(dates_missing_all)]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.737270Z","iopub.execute_input":"2026-02-16T13:47:01.738053Z","iopub.status.idle":"2026-02-16T13:47:01.753765Z","shell.execute_reply.started":"2026-02-16T13:47:01.738008Z","shell.execute_reply":"2026-02-16T13:47:01.752882Z"},"jupyter":{"outputs_hidden":false}}
#subset[subset["volume"].apply(lambda x: isinstance(x, str))]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.755084Z","iopub.execute_input":"2026-02-16T13:47:01.755556Z","iopub.status.idle":"2026-02-16T13:47:01.830593Z","shell.execute_reply.started":"2026-02-16T13:47:01.755509Z","shell.execute_reply":"2026-02-16T13:47:01.829786Z"},"jupyter":{"outputs_hidden":false}}
all_modes_rows = (
    subset
    .groupby("date")
    .apply(
        lambda g: pd.Series({
            "mode": "All transport modes",
            "volume": g["volume"].sum(),
            "rate": (g[g["rate"].notna()]["volume"] * g[g["rate"].notna()]["rate"]).sum()
                    / g[g["rate"].notna()]["volume"].sum()
        }),
        include_groups=False
    )
    .reset_index()
)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.831640Z","iopub.execute_input":"2026-02-16T13:47:01.831876Z","iopub.status.idle":"2026-02-16T13:47:01.837967Z","shell.execute_reply.started":"2026-02-16T13:47:01.831854Z","shell.execute_reply":"2026-02-16T13:47:01.836906Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all = pd.concat([clean_df_combined, all_modes_rows], ignore_index=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.839568Z","iopub.execute_input":"2026-02-16T13:47:01.839986Z","iopub.status.idle":"2026-02-16T13:47:01.856244Z","shell.execute_reply.started":"2026-02-16T13:47:01.839959Z","shell.execute_reply":"2026-02-16T13:47:01.855240Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all = clean_df_with_all.sort_values(["date", "mode"]).reset_index(drop=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.857496Z","iopub.execute_input":"2026-02-16T13:47:01.858026Z","iopub.status.idle":"2026-02-16T13:47:01.865493Z","shell.execute_reply.started":"2026-02-16T13:47:01.857998Z","shell.execute_reply":"2026-02-16T13:47:01.864543Z"},"jupyter":{"outputs_hidden":false}}
#clean_df_with_all["mode"].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.866716Z","iopub.execute_input":"2026-02-16T13:47:01.867135Z","iopub.status.idle":"2026-02-16T13:47:01.930895Z","shell.execute_reply.started":"2026-02-16T13:47:01.867100Z","shell.execute_reply":"2026-02-16T13:47:01.929759Z"},"jupyter":{"outputs_hidden":false}}
long_blocks = [block_to_long(b) for b in blocks]
full_long_df = pd.concat(long_blocks, ignore_index=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.932250Z","iopub.execute_input":"2026-02-16T13:47:01.932614Z","iopub.status.idle":"2026-02-16T13:47:01.955332Z","shell.execute_reply.started":"2026-02-16T13:47:01.932586Z","shell.execute_reply":"2026-02-16T13:47:01.954181Z"},"jupyter":{"outputs_hidden":false}}
#full_long_df["mode"].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.956583Z","iopub.execute_input":"2026-02-16T13:47:01.956934Z","iopub.status.idle":"2026-02-16T13:47:01.975631Z","shell.execute_reply.started":"2026-02-16T13:47:01.956899Z","shell.execute_reply":"2026-02-16T13:47:01.974791Z"},"jupyter":{"outputs_hidden":false}}
lu_rows = full_long_df[full_long_df["mode"] == "London Underground"]
dlr_rows = full_long_df[full_long_df["mode"] == "Docklands Light Railway"]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.976845Z","iopub.execute_input":"2026-02-16T13:47:01.977247Z","iopub.status.idle":"2026-02-16T13:47:01.995802Z","shell.execute_reply.started":"2026-02-16T13:47:01.977209Z","shell.execute_reply":"2026-02-16T13:47:01.994748Z"},"jupyter":{"outputs_hidden":false}}
lu_dlr = lu_rows.merge(
    dlr_rows,
    on="date",
    suffixes=("_lu", "_dlr")
)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:01.997064Z","iopub.execute_input":"2026-02-16T13:47:01.997777Z","iopub.status.idle":"2026-02-16T13:47:02.015986Z","shell.execute_reply.started":"2026-02-16T13:47:01.997736Z","shell.execute_reply":"2026-02-16T13:47:02.014928Z"},"jupyter":{"outputs_hidden":false}}
lu_dlr["volume"] = lu_dlr["volume_lu"] + lu_dlr["volume_dlr"]

lu_dlr["rate"] = (
    lu_dlr["volume_lu"] * lu_dlr["rate_lu"] +
    lu_dlr["volume_dlr"] * lu_dlr["rate_dlr"]
) / lu_dlr["volume"]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.017321Z","iopub.execute_input":"2026-02-16T13:47:02.018395Z","iopub.status.idle":"2026-02-16T13:47:02.037641Z","shell.execute_reply.started":"2026-02-16T13:47:02.018350Z","shell.execute_reply":"2026-02-16T13:47:02.036382Z"},"jupyter":{"outputs_hidden":false}}
lu_dlr_combined = lu_dlr[["date", "volume", "rate"]].copy()
lu_dlr_combined["mode"] = "LU+DLR"

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.038920Z","iopub.execute_input":"2026-02-16T13:47:02.039374Z","iopub.status.idle":"2026-02-16T13:47:02.057645Z","shell.execute_reply.started":"2026-02-16T13:47:02.039330Z","shell.execute_reply":"2026-02-16T13:47:02.056764Z"},"jupyter":{"outputs_hidden":false}}
clean_df = pd.concat([clean_df, lu_dlr_combined], ignore_index=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.058731Z","iopub.execute_input":"2026-02-16T13:47:02.059098Z","iopub.status.idle":"2026-02-16T13:47:02.079769Z","shell.execute_reply.started":"2026-02-16T13:47:02.059071Z","shell.execute_reply":"2026-02-16T13:47:02.078705Z"},"jupyter":{"outputs_hidden":false}}
clean_df = clean_df.copy()


clean_df["volume"] = pd.to_numeric(clean_df["volume"], errors="coerce")
clean_df["rate"] = pd.to_numeric(clean_df["rate"], errors="coerce")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.080917Z","iopub.execute_input":"2026-02-16T13:47:02.081235Z","iopub.status.idle":"2026-02-16T13:47:02.332054Z","shell.execute_reply.started":"2026-02-16T13:47:02.081209Z","shell.execute_reply":"2026-02-16T13:47:02.331066Z"},"jupyter":{"outputs_hidden":false}}
grouped = clean_df.groupby("date")

all_modes_rows = []

for date, group in grouped:
    # Total volume always includes all modes
    total_volume = group["volume"].sum()

    # Filter modes with valid rates for weighted average
    valid = group.dropna(subset=["rate"])

    # Weighted rate
    weighted_rate = (valid["volume"] * valid["rate"]).sum() / valid["volume"].sum()

    all_modes_rows.append({
        "date": date,
        "mode": "All transport modes",
        "volume": total_volume,
        "rate": weighted_rate
    })

all_modes_df = pd.DataFrame(all_modes_rows)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.333375Z","iopub.execute_input":"2026-02-16T13:47:02.333655Z","iopub.status.idle":"2026-02-16T13:47:02.340804Z","shell.execute_reply.started":"2026-02-16T13:47:02.333618Z","shell.execute_reply":"2026-02-16T13:47:02.339380Z"},"jupyter":{"outputs_hidden":false}}
clean_df_no_all = clean_df[clean_df["mode"] != "All transport modes"]

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.342037Z","iopub.execute_input":"2026-02-16T13:47:02.342877Z","iopub.status.idle":"2026-02-16T13:47:02.362371Z","shell.execute_reply.started":"2026-02-16T13:47:02.342844Z","shell.execute_reply":"2026-02-16T13:47:02.361207Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all = pd.concat([clean_df_no_all, all_modes_df], ignore_index=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.363900Z","iopub.execute_input":"2026-02-16T13:47:02.364552Z","iopub.status.idle":"2026-02-16T13:47:02.380391Z","shell.execute_reply.started":"2026-02-16T13:47:02.364521Z","shell.execute_reply":"2026-02-16T13:47:02.379148Z"},"jupyter":{"outputs_hidden":false}}
#clean_df_with_all[clean_df_with_all["mode"] == "All transport modes"].head()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.381795Z","iopub.execute_input":"2026-02-16T13:47:02.382153Z","iopub.status.idle":"2026-02-16T13:47:02.399016Z","shell.execute_reply.started":"2026-02-16T13:47:02.382088Z","shell.execute_reply":"2026-02-16T13:47:02.397913Z"},"jupyter":{"outputs_hidden":false}}
mode_mapping = {
    "London Tramlink": "Trams",
    "Trams": "Trams",
    "TfL Rail": "Elizabeth Line",
    "Elizabeth Line (formerly TfL Rail)": "Elizabeth Line"
}

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.400273Z","iopub.execute_input":"2026-02-16T13:47:02.401003Z","iopub.status.idle":"2026-02-16T13:47:02.419231Z","shell.execute_reply.started":"2026-02-16T13:47:02.400973Z","shell.execute_reply":"2026-02-16T13:47:02.418394Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all["mode"] = clean_df_with_all["mode"].replace(mode_mapping)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.420463Z","iopub.execute_input":"2026-02-16T13:47:02.420979Z","iopub.status.idle":"2026-02-16T13:47:02.436743Z","shell.execute_reply.started":"2026-02-16T13:47:02.420952Z","shell.execute_reply":"2026-02-16T13:47:02.435665Z"},"jupyter":{"outputs_hidden":false}}
#clean_df_with_all["mode"].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.438061Z","iopub.execute_input":"2026-02-16T13:47:02.438478Z","iopub.status.idle":"2026-02-16T13:47:02.460558Z","shell.execute_reply.started":"2026-02-16T13:47:02.438450Z","shell.execute_reply":"2026-02-16T13:47:02.459398Z"},"jupyter":{"outputs_hidden":false}}
#sorted(clean_df_with_all["mode"].unique())

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.461772Z","iopub.execute_input":"2026-02-16T13:47:02.462192Z","iopub.status.idle":"2026-02-16T13:47:02.480411Z","shell.execute_reply.started":"2026-02-16T13:47:02.462163Z","shell.execute_reply":"2026-02-16T13:47:02.479424Z"},"jupyter":{"outputs_hidden":false}}
#"LU+DLR" in clean_df_with_all["mode"].unique()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.481759Z","iopub.execute_input":"2026-02-16T13:47:02.482201Z","iopub.status.idle":"2026-02-16T13:47:02.499503Z","shell.execute_reply.started":"2026-02-16T13:47:02.482156Z","shell.execute_reply":"2026-02-16T13:47:02.498624Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all["mode"] = clean_df_with_all["mode"].replace({
    "London Underground / Docklands Light Railway": "LU+DLR"
})

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.500703Z","iopub.execute_input":"2026-02-16T13:47:02.501617Z","iopub.status.idle":"2026-02-16T13:47:02.518894Z","shell.execute_reply.started":"2026-02-16T13:47:02.501572Z","shell.execute_reply":"2026-02-16T13:47:02.517947Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all = clean_df_with_all.rename(columns={
    "volume": "journeys_millions",
    "rate": "crime_rate"
})

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.519976Z","iopub.execute_input":"2026-02-16T13:47:02.520209Z","iopub.status.idle":"2026-02-16T13:47:02.538979Z","shell.execute_reply.started":"2026-02-16T13:47:02.520187Z","shell.execute_reply":"2026-02-16T13:47:02.537521Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all = clean_df_with_all.sort_values(["date", "mode"]).reset_index(drop=True)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.540357Z","iopub.execute_input":"2026-02-16T13:47:02.540723Z","iopub.status.idle":"2026-02-16T13:47:02.559216Z","shell.execute_reply.started":"2026-02-16T13:47:02.540692Z","shell.execute_reply":"2026-02-16T13:47:02.557977Z"},"jupyter":{"outputs_hidden":false}}
cols_to_drop = [col for col in clean_df_with_all.columns if col.endswith("_lu") or col.endswith("_dlr")]
clean_df_with_all = clean_df_with_all.drop(columns=cols_to_drop, errors="ignore")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.560592Z","iopub.execute_input":"2026-02-16T13:47:02.560997Z","iopub.status.idle":"2026-02-16T13:47:02.579064Z","shell.execute_reply.started":"2026-02-16T13:47:02.560969Z","shell.execute_reply":"2026-02-16T13:47:02.577984Z"},"jupyter":{"outputs_hidden":false}}
#clean_df_with_all.head()
#clean_df_with_all["mode"].unique()
#clean_df_with_all.info()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.580417Z","iopub.execute_input":"2026-02-16T13:47:02.580824Z","iopub.status.idle":"2026-02-16T13:47:02.596822Z","shell.execute_reply.started":"2026-02-16T13:47:02.580766Z","shell.execute_reply":"2026-02-16T13:47:02.595786Z"},"jupyter":{"outputs_hidden":false}}
#sorted(clean_df_with_all["mode"].unique())

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.598162Z","iopub.execute_input":"2026-02-16T13:47:02.598608Z","iopub.status.idle":"2026-02-16T13:47:02.618185Z","shell.execute_reply.started":"2026-02-16T13:47:02.598567Z","shell.execute_reply":"2026-02-16T13:47:02.617106Z"},"jupyter":{"outputs_hidden":false}}
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact, SelectMultiple

sns.set(style="whitegrid")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.619421Z","iopub.execute_input":"2026-02-16T13:47:02.619826Z","iopub.status.idle":"2026-02-16T13:47:02.636062Z","shell.execute_reply.started":"2026-02-16T13:47:02.619782Z","shell.execute_reply":"2026-02-16T13:47:02.635161Z"},"jupyter":{"outputs_hidden":false}}
modes = sorted(clean_df_with_all["mode"].unique())
#modes

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.637152Z","iopub.execute_input":"2026-02-16T13:47:02.637751Z","iopub.status.idle":"2026-02-16T13:47:02.655509Z","shell.execute_reply.started":"2026-02-16T13:47:02.637721Z","shell.execute_reply":"2026-02-16T13:47:02.654234Z"},"jupyter":{"outputs_hidden":false}}
def plot_rates(selected_modes):
    if isinstance(selected_modes, str):
        selected_modes = [selected_modes]

    df_plot = clean_df_with_all[clean_df_with_all["mode"].isin(selected_modes)]

    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df_plot,
        x="date",
        y="crime_rate",
        hue="mode",
        palette="tab10"
    )
    plt.title("Crime rate over time by transport mode")
    plt.xlabel("Date")
    plt.ylabel("Crime rate (per million journeys)")
    plt.legend(title="Mode", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.656929Z","iopub.execute_input":"2026-02-16T13:47:02.657347Z","iopub.status.idle":"2026-02-16T13:47:02.973322Z","shell.execute_reply.started":"2026-02-16T13:47:02.657303Z","shell.execute_reply":"2026-02-16T13:47:02.972520Z"},"jupyter":{"outputs_hidden":false}}
interact(
    plot_rates,
    selected_modes=SelectMultiple(
        options=modes,
        value=("All transport modes",),
        description="Modes",
        disabled=False
    )
)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:02.974439Z","iopub.execute_input":"2026-02-16T13:47:02.974783Z","iopub.status.idle":"2026-02-16T13:47:08.163687Z","shell.execute_reply.started":"2026-02-16T13:47:02.974754Z","shell.execute_reply":"2026-02-16T13:47:08.162526Z"},"jupyter":{"outputs_hidden":false}}
for mode in modes:
    df_plot = clean_df_with_all[clean_df_with_all["mode"] == mode]

    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df_plot,
        x="date",
        y="crime_rate",
        hue="mode",
        palette="tab10"
    )
    plt.title(f"Crime rate over time — {mode}")
    plt.xlabel("Date")
    plt.ylabel("Crime rate (per million journeys)")
    plt.tight_layout()

    filename = f"crime_rates_{mode.replace(' ', '_')}.png"
    plt.savefig(filename, dpi=300)
    plt.close()

    print("Saved:", filename)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:08.165258Z","iopub.execute_input":"2026-02-16T13:47:08.165729Z","iopub.status.idle":"2026-02-16T13:47:08.667722Z","shell.execute_reply.started":"2026-02-16T13:47:08.165691Z","shell.execute_reply":"2026-02-16T13:47:08.666874Z"},"jupyter":{"outputs_hidden":false}}
# Plot all modes together
plt.figure(figsize=(14, 7))

sns.scatterplot(
    data=clean_df_with_all,
    x="date",
    y="crime_rate",
    hue="mode",
    palette="tab10"
)

plt.title("Crime rate over time — ALL transport modes")
plt.xlabel("Date")
plt.ylabel("Crime rate (per million journeys)")
plt.legend(title="Mode", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# SHOW the plot
plt.show()

# Save PNG
plt.savefig("crime_rates_ALL_MODES.png", dpi=300)
plt.close()

print("Saved: crime_rates_ALL_MODES.png")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:08.669326Z","iopub.execute_input":"2026-02-16T13:47:08.669709Z","iopub.status.idle":"2026-02-16T13:47:09.170856Z","shell.execute_reply.started":"2026-02-16T13:47:08.669680Z","shell.execute_reply":"2026-02-16T13:47:09.169736Z"},"jupyter":{"outputs_hidden":false}}
# Use the full cleaned dataset
df_plot = clean_df_with_all.copy()

# Create the figure
plt.figure(figsize=(14, 7))

sns.scatterplot(
    data=df_plot,
    x="date",
    y="journeys_millions",
    hue="mode",
    palette="tab10"
)

plt.title("Journey volumes over time — ALL transport modes")
plt.xlabel("Date")
plt.ylabel("Journeys (millions)")
plt.legend(title="Mode", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# SHOW the plot
plt.show()

# SAVE the plot
plt.savefig("journey_volumes_ALL_MODES.png", dpi=300)
plt.close()

print("Saved: journey_volumes_ALL_MODES.png")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:09.172050Z","iopub.execute_input":"2026-02-16T13:47:09.172586Z","iopub.status.idle":"2026-02-16T13:47:09.184854Z","shell.execute_reply.started":"2026-02-16T13:47:09.172525Z","shell.execute_reply":"2026-02-16T13:47:09.183631Z"},"jupyter":{"outputs_hidden":false}}
from ipywidgets import interact, Dropdown

modes = sorted(clean_df_with_all["mode"].unique())

def compare_two_modes(mode1, mode2):
    if mode1 == mode2:
        print("Please choose two different modes.")
        return
    
    # Extract the two series
    df1 = clean_df_with_all[clean_df_with_all["mode"] == mode1][["date", "crime_rate"]]
    df2 = clean_df_with_all[clean_df_with_all["mode"] == mode2][["date", "crime_rate"]]
    
    # Merge on date
    merged = df1.merge(df2, on="date", suffixes=(f"_{mode1}", f"_{mode2}"))
    
    # Compute correlation
    corr = merged[f"crime_rate_{mode1}"].corr(merged[f"crime_rate_{mode2}"])
    
    print(f"Correlation between {mode1} and {mode2}: {corr:.3f}")
    
    # Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x=merged[f"crime_rate_{mode1}"],
        y=merged[f"crime_rate_{mode2}"]
    )
    
    plt.title(f"Crime rate comparison: {mode1} vs {mode2}")
    plt.xlabel(f"{mode1} crime rate")
    plt.ylabel(f"{mode2} crime rate")
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
    # Save PNG
    filename = f"crime_rate_comparison_{mode1.replace(' ', '_')}_vs_{mode2.replace(' ', '_')}.png"
    plt.savefig(filename, dpi=300)
    plt.close()
    
    print(f"Saved: {filename}")

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:09.186347Z","iopub.execute_input":"2026-02-16T13:47:09.187160Z","iopub.status.idle":"2026-02-16T13:47:09.227921Z","shell.execute_reply.started":"2026-02-16T13:47:09.187128Z","shell.execute_reply":"2026-02-16T13:47:09.226916Z"},"jupyter":{"outputs_hidden":false}}
interact(
    compare_two_modes,
    mode1=Dropdown(options=modes, description="Mode 1"),
    mode2=Dropdown(options=modes, description="Mode 2")
)

# %% [code] {"execution":{"iopub.status.busy":"2026-02-16T13:47:09.229238Z","iopub.execute_input":"2026-02-16T13:47:09.229636Z","iopub.status.idle":"2026-02-16T13:47:09.346807Z","shell.execute_reply.started":"2026-02-16T13:47:09.229593Z","shell.execute_reply":"2026-02-16T13:47:09.345732Z"},"jupyter":{"outputs_hidden":false}}
clean_df_with_all.to_excel(
    "final_tfl_cleaned_dataset.xlsx",
    index=False,
    na_rep="N/A"
)
