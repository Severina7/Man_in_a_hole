import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# TELCO Data Preparation

def split_telco_data(df):
    '''
    split_telco_data(telco) splits telco data, stratify churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test

def prep_telco_data(df):
    '''
    prep_telco_data(df) drops columns, transforms data,adds columns
    to make it ready for splitting and exploration. Some of the columns
    will be dropped from train, validate, and test because they are still
    categorical.
    '''
    # Drop duplicate columns
    df.drop(columns=['payment_type_id', \
                        'internet_service_type_id', \
                        'contract_type_id', \
                        'customer_id'], inplace=True)
       
    # Drop null values stored as whitespace    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Convert to correct datatype
    df['total_charges'] = df.total_charges.astype(float)
    
    # Bin tenure
    bins = [0, 12, 24, 36, 48, 60, 72]
    bin_names = ['1year', '2years', '3years', '4years', '5years', '6years']
    df['binned_tenure'] = pd.cut(df['tenure'], bins, labels = bin_names)

    # Convert binary categorical variables to numeric
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Get dummies for non-binary categorical variables
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'binned_tenure', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=True)
    
    # Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)

  # split the data
    train, validate, test = split_telco_data(df)
    
    return train, validate, test
