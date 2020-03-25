from abc import abstractmethod


class GTRepresentativeValidator(object):
    """
    An interface for GT representation validators.

    One of the essential challenges of data research is GT representativity. GT (Ground Truth) stand for the labeled
    data upon which we train our models. If the GT isn't distributed as the total population does, then any insight
    gained from the GT is doubtful.

    That's why it is highly important to verify the GT representativity and to quantify the GT bias if there's such.
    There are several methods to verify this, and this is an interface from which every method should derive.
    """

    def __init__(self, dataset):
        self.dataset = dataset

    @abstractmethod
    def validate(self):
        """

        """
        pass
