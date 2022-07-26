import pandas as pd
import env
import os
import acquire
from sklearn.model_selection import train_test_split




def null_handlers(df):
    ''' This function handles null values in zillow data by dropping all null values
    as 99 % of data sre retianed even after dropping all rows containing nulls'''
    df=df.dropna()
    return df

def optimize_types(df):
    # Convert some columns to integers
    # fips, yearbuilt, and bedrooms can be integers
    df["county_code"] = df["county_code"].astype(int)
    df["yearbuilt"] = df["yearbuilt"].astype(int)
    df["bed"] = df["bed"].astype(int)    
    df["home_estimate"] = df["home_estimate"].astype(int)
    df["sq_ft_area"] = df["sq_ft_area"].astype(int)
    return df


def handle_outliers(df):
    """Manually handle outliers that do not represent properties likely for 99% of buyers and zillow visitors"""
    df = df[df.bath <= 6]
    
    df = df[df.bed <= 6]

    df = df[df.home_estimate < 2_500_000]

    return df


def prep_zillow(df):
    """
    Acquires Zillow data
    Handles nulls
    optimizes or fixes data types
    handles outliers w/ manual logic
    returns a clean dataframe
    """

    df = null_handlers(df)

    df = optimize_types(df)

    df = handle_outliers(df)

    df.to_csv("zillow.csv", index=False)

    return df



def split_data(df, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed)
                                            
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed)
                                       
    return train, validate, test
    