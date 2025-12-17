import argparse
from typing import Optional, List, Any
import asyncio
from .upload import Upload
from .main import Ask
from .info import versions, help

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="PyiMAi",
        description="PyiMAi - AI CLI with optional image support",
        add_help=False
    )
    parser.add_argument("-p", "--prompt", type=str, help="Prints response of ai")
    parser.add_argument("-f", "--filepath", type=str, help="Path of image")
    parser.add_argument("-u" , "--upload" , type=str, help= "Uploading images")
    parser.add_argument("-e", "--expiration", default=600, type=int, help="Enable this if you want uploads to be automatically deleted after a certain time (in seconds, 60-15552000).")
    parser.add_argument("-k", "--key", type=str, default= "46503be935b7b03b31d903b3dae8397b", help="The API key.")
    parser.add_argument("-h", "--help", action="store_true", help="Display help message")
    parser.add_argument("-v", "--version", action="store_true", help="Display version info")
    args, unknown = parser.parse_known_args()

    if unknown:
        for arg in unknown:
            print(f"[ERROR] Argument `{arg}` not recognized.")
        exit(1)

    return args


async def run_cli():
    args = parse_args()

    try:
        if args.prompt:
            filepaths: Optional[List[str]] = None
            if args.filepath:
                filepaths = [args.filepath]

            ai = Ask(
                prompt=args.prompt,
                filepath=filepaths
            )
            print(await ai.chat())


        elif args.upload:
            uploader = Upload(
                filepaths=[args.upload],
                expiration=args.expiration,
                key=args.key
            )
            result = await uploader.get_info()
            print(result)

        elif args.help:
            print(help())

        elif args.version:
            print(versions())

        else:
            print("[ERROR] No valid arguments provided. Use `-h` for help.")
    except Exception as e:
        print(f"[FATAL] Unexpected error: {e}")


def console():
    asyncio.run(run_cli())

if __name__ == "__main__":
    console()