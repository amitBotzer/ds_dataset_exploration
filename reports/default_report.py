"""
This is the default exploration report that should be used during the dataset exploration phase in the project. This
module contains main run(dataset) method and additional auxiliary methods. The run(dataset) executes all the standard
exploration methods that shall always be executed regardless the specific project.
"""

from gt_representativity.gt_representativity_factory import *


def run(dataset):
    """
    The run(dataset) executes all the standard exploration methods that shall always be executed regardless the specific
    project.

    Parameters
    ----------
    dataset : DSDataSet
        upon which we'll execute the exploration.

    Returns
    -------
    res_dict
        a dictionary containing the exploration results where the key is the exploration name and the value is its
        result.

    """
    res_dict = {}

    #check gt representativity:
    gt_rep_validator = get_default_gt_representativity(dataset)
    res_dict['gt representativity'] = gt_rep_validator.validate()

    return res_dict
