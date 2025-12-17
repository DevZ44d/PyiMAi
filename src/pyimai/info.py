from importlib.metadata import version, PackageNotFoundError
from colorama import Fore

def versions():
    try:
        pkg_version = version("pyimai")
    except PackageNotFoundError:
        pkg_version = "unknown"

    return f"""
{Fore.RED}PyiMAi {Fore.WHITE}Version: {Fore.RED}{pkg_version} {Fore.WHITE}.
Author: {Fore.RED}PyCodz {Fore.WHITE}Channel .
({Fore.RED}PyPi{Fore.WHITE}) : https://pypi.org/project/PyiMAi .
({Fore.RED}Telegram{Fore.WHITE}) : https://t.me/PyCodz .
({Fore.RED}Portfolio{Fore.WHITE}) : https://deep.is-a.dev .
"""


def help() -> str:
    return f"""
{Fore.RED}pyimai {Fore.WHITE}-[OPTIONS] "[FOR-OPTION]"

Options:
—— {Fore.RED}Argument	            {Fore.RED}Description{Fore.WHITE}
    -p, --prompt	      Send a prompt to the AI.
    -f, --filepath	      Image path ({Fore.RED}optional{Fore.WHITE}).
    -u, --upload	      Upload image only.
    -e, --expiration	  default = 600 , Image expiration time. ({Fore.RED}seconds{Fore.WHITE}) ({Fore.RED}optional{Fore.WHITE})
    -k, --key             default i added one, The API key. ({Fore.RED}optional{Fore.WHITE})
    -v, --version	      Show version
    -h, --help	          Show help
"""
