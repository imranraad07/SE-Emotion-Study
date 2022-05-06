import re
from random import shuffle


def remove_punctuation(text):
    """Remove all punctuation except ! and ? from tweet text"""
    return re.sub(
        "[#]|[$]|[\"]|[%]|[\']|[&]|[(]|[)]|[*]|[+]|[=]|[-]|[_]|[@]|[.]|[:]|[;]|[,]|[<]|[>]|[`]|[~]|[\\]|[\/]|[{]|[}]|[\^]",
        " ", text)

