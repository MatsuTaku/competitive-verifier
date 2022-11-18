import pathlib
from logging import getLogger
from typing import Optional

from oj_verify_clone.config import get_config
from oj_verify_clone.languages.models import Language

logger = getLogger(__name__)

_dict: Optional[dict[str, Language]] = None


def _get_dict() -> dict[str, Language]:
    from oj_verify_clone.languages.cplusplus import CPlusPlusLanguage
    from oj_verify_clone.languages.go import GoLanguage
    from oj_verify_clone.languages.haskell import HaskellLanguage
    from oj_verify_clone.languages.java import JavaLanguage
    from oj_verify_clone.languages.nim import NimLanguage
    from oj_verify_clone.languages.python import PythonLanguage
    from oj_verify_clone.languages.ruby import RubyLanguage
    from oj_verify_clone.languages.rust import RustLanguage
    from oj_verify_clone.languages.user_defined import UserDefinedLanguage

    global _dict  # pylint: disable=invalid-name
    if _dict is None:
        _dict = {}
        _dict[".cpp"] = CPlusPlusLanguage()
        _dict[".hpp"] = _dict[".cpp"]
        _dict[".cc"] = _dict[".cpp"]
        _dict[".h"] = _dict[".cpp"]
        _dict[".nim"] = NimLanguage()
        _dict[".py"] = PythonLanguage()
        _dict[".hs"] = HaskellLanguage()
        _dict[".ruby"] = RubyLanguage()
        _dict[".go"] = GoLanguage()
        _dict[".java"] = JavaLanguage()
        _dict[".rs"] = RustLanguage()

        for ext, config in get_config()["languages"].items():
            if "." + ext in _dict:
                if not isinstance(_dict["." + ext], UserDefinedLanguage):
                    for key in (
                        "compile",
                        "execute",
                        "bundle",
                        "list_attributes",
                        "list_dependencies",
                    ):
                        if key in config:
                            raise RuntimeError(
                                "You cannot overwrite existing language: .{}".format(
                                    ext
                                )
                            )
            else:
                _dict["." + ext] = UserDefinedLanguage(extension=ext, config=config)
    return _dict


def get(path: pathlib.Path) -> Optional[Language]:
    return _get_dict().get(path.suffix)
