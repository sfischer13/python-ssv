class SSVException(Exception):
    """Super class of all SSV exceptions."""


class RecordSeparatorException(SSVException):
    """Raised if the given data contains the record separator."""


class UnitSeparatorException(SSVException):
    """Raised if the given data contains the unit separator."""
