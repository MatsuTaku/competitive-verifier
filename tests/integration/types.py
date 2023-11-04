import pathlib
from pydantic import BaseModel


class FilePaths(BaseModel):
    root: pathlib.Path
    targets: str
    verify: str
    result: str
    dest_root: pathlib.Path
