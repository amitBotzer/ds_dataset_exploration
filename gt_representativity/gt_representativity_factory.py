from gt_representativity.gtrep_classifier_method import *


def get_default_gt_representativity(ds_dataset):
    return GTRepClfMethod(ds_dataset)


def get_gt_representativity(method_type, ds_dataset):
    if method_type == "GT_REP_CLF_METHOD":
        return GTRepClfMethod(ds_dataset)
    else:
        raise NotImplementedError("{0} GT representativity validator doesn't exist".format(method_type))
