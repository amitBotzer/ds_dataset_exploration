from abc import ABC

from dataset.ds_dataset import DSDateSet


class DSPandasDataSet(DSDateSet, ABC):
    """
    The DSSparkDataSet implements DSDateSet and it is practically a wrapper with
    benefits to pandas dataframes.
    """

    def __init__(self, pandas_df):
        super().__init__(pandas_df)

    def get_labeled_samples(self):
        """

        """
        return self.df[self.df['is_labeled'] == True]

    def get_unlabeled_samples(self):
        """

        """
        return self.df[self.df['is_labeled'] == False]

    def is_normalized(self):
        """
        Validate pandas dataset feature normalization.

        In order to run any mathematical experiment on a dataset, it must be
        normalized. i.e. the features must be scaled to the same range. This
        method validate this property.

        Parameters
        ----------
        self : ds_dataset
            The dataset to be validated

        Returns
        -------
        bool
            Whether the dataset is normalized or not

        """
        raise NotImplementedError("Not implemented")
