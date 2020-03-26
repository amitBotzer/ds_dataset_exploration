import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from gt_representativity.gt_representativity import GTRepresentativeValidator


class GTRepClfMethod(GTRepresentativeValidator):
    """
    Using Random Forest classifier to ensure GT proper representation.

    Classifiers try to distinguish between two different classes by separating the positive samples from the negative
    samples. Formally, classifiers work on a certain feature space, trying to find a decision boundary between the
    positive vectors and the negative vectors. If the classifier achieves high accuracy, then we conclude that we can
    differentiate the positive from the negative samples over the current vector space, using the specific algorithm
    with which the classifier was trained.

    We can use this classifiers property to ensure that we *cannot* differentiate positive from negative samples. We
    would like to verify this kind of behavior when we are checking GT representativity. This method defines all the GT
    samples as positive samples (regardless of the real labels), and all the other samples as negative. Then the method
    trains Random Forest classifier over those samples. If the classifier achieves high accuracy it means the classifier
    can easily distinguish GT samples from general samples, means the GT isn't distributed as the overall population
    does. Best case scenario, the classifier achieves accuracy of 50%.
    """

    def __init__(self, dataset):
        super().__init__(dataset)

    def validate(self):
        """
        Validate self.dataset GT representativity using the Random Forest validation method.

        Randomly samples 90% of the labeled data, and 90% percent of the unlabeled data. Then compiles them to a new
        pandas DataFrame and trains a Random Forest classifier, computes the bias and returns it.

        Parameters
        ----------
        self : GTRepClfMethod object initialized with DSDataSet object.

        Returns
        -------
        float
            The deviation in percents from the desired distributions difference (50%).

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
