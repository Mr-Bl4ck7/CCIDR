# CCIDR - CIDR Deduplication Tool

![CCIDR Logo](CCIDR_Logo.png)

CCIDR is a simple yet powerful tool for deduplicating CIDR ranges. It reads a list of CIDR ranges from an input file, removes duplicates, and saves the cleaned list to an output file.

## Developer

Developed by [Bl4ck7](https://github.com/Mr-Bl4ck7)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Mr-Bl4ck7/ccidr.git
    cd ccidr
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    ```sh
    pip3 install -r requirements.txt
    ```

## Usage

### Command-line Arguments

- `-l`, `--list`: Path to the input file containing CIDR ranges (required)
- `-o`, `--output`: Path to the output file to save deduplicated CIDR ranges (required)

### Example

To run the script, use the following command:

    python ccidr.py
    python3 ccidr.py
    python ccidr.py -l cidr_list.txt -o cleaned_cidr_list.txt
    python3 ccidr.py -l cidr_list.txt -o cleaned_cidr_list.txt
