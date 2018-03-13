# -*- coding: utf-8 -*-
from sklearn.model_selection import StratifiedKFold
import xgboost as xgb
import numpy as np

__all__ = ['cross_validation']

def cross_validation(df, target, num_folds=10):
    """
    Processa df i target per tal de retornar una llista amb el nombre de folds definits

    Parametres:
    ----------
    df: Dataframe amb els features per columnes.
    target: Serie o diccionari amb el target. Ha d'estar amb el mateix order que el df
    num_folds (default=10): Nombre de folds a generar

    return: Llista de diccionaris amb els següents camps:
        fold_num: Nombre de fold
        train_data: Df de features amb els ítems de train
        train_target: Llista amb el target de train
        test_data: Df de features amb els ítems de test
        test_target: Llista amb el target de test

    """

    if len(df) != len(target):
        print ('El tamany de df i de target ha de ser igual')
        return None

    skf = StratifiedKFold(n_splits=num_folds)

    folds = []

    for n, train, test in enumerate(skf.split(np.zeros(df.shape[0], target))):
        folds.append({'fold_num': n,
                      'train_data': df.iloc[train],
                      'train_target': target.iloc[train],
                      'test_data': df.iloc[test],
                      'test_target': df.iloc[test]})

    return folds


def train_test_xgboost(df_train, df_test, parameters = None, model=False, scores_test=False, accuracy=True):
    """

    df_train:
        Df de train
    df_test:
        Df de test
    parameters (optionals):
        Diccionari amb parametres
            https://xgboost.readthedocs.io/en/latest/parameter.html
    model (False):
        Return model?
    scores_test (False):
        Return test scores?
    accuracy (True):
        Return accuracy
    return:
        Diccionari amb els fields demanats
    """

    data_train = df_train.as_matrix()
    label_train = df_train.columns.tolist()
    label_train_integers = [i for i in range(df_train.shape[1])]
    dtrain = xgb.DMatrix(data_train, label=label_train_integers)



