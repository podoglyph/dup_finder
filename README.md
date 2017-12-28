# Dup Finder

Dup Finder is a program to search out and list duplicate files based on md5 checksums. Inspired by Raymond Hettinger.

## Getting Started

Clone this repo.

### Prerequisites

This app was developed in Python 3.6. It will work in Python 2.7, as well.

In the project root:
`pip install -r requirements.txt`

### Run

To run the program, from the project root:
`python find_dups.py`

The program will return a dict of the hashes along with lists containing either single files or multiple files, the latter being the duplicates.

## License

This project is licensed under the MIT License.
