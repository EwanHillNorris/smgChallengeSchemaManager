import pandas as pd

TYPE_MAPPING = {
    "int64": "integer",
    "object": "string",
    "float64": "float",
    "datetime64[ns]": "datetime"
}


def extract_schema(df):
    return {
        col: TYPE_MAPPING.get(str(dtype), str(dtype))
        for col, dtype in df.dtypes.items()
    }
