import sys
import getopt
import json
import pandas as pd


def get_io_filenames(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('Usage: python3 export_to_csv.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    ifile, ofile = None, None
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            ifile = arg
        elif opt in ("-o", "--ofile"):
            ofile = arg
        else:
            print('Usage: python3 export_to_csv.py -i <inputfile> -o <outputfile>')
            sys.exit(2)

    if None in (ifile, ofile):
        print('Usage: python3 export_to_csv.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    return ifile, ofile


def main(argv):
    ifile, ofile = get_io_filenames(argv)

    with open(ifile) as file:
        lines = file.readlines()

    data = [json.loads(line) for line in lines]

    df = pd.json_normalize(data, sep=',')

    df.to_csv(ofile, index=False, sep = ';')


if __name__ == '__main__':
    main(sys.argv[1:])
