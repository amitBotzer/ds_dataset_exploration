import unittest
import pandas as pd
from sklearn.datasets import load_wine
from dataset.ds_pandas_dataset import DSPandasDataSet
from gt_representativity.gtrep_classifier_method import GTRepClfMethod

RANDOM_STATE = 42


class TestGTRepClfMethod(unittest.TestCase):

    def setUp(self) -> None:
        features, target = load_wine(return_X_y=True)
        labeled_df = pd.DataFrame(features)
        labeled_df['label'] = target
        labeled_df['is_labeled'] = True
        unlabeled_df = pd.DataFrame(features)
        unlabeled_df['label'] = None
        unlabeled_df['is_labeled'] = False
        df = pd.concat([labeled_df, unlabeled_df])
        self.dataset = DSPandasDataSet(pandas_df=df)

    def test_validate_good_case(self):
        gt_rep_val = GTRepClfMethod(dataset=self.dataset)
        res = gt_rep_val.validate()
        self.assertLess(res, 10)


if __name__ == '__main__':
    unittest.main()
