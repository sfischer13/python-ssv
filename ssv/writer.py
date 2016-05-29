from .constant import RS
from .constant import US
from .exception import RecordSeparatorException
from .exception import UnitSeparatorException


def dump(table, fp):
    fp.write(dumps(table))


def dumpf(table, path, mode='wt', encoding=None):
    with open(path, mode=mode, encoding=encoding) as f:
        dump(table, f)


def dumps(table):
    if any((RS in unit) for record in table for unit in record):
        raise RecordSeparatorException
    if any((US in unit) for record in table for unit in record):
        raise UnitSeparatorException
    return RS.join(US.join(record) for record in table)
