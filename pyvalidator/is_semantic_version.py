from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx


def is_semantic_version(input: str) -> bool:
    input = assert_string(input)

    senabtic_version_pattern = RegEx(
        "^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)" +
        "(?:-((?:0|[1-9]\d*|\d*[a-z-][0-9a-z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-z-][0-9a-z-]*))*))" +
        "?(?:\+([0-9a-z-]+(?:\.[0-9a-z-]+)*))?$", "i"
    )

    return senabtic_version_pattern.match(input)
