from .main import Ask
from .upload import Upload
from importlib.metadata import version, PackageNotFoundError

try:
    pkg_version = version("pyimai")
except PackageNotFoundError:
    pkg_version = "unknown"

__version__ = pkg_version
__all__ = ["Ask", "Upload"]