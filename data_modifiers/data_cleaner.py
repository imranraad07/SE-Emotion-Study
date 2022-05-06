import re


def remove_block_quotes(text):
    modified_text = ''
    prev_line_block = False
    for line in text.split('\n'):
        if not line.strip().startswith('>'):
            modified_text += line + '\n'
            prev_line_block = False
        else:
            if prev_line_block is True:
                continue
            else:
                modified_text += '[BLOCK QUOTE].' + '\n'
                prev_line_block = True
    return modified_text


def remove_newlines(text):
    # replace new lines with space
    modified_text = text.replace("\n", " ")
    return modified_text


def remove_extra_whitespaces(text):
    return ' '.join(text.split())


def remove_triple_quotes(text):
    occurrences = [m.start() for m in re.finditer('```', text)]
    idx = len(occurrences)
    if idx % 2 == 1:
        text = text[:occurrences[idx - 1]]
        idx = idx - 1
    for i in range(0, idx, 2):
        if idx > 0:
            text = text[:occurrences[idx - 2]] + '[TRIPLE QUOTE].' + text[(occurrences[idx - 1] + 3):]
            idx = idx - 2
    return text


def remove_stacktrace(text):
    st_regex = re.compile('at [a-zA-Z0-9\.<>$]+\(.+\)')
    lines = list()
    for line in text.split('\n'):
        matches = st_regex.findall(line.strip())
        if len(matches) == 0:
            lines.append(line)
        else:
            for match in matches:
                line = line.replace(match, ' ')
            lines.append(line.strip(' \t'))

    lines = '\n'.join(lines)
    # hack to get rid of multiple spaces in the text
    # lines = ' '.join(lines.split())
    return lines


def remove_url(text):
    text = re.sub(r"http\S+", "[URL]", text)
    return text


def remove_usermention(text):
    text = re.sub(' @[^\s]+', ' [USER]', text)
    if text.startswith('@'):
        text = re.sub('@[^\s]+', '[USER]', text)
    return text


def filter_nontext(text):
    text = remove_url(text)
    text = remove_usermention(text)
    text = remove_block_quotes(text)
    text = remove_stacktrace(text)
    # text = remove_newlines(text)
    text = remove_triple_quotes(text)
    # text = remove_extra_whitespaces(text)
    return text.strip()
