import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import PowerTransformer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, auc
# import StratifiedKFold
from sklearn.model_selection import StratifiedKFold


def map_gambling(df):
    df['CAT_GAMBLING'] = df['CAT_GAMBLING'].map({'No': 0, 'Low': 1, 'High': 2})
    return df


def split_x_from_y(df, target='DEFAULT'):
    X = df.drop(columns=[target])
    y = df[target]
    return X, y


def get_my_metrics(model, X_train, X_val, y_train, y_val):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)

    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred)
    recall = recall_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred)

    return accuracy, precision, recall, f1


def cox_box_transform(X_train, X_val):
    # transform data
    # scaler = StandardScaler()
    cox_box_model = PowerTransformer(method='yeo-johnson')
    X_train_transformed = cox_box_model.fit_transform(X_train)
    X_val_transformed = cox_box_model.transform(X_val)

    # X_train_transformed = scaler.fit_transform(X_train_transformed)
    # X_val_transformed = scaler.transform(X_val_transformed)

    return X_train_transformed, X_val_transformed


def create_tally(X_train, X_val, y_train, y_val, models, names):
    X = pd.concat([X_train, X_val])
    y = pd.concat([y_train, y_val])
    # if CAT_GAMBLING column has strings, map them to integers
    if X['CAT_GAMBLING'].dtype == 'object':
        X = map_gambling(X)

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    stats = pd.DataFrame(
        columns=['model', 'accuracy', 'accuracy_std', 'precision', 'precision_std', 'recall', 'recall_std', 'f1',
                 'f1_std'])

    for model, name in zip(models, names):
        accuracy = []
        precision = []
        recall = []
        f1 = []
        for train_index, val_index in skf.split(X, y):
            X_train, X_val = X.iloc[train_index], X.iloc[val_index]
            y_train, y_val = y.iloc[train_index], y.iloc[val_index]

            X_train_transformed, X_val_transformed = cox_box_transform(X_train, X_val)
            model.fit(X_train_transformed, y_train)
            y_pred = model.predict(X_val_transformed)

            accuracy.append(accuracy_score(y_val, y_pred))
            precision.append(precision_score(y_val, y_pred))
            recall.append(recall_score(y_val, y_pred))
            f1.append(f1_score(y_val, y_pred))

        new_row = {'model': name,
                   'accuracy': np.mean(accuracy),
                   'accuracy_std': np.std(accuracy),
                   'precision': np.mean(precision),
                   'precision_std': np.std(precision),
                   'recall': np.mean(recall),
                   'recall_std': np.std(recall),
                   'f1': np.mean(f1),
                   'f1_std': np.std(f1)}
        stats = pd.concat([stats, pd.DataFrame([new_row])])

    return stats


def validate(X_train, X_test, y_train, y_test, models, names):
    score = pd.DataFrame(columns=['names', 'accuracy', 'precision', 'recall', 'f1'])
    if X_train['CAT_GAMBLING'].dtype == 'object':
        X_train = map_gambling(X_train)
    if X_test['CAT_GAMBLING'].dtype == 'object':
        X_test = map_gambling(X_test)
    X_train, X_test = cox_box_transform(X_train, X_test)
    for m, n in zip(models, names):
        ac, pr, re, f1 = get_my_metrics(m, X_train, X_test, y_train, y_test)
        new_row = {'names': n, 'accuracy': ac, 'precision': pr, 'recall': re, 'f1': f1}
        score = pd.concat([score, pd.DataFrame(new_row, index=[0])])
    return score


def prepair_score(score):
    score = pd.melt(score, id_vars=['model'], value_vars=['accuracy', 'precision', 'recall', 'f1'])
    return score


def create_visualization(s):
    s = prepair_score(s)
    sns.set(rc={'figure.figsize': (10, 5)})
    sns.barplot(x='model', y='value', hue='variable', data=s)
    plt.title('Model Performance')
    plt.ylabel('Score in each metric')
    plt.xlabel('Model')
    plt.legend(title='Metrics')
    plt.show()
