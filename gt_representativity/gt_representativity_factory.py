"""
This module is meant to decouple specific GTRepresentativeValidator implementations from the users. We don't want to
change code every time we found a novel method to validate GT representations.
"""
from gt_representativity.gtrep_classifier_method import *


def get_default_gt_representativity(ds_dataset):
    """
    Return the default GTRepresentativeValidator implementation. Should be changed if a new state-of-the-art approach is
    introduced.

    Parameters
    ----------
    ds_dataset : DSDataSet object with which we'll initialize the GTRepresentativeValidator object

    Returns
    -------
    GTRepresentativeValidator
        Initialized GTRepresentativeValidator object

    "'"""
    return GTRepClfMethod(ds_dataset)


def get_gt_representativity(method_type, ds_dataset):
    """
    Return an initialized GTRepresentativeValidator object according to the given method_type.

    Parameters
    ----------
    ds_dataset : DSDataSet object with which we'll initialize the GTRepresentativeValidator object.

    Returns
    -------
    GTRepresentativeValidator
        Initialized GTRepresentativeValidator object from the specific type.

    Raises
    ------
    NotImplementedError
        If the method_type given isn't exist.

    "'"""
    if method_type == "GT_REP_CLF_METHOD":
        return GTRepClfMethod(ds_dataset)
    else:
        raise NotImplementedError("{0} GT representativity validator doesn't exist".format(method_type))
