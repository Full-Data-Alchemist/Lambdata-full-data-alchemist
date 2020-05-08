import pandas as pd

def add_state_names(my_df):

    new_df = my_df.copy()
    names_map = {
        "ks":"Kan",
            "CO":"Col",
            "OK":"Okl",
            "KT":"Kenn",
            "TX":"Tex"
            }

    new_df['name'] = new_df['abbrev'].map(names_map)
    return new_df

if __name__ == "__main__":

    df = pd.DataFrame({"State":["KS", "CO", "OK","KT, TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())