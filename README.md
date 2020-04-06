
<p align="center">
  <img width="460" height="300" src="https://i.pinimg.com/236x/9c/d7/2c/9cd72caaa4dde095f767da09387d6f3c--animal-captions-animal-memes.jpg">
</p>

# W2-Global-Shark-Attacks
IH: W2 Project - Data cleaning &amp; wrangling

## Objective
We were provided with a raw dataset from the web Kaggle about shark attacks registered: time and date when they were registered, characteristics of the victim, lethality of the attacks and details about how the events were investigated. (https://www.kaggle.com/teajay/global-shark-attacks#attacks.csv)

Our objective is to clean the dataset until we have a database we can work with and contrast the next three hypotheses:

1. Most of the provoked shark attacks are provoked by Americans.
2. Distribution of shark attacks is correlated with the age of the victims
3. Shark attacks ocurr mainly in the afternoon

## Methodology: Data cleaning

1. Looking for NaN values: Raw dataset contents many rows an columns which are filled with NaN values. In order to improve the quality of the dataset we get rid of it by using the drop and dropna methods of pandas dataframe once we are sure no important information will be lose.

2. Looking for duplicated values: some columns have duplicated information, or really similar information. We drop it once we determine which column is more appropiate. Also we drop columns that have not usefull data for de hypothesis we have planted.

3. Consistency of the data (Here comes the big prize!): We have to check if after getting rid of "no data" data, the data we get is useful for an analysis. We proceed column by column, checking the quality of data, fixing them when possible and dropping them when not possible.

4 Exporting data

## Data Analysis: results

1. Most of the provoked shark attacks are provoked by American: We contrast the number of provoked shark attacks with the number of total attacks by countries. It comes to English been the nationality with a bigger proportion of provoked shark attacks.

2. Distribution of sharks attacks correlates with the age of the victims: We find that distribution of shark attacks with age has a well defined maximum around 19 years.

3. Shark attacks ocurr mainly in the afternoon: We classify shark attacks based on the moment of the day they occur and found that most of the attacks occur in the afternoon (which made sense due to people tend to have them leisure time during the afternoon) but follow close by attacks occurring during the morning.

