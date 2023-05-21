import logging

log = logging.getLogger(__name__)


def remove_brackets(txt):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in txt:
        if i == '[':
            skip1c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret


def append_ext(fname: str, ext: str):
    if fname is not None:
        return '{}.{}'.format(fname, ext)
    return None


def underscore_to_camel(el):
    if el is not None:
        title = ''.join(x for x in el.title() if x != '_')
        first_letter = title[0].lower()
        return '{}{}'.format(first_letter, title[1:])
    return el


def all_not_none(lst: list):
    return all(v is not None for v in lst)
