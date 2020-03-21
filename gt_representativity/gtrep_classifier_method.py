import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from gt_representativity.gt_representativity import GTRepresentativeValidator

from sklearn.svm import LinearSVC


class GTRepClfMethod(GTRepresentativeValidator):

    def __init__(self, dataset):
        super().__init__(dataset)

    def validate(self):
        """

        """
        labeled_samples = self.dataset.get_labeled_samples().drop(columns=['label']).sample(frac=0.9)
        unlabled_samples = self.dataset.get_unlabeled_samples().drop(columns=['label']).sample(frac=0.9)
        df = pd.concat([labeled_samples, unlabled_samples])
        is_labeled = df['is_labeled']
        df = df.drop(columns=['is_labeled'])
        rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_clf.fit(df, is_labeled)
        predictions = rf_clf.predict(df)
        score = np.sum([predictions == is_labeled]) / len(predictions)
        bias = 100 * np.abs(score - 0.5)
        return bias
