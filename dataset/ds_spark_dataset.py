from dataset.ds_dataset import DSDateSet


class DSSparkDataSet(DSDateSet):
    """
    The DSSparkDataSet implements DSDateSet and it is practically a wrapper with
    benefits to spark dataframes.
    """

    def __init__(self, spark_df):
        super().__init__(spark_df)

    def is_normalized(self):
        """
        Validate spark dataset feature normalization.

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
