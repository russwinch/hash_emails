import hashlib
import time


def hasher(text, algorithm):
    '''Applies hashing to the string and returns the hex value.'''
    m = getattr(hashlib, algorithm)(str.encode(text))
    return m.hexdigest()


def hashfile(file_in, file_out, algorithm='md5', anonymise=True):
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

    total_time = time.time() - start_time
    print('{} lines processed from {} to {} in {} seconds'.format(
        total_lines, infile, outfile, total_time))


def clearfile(text_file):
    '''Opens the file in write mode which clears it.'''
    with open(text_file, mode='w'):
        print('file {} cleared!'.format(text_file))


if __name__ == '__main__':
    infile = 'testdata.csv'
    outfile = 'outfile.csv'

    clearfile(outfile)
    hashfile(infile, outfile)  # , algorithm='sha256')  # , anonymise=False)
