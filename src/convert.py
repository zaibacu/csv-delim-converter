import logging
import csv

from argparse import ArgumentParser
from enum import Enum

logger = logging.getLogger(__name__)

class QuoteLevel(Enum):
    Null = "none"
    Minimal = "minimal"
    All = "all"


def main(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    f_in = open(args.input, "r")
    f_out = open(args.output if args.output else args.input, "w")

    reader = csv.reader(f_in, delimiter=args.d1)

    q_level = csv.QUOTE_MINIMAL
    if args.quote_level == QuoteLevel.Null:
        q_level = csv.QUOTE_NONE
    elif args.quote_level == QuoteLevel.Minimal:
        q_level = csv.QUOTE_MINIMAL
    elif args.quote_level == QuoteLevel.All:
        q_level = csv.QUOTE_ALL

    header = next(reader)
    print(header)
    writer = csv.DictWriter(f_out, delimiter=args.d2, quotechar=args.quote, quoting=q_level, fieldnames=header)
    writer.writeheader()
    for row in reader:
        writer.writerow(row)

    f_in.close()
    f_out.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input", help="Input file")
    parser.add_argument("--output", help="Output file", default=None)
    parser.add_argument("-d1", help="Initial delimiter")
    parser.add_argument("-d2", help="Final delimiter")
    parser.add_argument("--quote", help="Quote character", default="\"")
    parser.add_argument("--quote-level", help="Select quoting", type=QuoteLevel, choices=list(QuoteLevel), default=QuoteLevel.Minimal)
    parser.add_argument("--debug", help="Debug mode", action="store_true")
    main(parser.parse_args())
