#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary is not None:
            reverse = [(value, key) for key, value in a_dictionary.items()]
            return(max(reverse)[1])
        return None
