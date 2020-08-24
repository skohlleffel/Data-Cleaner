import pandas as pd

"""tempory variables"""
drop_subset = ['Email Address', 'Full Name']
partners_remove = ['Ameex Technologies']
emails_remove = ['gmail']
numeric_list = ['Job Title', 'Company Name']
capitalize_list = ['Job Title', 'Company Name']

def file_to_dataframe(path):
    if path.endswith('.csv'):
        df = pd.read_csv(path)
    elif path.endswith('.xlsx'):
        df = pd.read_excel(path)
    elif path.endswith('.json'):
        df = pd.read_json(path)
    elif path.endswith('.sql'):
        df = pd.read_sql(path)
    elif path.endswith('.html'):
        df = pd.read_html(path)
    return df

def reformat_dataframe(df, subset):
    df.dropna(subset=subset, inplace=True)
    df.fillna('', inplace=True)
    df = df.applymap(str)
    return df

def split_name_column(df):
    df[['First Name', 'Last Name']] = df['Full Name'].str.split(' ', n=1, expand=True)
    df.drop(columns='Full Name', inplace=True)
    cols = df.columns.tolist()
    cols = ['First Name'] + ['Last Name'] + [col for col in df if col != 'First Name' and col != 'Last Name']
    df = df[cols]
    return df

def remove_partners(df, partners_list):
    for index, row in df.iterrows():
        for i in partners_list:
            if i in row['Company Name']:
                df.drop(index, inplace=True)
    return df

def remove_email(df, email_list):
    for index, row in df.iterrows():
        for i in email_list:
            if i in row['Email Address']:
                df.drop(index, inplace=True)
    return df

def remove_numeric_cells(df, numeric_list):
    for i in numeric_list:
        if i in df.columns:
            for index, row in df.iterrows():
                if row[i].isnumeric():
                    df.drop(index, inplace=True)
    return df

def capitalize_columns(df, capitalize_list):
    for i in capitalize_list:
        if i in df.columns:
            df[i] = df[i].str.lower().str.capitalize()
    return df


df = pd.read_excel('data_cleaner/mock_sheets/First_Sheet.xlsx')
df = reformat_dataframe(df, drop_subset)
df = split_name_column(df)
df = remove_partners(df, partners_remove)
df = remove_email(df, emails_remove)
df = remove_numeric_cells(df, numeric_list)
df = capitalize_columns(df, capitalize_list)
df.to_csv('fixed.csv')