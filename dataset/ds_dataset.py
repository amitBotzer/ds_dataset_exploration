class DSDateSet(object):
    """
    The DSDateSet object is meant to define a convention for datasets used. For
    example, we would like to ensure that there are certain columns such as
    label column. This is practically a wrapper with benefits of spark or pandas
    dataframe.
    """

    def __init__(self, df):
        self.df = df

    @abstractmethod
    def is_normalized(self):
        """
        Validate dataset feature normalization.

        In order to run any mathematical experiment on a dataset, it must be
        normalized. i.e. the features must be scaled to the same range. This method
        validate this property.

        Parameters
        ----------
        self : ds_dataset
            The dataset to be validated

        Returns
        -------
        bool
            Whether the dataset is normalized or not

        """
        pass
