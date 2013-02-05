# -*- coding: utf-8 -*-


def erase_none_values(param_dict):
    """ erases none values from dict """
    for k, v in param_dict.items():
        if v is None:
            del param_dict[k]