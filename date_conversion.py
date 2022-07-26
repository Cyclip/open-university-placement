import datetime as dt

def get_closest(df, col, val):
    """Get the row in the dataframe that is closest to the value

    Args:
        df (DataFrame): DataFrame to search
        col (string): Column to search
        val (any): Value to search for (or closest value to)

    Returns:
        DataFrame: Row closest to the value
    """
    return df.loc[get_closest_index(df, col, val)]


def get_closest_index(df, col,val):
    return df[col].sub(val).abs().idxmin()


def to_days(date):
    """Convert a date into an excel date (days since 1899-12-30)

    Args:
        date (DateTime): Date to convert

    Returns:
        int: Days since 1899-12-30
    """
    return (date - dt.datetime(1899, 12, 30)).days


def to_date(days):
    """Convert days since 1899-12-30 to a date

    Args:
        days (int): Number of days since 1899-12-30 (excel date)

    Returns:
        DateTime: DateTime object for excel date
    """
    return dt.datetime(1899, 12, 30) + dt.timedelta(days=days)