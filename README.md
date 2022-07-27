# Regression Project

## PROJECT GOALS:
- The main objective of this project is to identify key features that influence the value of Single Family Properties that were sold in 2017.
- Build a regression model to predict the property value.

## PROJECT DESCRIPTION:
In this project different features that has influence on determining the home value will be analyzed to predict the home value. Different regression model will becreated and the  model performing best overall will be choosen.

## INITIAL QUESTIONS:
- Does number of bedrooms have influence on home value?
- Does number of bathrooms determines the price of the property?
- Does interior area(in sq.feet) adds value to the property?
- Does the county_code have huge influence in property value estimate?


## DATA DICTIONARY:
#### Single Family Properties
- Property Id
- Bed : no of bedrooms
- bath : no.of bathrooms
- sq_ft_area : total finished square foot area of the property
- yearbuilt: year that property was build
- home_estimate: House evaluated value
- county_code : county zone whre the propety is located

## STEPS TO REPRODUCE MY WORK:
 In order to reproduce my final report and the model following process should be followed
- env.py file that has credentials for successful connection with CodeUp DB Server.
- clone my project repo(including aquire.py and prepare.py). 
- libraries to be used are pandas, matplotlib, seaborn, numpy, sklearn
- finally you should be able to run final_project report.

## PROJECT PLANNING:
- Create acquire and prepare module 
- these two are user defined functions for data acquisition and preparing a clean data. 
- acquire function is tested and added to acquire.py module. 
- codes to clean the acquire data and function to split the clean data were merged together and put in prepare.py module 
- prepare function has inbuilt function to handle null values, outliers and converting the datatypes.

## Split Data:
- prepared data was split into train, validate and test samples using the split function in prepare module. 
- first the data was split into 80% as train_validate and 20% test. then train_validate(80%) was split into 80% train and 30% validate samples.

## Data Exploration and Evaluation:
- Features were plotted, visualized and statistical testing were performed to determine the correlation with the target variable.


## SCALE Data:
- Data were scaled as needed by using MinMaxScaler

## MODELING 
- Build a regression model that performs better than a baseline
- Linear regression, Lassolars, Tweedieregressor models were created and fitted with train sample and made a predictions.
- RMSE was chosen as metrics to compare the three different models.
- Root mean square error, which is a metric that tells us the average distance between the predicted values from the model and the actual values in the dataset.

- The lower the RMSE, the better a given model is able to “fit” a dataset.



## CONCLUSIONS:
- Features explored 'Bed', 'Bath', and ' Squre foot area' have the direct correlation with the property value. I decided to drop 'county_code' feature as feature selection method gave bed, bath and sq)ft_area as top 3 best features.
