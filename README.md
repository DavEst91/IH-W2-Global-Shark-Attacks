
<p align="center">
  <img width="460" height="300" src="https://i.pinimg.com/236x/9c/d7/2c/9cd72caaa4dde095f767da09387d6f3c--animal-captions-animal-memes.jpg">
</p>

# W2-Global-Shark-Attacks
IH: W2 Project - Data cleaning &amp; wrangling

## Objective
We were provided with a raw dataset from the web Kaggle about sharks attacks registered: time and date when they where registered, characteristics of the victim, lethality of the attacks and details about how the events were investigated. (https://www.kaggle.com/teajay/global-shark-attacks#attacks.csv)

Our objetive is to clean the dataset until we have a database we can work with and contrast the next three hypothesis:

1. Most of the provoked sharks attacks are provoked by Americans.
2. Distribution of sharks attacks is correlated with the Age of the victim
3. Sharks attacks ocurrs mainly in the afternoon

## Methodology

### Data cleaning

1. Looking for NaN values: Raw dataset contents many rows an columns which are filled with NaN values. In order to improve the quality of the dataset we get rid of it by using de drop and dropna methods of pandas dataframe once we are sure no important information will be lose.

2. Looking for duplicated values: some columns have duplicated information, or really similar information. We drop it once we determine which column is more appropiated. Also we drop columns that have not usefull data for de hypothesis we have planteated.

3. Consistency of the data (Here comes the big prize!): We have 
