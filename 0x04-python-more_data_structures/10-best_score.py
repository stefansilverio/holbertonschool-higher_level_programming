#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary is not None:
            if len(a_dictionary.items()) != 0:
                arbys = [(key, value) for key, value in a_dictionary.items()]
            return(max(arbys)[0])
        return None
