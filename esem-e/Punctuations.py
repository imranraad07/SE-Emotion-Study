import re
from random import shuffle


def remove_punctuation(text):
    """Remove all punctuation except ! and ? from tweet text"""
    return re.sub(
        "[#]|[$]|[\"]|[%]|[\']|[&]|[(]|[)]|[*]|[+]|[=]|[-]|[_]|[@]|[.]|[:]|[;]|[,]|[<]|[>]|[`]|[~]|[\\]|[\/]|[{]|[}]|[\^]",
        " ", text)


def remove_punctuation_emtk(text):
    """Remove all punctuation except . ! and ? from tweet text"""
    return re.sub(
        "[#]|[$]|[\"]|[%]|[\']|[&]|[(]|[)]|[*]|[+]|[=]|[-]|[_]|[@]|[:]|[;]|[,]|[<]|[>]|[`]|[~]|[\\]|[\/]|[{]|[}]|[\^]",
        " ", text)
