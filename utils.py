
import json
import pandas as pd

def load_checklist(json_file):
    content = json.load(json_file)
    return content.get("checklist", [])

def results_to_dataframe(results):
    return pd.DataFrame(results)
