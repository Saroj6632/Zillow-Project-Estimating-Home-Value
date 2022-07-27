import pandas as pd
import env
import os



''' function to connect to CodeUp SQL database'''
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db}'


# new_zillow_data function runs the sql querry to connect to zillow database and returns the columns we wanted as a dataframe
def new_zillow_data():
    sql_querry= '''
            select parcelid as property_id, 
            bathroomcnt as bath, 
            bedroomcnt as bed, 
            calculatedfinishedsquarefeet as sq_ft_area, 
            yearbuilt, 
            taxvaluedollarcnt as home_estimate,
            fips as county_code 
            from properties_2017
            join predictions_2017 as pred using(parcelid)
            join propertylandusetype as prop using (propertylandusetypeid)
            where (pred.transactiondate like"2017-%%" AND prop.propertylandusedesc = "Single Family Residential")
            '''
    
    
    df= pd.read_sql(sql_querry, get_connection('zillow'))
    
    return df



# creates a csv file in local directory if not already existed
def zillow_data():
    '''this function returns the zillow data and creates the csv file in local directory  if it doesnot exist already.'''
    filename= "zillow.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read data from database in dataframe
        df= new_zillow_data()
        #cache data
        df.to_csv(filename)
        return df





