import argparse
from netaddr import IPSet, IPNetwork
from termcolor import colored

def deduplicate_cidrs(input_file, output_file):
    # Read the list of CIDR ranges from the input file
    with open(input_file, 'r') as f:
        cidr_ranges = [line.strip() for line in f.readlines()]

    # Use IPSet to manage and deduplicate the CIDR ranges
    ip_set = IPSet()

    for cidr in cidr_ranges:
        ip_set.add(IPNetwork(cidr))

    # Get the cleaned list of CIDR ranges
    cleaned_cidrs = list(ip_set.iter_cidrs())

    # Save the cleaned list to the output file
    with open(output_file, 'w') as f:
        for cidr in cleaned_cidrs:
            f.write(str(cidr) + '\n')

def print_logo():
    logo = """

 ██████╗ ██████╗██╗██████╗ ██████╗ 
██╔════╝██╔════╝██║██╔══██╗██╔══██╗
██║     ██║     ██║██║  ██║██████╔╝
██║     ██║     ██║██║  ██║██╔══██╗
╚██████╗╚██████╗██║██████╔╝██║  ██║
 ╚═════╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝
                                  
    print(colored(logo, 'blue'))
    print(colored('Developed By Bl4ck7', 'red'))

def main():
    print_logo()

    parser = argparse.ArgumentParser(description='CCIDR - CIDR Deduplication Tool')
    parser.add_argument('-l', '--list', required=True, help='Input file containing list of CIDR ranges')
    parser.add_argument('-o', '--output', required=True, help='Output file to save deduplicated CIDR ranges')

    args = parser.parse_args()

    deduplicate_cidrs(args.list, args.output)

if __name__ == '__main__':
    main()
