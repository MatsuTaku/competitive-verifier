import argparse
import pathlib
from typing import Optional

from competitive_verifier.utils import VerificationSummary


def run_impl(summary: VerificationSummary) -> None:
    pass


def run(args: argparse.Namespace) -> None:
    pass


def argument_docs(parser: argparse.ArgumentParser, *, default_json: Optional[pathlib.Path] = None) -> argparse.ArgumentParser:
    if default_json is None:
        parser.add_argument(
            'verify_result_json',
            help='File path of verify_result.json.',
            type=pathlib.Path
        )
    else:
        parser.add_argument(
            'verify_result_json',
            nargs='?',
            help='File path of verify_result.json. default: "{}"'.format(
                default_json
            ),
            default=default_json,
            type=pathlib.Path
        )
    return parser


def main(args: Optional[list[str]] = None) -> None:
    parsed = argument_docs(argparse.ArgumentParser()).parse_args(args)
    run(parsed)