import sys
from _typeshed import SupportsWrite
from collections.abc import Iterable, Iterator
from typing import Any
from typing_extensions import Final, Literal, TypeAlias

__version__: Final[str]

QUOTE_ALL: Literal[1]
QUOTE_MINIMAL: Literal[0]
QUOTE_NONE: Literal[3]
QUOTE_NONNUMERIC: Literal[2]
if sys.version_info >= (3, 12):
    QUOTE_STRINGS: Literal[4]
    QUOTE_NOTNULL: Literal[5]

# Ideally this would be `QUOTE_ALL | QUOTE_MINIMAL | QUOTE_NONE | QUOTE_NONNUMERIC`
# However, using literals in situations like these can cause false-positives (see #7258)
_QuotingType: TypeAlias = int

class Error(Exception): ...

class Dialect:
    delimiter: str
    quotechar: str | None
    escapechar: str | None
    doublequote: bool
    skipinitialspace: bool
    lineterminator: str
    quoting: _QuotingType
    strict: bool
    def __init__(self) -> None: ...

_DialectLike: TypeAlias = str | Dialect | type[Dialect]

class _reader(Iterator[list[str]]):
    @property
    def dialect(self) -> Dialect: ...
    line_num: int
    def __next__(self) -> list[str]: ...

class _writer:
    @property
    def dialect(self) -> Dialect: ...
    def writerow(self, row: Iterable[Any]) -> Any: ...
    def writerows(self, rows: Iterable[Iterable[Any]]) -> None: ...

def writer(
    csvfile: SupportsWrite[str],
    dialect: _DialectLike = "excel",
    *,
    delimiter: str = ",",
    quotechar: str | None = '"',
    escapechar: str | None = None,
    doublequote: bool = True,
    skipinitialspace: bool = False,
    lineterminator: str = "\r\n",
    quoting: _QuotingType = 0,
    strict: bool = False,
) -> _writer: ...
def reader(
    csvfile: Iterable[str],
    dialect: _DialectLike = "excel",
    *,
    delimiter: str = ",",
    quotechar: str | None = '"',
    escapechar: str | None = None,
    doublequote: bool = True,
    skipinitialspace: bool = False,
    lineterminator: str = "\r\n",
    quoting: _QuotingType = 0,
    strict: bool = False,
) -> _reader: ...
def register_dialect(
    name: str,
    dialect: type[Dialect] = ...,
    *,
    delimiter: str = ",",
    quotechar: str | None = '"',
    escapechar: str | None = None,
    doublequote: bool = True,
    skipinitialspace: bool = False,
    lineterminator: str = "\r\n",
    quoting: _QuotingType = 0,
    strict: bool = False,
) -> None: ...
def unregister_dialect(name: str) -> None: ...
def get_dialect(name: str) -> Dialect: ...
def list_dialects() -> list[str]: ...
def field_size_limit(new_limit: int = ...) -> int: ...
