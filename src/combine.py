import sys
import ntpath
import csv


def combine(paths):
    with open(paths[-1], 'w') as out:
        writer = csv.writer(out, delimiter=',')
        writer.writerow(['email_hash', 'category', 'filename']) 

        for file in paths[:-1]:
            with open(file, 'r') as f:
                reader = csv.reader(f)
                reader.__next__()

                filename = ntpath.split(file)[-1]
                for line in reader:
                    line.append(filename)
                    writer.writerow(line)



if __name__ == '__main__':
    combine(sys.argv[1:])
