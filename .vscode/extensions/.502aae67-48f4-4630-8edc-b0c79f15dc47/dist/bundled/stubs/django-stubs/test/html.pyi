from collections.abc import Sequence
from html.parser import HTMLParser
from typing import Any

WHITESPACE: Any

def normalize_whitespace(string: str) -> str: ...

_ElementAttribute = tuple[str, str | None]

class Element:
    name: str | None = ...
    attributes: list[_ElementAttribute] = ...
    children: list[Any] = ...
    def __init__(
        self, name: str | None, attributes: Sequence[_ElementAttribute]
    ) -> None: ...
    def append(self, element: Element | str) -> None: ...
    def finalize(self) -> None: ...
    def __contains__(self, element: Element | str) -> bool: ...
    def count(self, element: Element | str) -> int: ...
    def __getitem__(self, key: int) -> Any: ...

class RootElement(Element):
    def __init__(self) -> None: ...

class HTMLParseError(Exception): ...

class Parser(HTMLParser):
    SELF_CLOSING_TAGS: Any = ...
    root: Any = ...
    open_tags: Any = ...
    element_positions: Any = ...
    def __init__(self) -> None: ...
    def format_position(self, position: Any = ..., element: Any = ...) -> str: ...
    @property
    def current(self) -> Element: ...

def parse_html(html: str) -> Element: ...