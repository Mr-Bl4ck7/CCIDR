# -*- coding: utf-8 -*-

"""
CCIDR - Command Line Tool for CIDR Deduplication

Usage:
  ccidr.py [-l <input_file>] [-o <output_file>]
  ccidr.py -h | --help

Options:
  -l --input <input_file>    Input file containing CIDR blocks
  -o --output <output_file>  Output file to save deduplicated CIDR blocks
  -h --help                  Show this help message and exit
"""

from docopt import docopt

def main(args):
    if args['--input'] and args['--output']:
        input_file = args['--input']
        output_file = args['--output']
        # Process input_file and output_file as needed
        print("Input file: {}".format(input_file))
        print("Output file: {}".format(output_file))
    else:
        print("""
\033[94m ██████╗ ██████╗██╗██████╗ ██████╗ \033[0m
\033[94m██╔════╝██╔════╝██║██╔══██╗██╔══██╗\033[0m
\033[94m██║     ██║     ██║██║  ██║██████╔╝\033[0m
\033[94m██║     ██║     ██║██║  ██║██╔══██╗\033[0m
\033[94m╚██████╗╚██████╗██║██████╔╝██║  ██║\033[0m
\033[94m ╚═════╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝\033[0m
\033[91mDeveloped By Bl4ck7\033[0m
\033[91mhttps://github.com/Mr-Bl4ck7\033[0m
                                   
CCIDR - Command Line Tool for CIDR Deduplication

Usage:
  ccidr.py -l <input_file> -o <output_file>
  ccidr.py -h | --help

Options:
  -l --input <input_file>    Input file containing CIDR blocks
  -o --output <output_file>  Output file to save deduplicated CIDR blocks
  -h --help                  Show this help message and exit
        """)

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
