import requests
import pandas as pd
import logging

"""Clean and structure the repository and language data."""

def transform_data(repos: list[dict]) -> pd.DataFrame:
    output = []

    for repo in repos:
        lang_data =requests.get(repo["languages_url"]).json()
        #language = [lang_data.keys() if lang_data.keys() else "N/A"]
            #print(lang_data.keys()) .keys() in Python returns a specific view object, not a standard list. When you print() that object directly, Python includes the type wrapper to let you know what it is.
        output.append({"repo_name": repo["name"],
                       "languages" : list(lang_data.keys()), # if lang_data else None, 
                       "updated_at": pd.to_datetime(repo["updated_at"])
                       })
             
    df = pd.DataFrame(output)
    # If the list is empty, return None, otherwise return the list
    df['languages'] = df['languages'].apply(lambda x: x if x else None)
    return df