import sys
import Macro_parser

macroParser = Macro_parser.getparser()
while True:
    try:
        parse_in = input('Macro >>')
        macroParser.parse(parse_in)
    except (EOFError, KeyboardInterrupt):
        break
