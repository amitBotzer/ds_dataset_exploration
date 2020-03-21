from abc import abstractmethod


class GTRepresentativeValidator(object):
    """
    
    """

    def __init__(self, dataset):
        self.dataset = dataset

    @abstractmethod
    def validate(self):
        """

        """
        pass
