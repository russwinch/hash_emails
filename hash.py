import hashlib
import os
import sys
import time


def hasher(text, algorithm):
    '''Applies hashing to the string and returns the hex value.'''
    if algorithm not in hashlib.algorithms_available:
        raise AttributeError("Algorithm not supported")

    m = getattr(hashlib, algorithm)(str.encode(text))
    return m.hexdigest()


def hashfile(file_in, file_out, algorithm, anonymise=True):
    '''
    Reads the file line by line, appending the hashed email.

    Anonymise removes the first two columns: contact number and email.
    '''
    start_time = time.time()
    total_lines = 0

    with open(file_in) as f:
        for line in f:
            total_lines += 1
            line = line.strip()  # remove line breaks

            columns = line.split(',')
            hashed_email = hasher(columns[1], algorithm)

            with open(file_out, mode='a') as out:
                if anonymise:
                    out.write(columns[2] + ',')
                else:
                    for c in columns:
                        out.write(c + ',')

                if total_lines == 1:  # add header
                    out.write('hashed_email\n')
                else:
                    out.write(hashed_email + '\n')

            if total_lines % 1000 == 0:
                print("{} lines processed".format(total_lines))

    total_time = round(time.time() - start_time, 6)
    print('{} lines processed in {} seconds using {}'.format(
        total_lines, total_time, algorithm))


def check_files(infile, outfile):
    '''Checks files are valid and returns True if output file exists.'''
    existing_outfile = False

    if not os.access(infile, os.F_OK):
        raise IOError("Source file not found, ensure path is correct")

    if os.access(outfile, os.F_OK):
        if infile == outfile:
            raise IOError("Source and output files cannot be the same")
        existing_outfile = True
        if input("File exists. OK to overwrite? [y/n] > ") != 'y':
            raise IOError("""User declined to grant permission to overwrite
                            existing file with 'y'""")
    return existing_outfile


def clearfile(text_file):
    '''Opens the file in write mode which clears it.'''
    with open(text_file, mode='w'):
        print('{} cleared!'.format(text_file))


if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        raise IOError("""Source and output file paths are missing.
                Usage: hash.py <source> <output> <algorithm>[optional]""")
    infile = sys.argv[1]
    outfile = sys.argv[2]

    if len(sys.argv) == 4:
        algorithm = sys.argv[3].lower()
    else:
        algorithm = 'sha256'  # default to sha256

    existing_outfile = check_files(infile, outfile)
    if existing_outfile:
        clearfile(outfile)

    hashfile(infile, outfile, algorithm)
