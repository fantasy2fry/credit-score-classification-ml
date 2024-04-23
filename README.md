## Project - Credit Score classification
[This Project](https://github.com/fantasy2fry/credit-score-classification-ml) is created as part of introduction to machine learning course included in Data Science Studies.
We are going to use the dataset from Kaggle: [Credit Score](https://www.kaggle.com/datasets/conorsully1/credit-score).
Project is going to be done by a team of 3 people. Throughout the project we are going to be validated by another team.

### Project team:
- [Norbert Frydrysiak](https://github.com/fantasy2fry)
- [Anna Ostrowska](https://github.com/annaostrowska03)
- [Dominika Gimzicka](https://github.com/GimzickaDominika?fbclid=IwAR117ek299FTZ05YrRQHRcsr8fk-1SZ2kE59icbJIOspeX861-zq1do5MqY)

### Validators team:
- [Natalia Choszczyk](https://github.com/nataliachoszczyk)
- [Karolina Dunal](https://github.com/xxkaro)

### First part of the project - Exploratory Data Analysis
- The dataset is going to be divided into 4 parts: credit_score_train, credit_score_test, credit_score_valid, credit_score_validators.
- One part is only available for the Validators team.
- Each team member takes dataset and performs EDA on it separately.
- The results are then compared and discussed in the team.
- The final version of the EDA is going to be put in "EDA/final" folder.
- Validators are going to check the final version of the EDA.
- Project team is going to think of feedback from the validators and improve the final version of the EDA.
- Whole process can be repeated or changed if needed.

### Second part of the project - Feature engineering and First models
- After EDA we know that there are no missing values in the dataset.
- We are going to ordinally encode "CAT_GAMBLING" column.
- We try to deal with outliers in two ways:
    - We are going to manually remove some of the outliers.
    - We are going to compare it with PYOD library functions.
- We are going to transform continuous variables using Box-Cox transformation and StandardScaler.
- We might try to use for instance PCA to reduce the number of features.
- We are going to compare the results of the models using different methods of dealing with outliers and different methods of feature engineering.
- We are going to use MANY different models to compare them.
- We will look at hiperparameters and try to optimize them.
- We are going to use cross-validation to compare the models.
- We are going to use different metrics to compare the models.
- Validators will check the results in feature_engineering/final.ipynb file.
- Project team is going to think of feedback from the validators and improve the final version of the feature engineering and first models.


### Third part of the project - Final models and conclusions
- Files from this part can be found in "final_models" folder.
- We have done lots of things, I might describe them later.
- In folder "library" we have our own library with functions that we have used in the project.

### Final reports
- Reports are written in Polish.
- They can be found in "reports" folder.
- We have report from our whole project and from each part of the project.
- We have also report about our validator work for the other team.

### Note for every contributor:
- All files names should contain underscore instead of spaces. It is a good practice, because it is better for UNIX or UNIX-like systems.
- You can use Polish language, because this is pretty language, but I will try to use English as much as possible.