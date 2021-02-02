import sys
import ntpath
import csv


def combine(paths):
    """
    Takes in list of files, combines all but last file and saves to last file

        Parameters:
            paths (list): string for path to file
        Return: None
    """
    # init writer and create header
    writer = csv.writer(sys.stdout)
    writer.writerow(['email_hash', 'category', 'filename'])

    # iterate through files to write
    for file in paths:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            reader.__next__()

            filename = ntpath.split(file)[-1]
            for line in reader:
                line.append(filename)
                writer.writerow(line)


if __name__ == '__main__':
    combine(sys.argv[1:])
