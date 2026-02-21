import pandas as pd

def rename_columns(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    df.columns = df.columns.str.replace("titlê", "title", regex=False)
    df.columns = df.columns.str.replace("genrë", "genre", regex=False)
    df.columns = df.columns.str.replace("unnamed:_8", "unnamed_8", regex=False)

    return df

def remove_fully_null_columns_rows(df):
    df = df.copy()
    # look at each row
    # only drop if all values are NaN
    df = df.dropna(axis=0, how="all")
    # look at each column 
    # only drop if all values are NaN
    df = df.dropna(axis=1, how="all")

    return df


def clean_and_fill_content_rating(df):
    df = df.copy()
    # it missing replace with "Unrated"
    df["content_rating"] = df["content_rating"].fillna("Unrated")
    # replace "Not Rated" with "Unrated" to standardize
    df["content_rating"] = df["content_rating"].replace("Not Rated", "Unrated")
    return df


def clean_release_year(df):
    df = df.copy()

    # convert string to datetime, if unable then replace with NaT
    df["release_year_coerce"] = pd.to_datetime(df["release_year"], errors="coerce")
    # convert mixed date format to dateime, if unable then replace with NaT
    df["release_year_mixed"] = pd.to_datetime(df["release_year"], errors="coerce", format="mixed")

    return df

def clean_income(df):
    df = df.copy()

    # remove non numberic values
    df["income"] = (
        df["income"]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    # convert the cleaned strings to real numbers 
    df["income"] = pd.to_numeric(df["income"], errors="coerce")

    return df


