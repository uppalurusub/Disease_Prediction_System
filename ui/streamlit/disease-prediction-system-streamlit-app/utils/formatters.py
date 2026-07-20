import pandas as pd
def prediction_dataframe(result):
    if isinstance(result,dict):
        return pd.DataFrame(result.items(),columns=["Attribute","Value"])
    return pd.DataFrame({"Prediction":[result]})
