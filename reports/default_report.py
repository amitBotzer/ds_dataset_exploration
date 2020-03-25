from gt_representativity.gt_representativity_factory import *


def run(dataset):
    """
    """
    res_dict = {}

    #check gt representativity:
    gt_rep_validator = get_default_gt_representativity(dataset)
    res_dict['gt representativity'] = gt_rep_validator.validate()

    return res_dict
