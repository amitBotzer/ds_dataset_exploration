from abc import ABC

from dataset.ds_dataset import DSDateSet


class DSSparkDataSet(DSDateSet, ABC):
    """
     Implements DSDateSet for Spark DataFrames.
     """

    def __init__(self, spark_df):
        super().__init__(spark_df)

    def get_labeled_samples(self):
        """
        Overrides DSDataSet.get_labeled_samples() method for Spark DataFrame.
        """
        raise NotImplementedError("Not implemented")

    def get_unlabeled_samples(self):
        """
        Overrides DSDataSet.get_unlabeled_samples() method for Spark DataFrame.
        """
        raise NotImplementedError("Not implemented")

    def is_normalized(self):
        """
        Overrides DSDataSet.is_normalized() method for Spark DataFrame.
        """
        raise NotImplementedError("Not implemented")
