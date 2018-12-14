#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary is not None:
            reverse = [(key, value) for key, value in a_dictionary.items()]
            if max(reverse)[0] == 0:
                return None
            return(max(reverse)[0])
        return None
