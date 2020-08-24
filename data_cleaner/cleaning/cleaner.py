import pandas as pd

"""tempory variables"""
# drop_empty_list = ['Email Address', 'Full Name']
# partners_remove = ['Ameex Technologies']
# emails_remove = ['gmail']
# numeric_list = ['Job Title', 'Company Name']
# capitalize_list = ['Job Title', 'Company Name']

def file_to_dataframe(path):
    # if path.endswith('.csv'):
    #     df = pd.read_csv(path)
    # elif path.endswith('.xlsx'):
    df = pd.read_excel(path)
    # elif path.endswith('.json'):
    #     df = pd.read_json(path)
    # elif path.endswith('.sql'):
    #     df = pd.read_sql(path)
    # elif path.endswith('.html'):
    #     df = pd.read_html(path)
    return df

def reformat_dataframe(df, drop_empty_list):
    if drop_empty_list:
        df.dropna(subset=drop_empty_list, inplace=True)
    df.fillna('', inplace=True)
    df = df.applymap(str)
    return df

def split_name_column(df):
    if 'Full Name' in df.columns:
        df[['First Name', 'Last Name']] = df['Full Name'].str.split(' ', n=1, expand=True)
        df.drop(columns='Full Name', inplace=True)
        cols = df.columns.tolist()
        cols = ['First Name'] + ['Last Name'] + [col for col in df if col != 'First Name' and col != 'Last Name']
        df = df[cols]
    return df

def remove_partners(df, partners_list):
    if partners_list:
        for index, row in df.iterrows():
            for i in partners_list:
                if i in row['Company Name']:
                    df.drop(index, inplace=True)
    return df


def remove_emails(df, email_list):
    if email_list:
        for index, row in df.iterrows():
            for i in email_list:
                if i in row['Email Address']:
                    df.drop(index, inplace=True)
    return df


def remove_numeric_cells(df, numeric_list):
    if numeric_list:
        for i in numeric_list:
            if i in df.columns:
                for index, row in df.iterrows():
                    if row[i].isnumeric():
                        df.drop(index, inplace=True)
    return df


def capitalize_columns(df, capitalize_list):
    if capitalize_list:
        for i in capitalize_list:
            if i in df.columns:
                df[i] = df[i].str.lower().str.capitalize()
    return df

def convert_pd_df(df):
    cleaned_file = df.to_csv()
    return cleaned_file



def get_cleaned_file(path, capitalize_list=None, numeric_list=None, email_list=None, partners_list=None, drop_empty_list=None):
    """main function"""

    if not path:
        raise ValueError('A file has not been added.')
    
    df = file_to_dataframe(path)
    formatted_df = reformat_dataframe(df, drop_empty_list)
    refactored_names_df = split_name_column(formatted_df)
    removed_partners_df = remove_partners(refactored_names_df, partners_list)
    removed_email_df = remove_emails(removed_partners_df, email_list)
    removed_numeric_df = remove_numeric_cells(removed_email_df, numeric_list)
    cleaned_df = capitalize_columns(removed_numeric_df, capitalize_list)
    cleaned_file = convert_pd_df(cleaned_df)
    return cleaned_file

