from importlib.metadata import version, PackageNotFoundError
from colorama import Fore

def versions():
    try:
        pkg_version = version("pyimai")
    except PackageNotFoundError:
        pkg_version = "unknown"

    return f"""
{Fore.RED}PyiMAi {Fore.WHITE}Version: {Fore.RED}{pkg_version} {Fore.WHITE}.
Author: PyCodz Channel .
(PyPi) : https://pypi.org/project/PyiMAi .
(Telegram) : https://t.me/PyCodz .
(My Portfolio) : https://deep.is-a.dev .
"""


def help() -> str:
    return f"""
{Fore.RED}pyimai {Fore.WHITE}-[OPTIONS] "[FOR-OPTION]"

Options:
—— {Fore.RED}Argument	            {Fore.RED}Description{Fore.WHITE}
    -p, --prompt	      Send a prompt to the AI
    -f, --filepath	      Image path (optional)
    -u, --upload	      Upload image only
    -e, --expiration	  Image expiration time (seconds)
    -k, --key             The API key.
    -v, --version	      Show version
    -h, --help	          Show help
"""
