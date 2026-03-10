 Taxi Fare Prediction using Machine Learning

 Project Overview

This project aims to build a machine learning model that predicts the **total taxi fare total_amount for a taxi trip. The prediction is based on several trip-related features such as trip distance, passenger count, pickup time.

The project demonstrates a complete end-to-end machine learning workflow, including data exploration, preprocessing, model training, evaluation, and saving the trained model for future predictions.


 Dataset Description

The dataset contains information about taxi trips, including:

 VendorID
 tpep_pickup_datetime
 tpep_dropoff_datetime
 passenger_count
 trip_distance
 RatecodeID
 store_and_fwd_flag
 PULocationID
 DOLocationID
 payment_type
 extra
 tip_amount
 tolls_amount
 improvement_surcharge
 total_amount (Target Variable)

The goal is to predict the total_amount using machine learning techniques.


 Project Workflow

The project follows the standard machine learning pipeline:

 1. Exploratory Data Analysis (EDA)
 Understanding dataset structure
 Checking missing values
 Checking duplicate records
 Handling negative values in total_amount
 Data visualization
 Correlation analysis

 2. Data Preprocessing
 Datetime feature extraction
 Creating new features such as:
   trip_duration
   pickup_hour
   pickup_day
Handling missing values
 Handling outliers using the IQR method
 Scaling numerical features
 Encoding categorical variables
 Creating a preprocessing pipeline using ColumnTransformer

 3. Model Building
Two models were used:

 Linear Regression (Baseline Model)
 Random Forest Regressor

 4. Hyperparameter Tuning
 GridSearchCV used to tune Random Forest parameters.

 5. Model Evaluation
Models were evaluated using:

 RMSE (Root Mean Squared Error)**
 R² Score

 6. Model Saving
The trained pipeline is saved as:
