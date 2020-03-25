from abc import ABC

from dataset.ds_dataset import DSDateSet


class DSPandasDataSet(DSDateSet, ABC):
    """
    Implements DSDateSet for pandas DataFrames.
    """

    def __init__(self, pandas_df):
        super().__init__(pandas_df)

    def get_labeled_samples(self):
        """
        Overrides DSDataSet.get_labeled_samples() method for pandas DataFrame.
        """
        return self.df[self.df['is_labeled'] == True]

    def get_unlabeled_samples(self):
        """
        Overrides DSDataSet.get_unlabeled_samples() method for pandas DataFrame.
        """
        return self.df[self.df['is_labeled'] == False]

    def is_normalized(self):
        """
        Overrides DSDataSet.is_normalized() method for pandas DataFrame.
        """
        raise NotImplementedError("Not implemented")
