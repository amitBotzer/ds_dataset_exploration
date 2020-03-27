from abc import abstractmethod


class DSDateSet(object):
    """
    The DSDateSet object is meant to define a convention for datasets used. For example, we would like to ensure that
    there are certain columns in the dataset. This is practically a wrapper with benefits of spark or pandas DataFrame.
    """

    def __init__(self, df):
        self.df = df

    @abstractmethod
    def get_labeled_samples(self):
        """
        Get only the labeled samples of the dataset.

        Parameters
        ----------
        self : ds_dataset

        Returns
        -------
        DataFrame
            pandas or Spark DataFrame that contains only the labeled samples of the whole dataset.

        """
        pass

    @abstractmethod
    def get_unlabeled_samples(self):
        """
        Get only the unlabeled samples of the dataset.

        Parameters
        ----------
        self : ds_dataset

        Returns
        -------
        DataFrame
            pandas or Spark DataFrame that contains only the unlabeled samples of the whole dataset.

        """
        pass

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
            ds_dataset

        Returns
        -------
        bool
            Whether the dataset is normalized or not

        """
        pass
