from .constant import RS
from .constant import US


def load(fp):
    return loads(fp.read())


def loadf(path, mode='rt', encoding=None):
    with open(path, mode=mode, encoding=encoding) as f:
        return loads(f.read())


def loads(s):
    return [record.split(US) for record in s.split(RS)]
