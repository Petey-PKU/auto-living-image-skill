# SPDX-License-Identifier: GPL-3.0-only
"""Build and verify an Excel-ready GraphPad Prism XY table."""

import argparse
import csv
from itertools import zip_longest
import math
from pathlib import Path
import re

from openpyxl import load_workbook


def hours(value):
    match = re.fullmatch(r"(\d+(?:\.\d+)?|\.\d+)\s*h?", str(value).strip(), re.I)
    if not match:
        raise ValueError(f"Invalid time in hours: {value!r}")
    return number(match[1])


def number(value):
    if isinstance(value, bool):
        raise ValueError(f"Expected a number, got {value!r}")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"Expected a finite number, got {value!r}")
    return result


def mouse_number(value):
    result = number(value)
    if result < 1 or not result.is_integer():
        raise ValueError(f"Invalid positive mouse number: {value!r}")
    return int(result)


def read_long(sheet):
    data = {}
    for row_number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), 2):
        if not any(value is not None for value in row):
            continue
        group, time, mouse, measure = (row + (None,) * 4)[:4]
        try:
            if not isinstance(group, str) or not group.strip():
                raise ValueError("Group is missing")
            group = group.strip()
            if any(character in group for character in "\t\r\n"):
                raise ValueError("Group contains a tab or line break")
            key = group, hours(time), mouse_number(mouse)
            if key in data:
                raise ValueError(f"Duplicate group/time/mouse record: {key}")
            data[key] = None if measure in ("", None) else number(measure)
        except (TypeError, ValueError) as error:
            raise ValueError(f"{sheet.title}, row {row_number}: {error}") from error
    if not data:
        raise ValueError("The source sheet has no data rows")
    return data


def wide_rows(data, requested):
    maxima = {}
    for group, _, mouse in data:
        maxima[group] = max(maxima.get(group, 0), mouse)
    groups = [group.strip() for group in requested.split(",")] if requested else list(maxima)
    if len(groups) != len(set(groups)) or any(group not in maxima for group in groups):
        raise ValueError("Provide distinct group names present in the source sheet")
    columns = [(group, mouse) for group in groups for mouse in range(1, maxima[group] + 1)]
    yield [None] + [group if mouse == 1 else None for group, mouse in columns]
    yield ["Time (h)"] + [f"Mouse {mouse}" for _, mouse in columns]
    for time in sorted({time for group, time, _ in data if group in groups}):
        yield [time] + [data.get((group, time, mouse)) for group, mouse in columns]


def build(rows, destination):
    rows = list(rows)
    with Path(destination).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(
            handle, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None
        )
        for row in rows:
            writer.writerow(format(value, ".15g") if isinstance(value, float) else value for value in row)


def same_value(observed, expected):
    if isinstance(expected, float):
        try:
            return math.isclose(number(observed), expected, rel_tol=1e-12)
        except (TypeError, ValueError):
            return False
    if expected is None:
        return observed is None or observed == ""
    return observed == expected


def check(rows, sheet):
    differences = []
    for row_number, (expected, observed) in enumerate(
        zip_longest(rows, sheet.iter_rows(values_only=True), fillvalue=()), 1
    ):
        for column, (want, got) in enumerate(zip_longest(expected, observed), 1):
            if not same_value(got, want):
                differences.append((row_number, column, want, got))
    for row, column, want, got in differences[:10]:
        print(f"Row {row}, column {column}: expected {want!r}, found {got!r}")
    print(f"{len(differences)} differences")
    return int(bool(differences))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    make = subparsers.add_parser("build", help="Create a Prism-style TSV")
    make.add_argument("xlsx")
    make.add_argument("out")
    make.add_argument("--sheet", type=int, default=0)
    verify = subparsers.add_parser("check", help="Verify the pasted wide worksheet")
    verify.add_argument("xlsx")
    verify.add_argument("--long-sheet", type=int, default=0)
    verify.add_argument("--wide-sheet", type=int, default=1)
    for command in (make, verify):
        command.add_argument("--groups", help="Comma-separated subset and order of groups")
    args = parser.parse_args()

    try:
        if args.command == "build" and Path(args.xlsx).resolve() == Path(args.out).resolve():
            raise ValueError("Choose a different path for the TSV output")
        with Path(args.xlsx).open("rb") as source:
            workbook = load_workbook(source, read_only=True, data_only=True)
            try:
                if args.command == "build":
                    build(wide_rows(read_long(workbook.worksheets[args.sheet]), args.groups), args.out)
                    print(f"Wrote {args.out}")
                    return 0
                return check(
                    wide_rows(read_long(workbook.worksheets[args.long_sheet]), args.groups),
                    workbook.worksheets[args.wide_sheet],
                )
            finally:
                workbook.close()
    except (IndexError, OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
