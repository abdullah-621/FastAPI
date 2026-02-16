import pandas as pd
get_data = {
    'bmi' : 20,
    'age_group' : 20,
    'lifestyle_risk' : 20,
    'city_tier' : 20,
    'income_lpa' : 20,
    'occupation' : 20
  }

input_df = pd.DataFrame([get_data])
print(input_df)