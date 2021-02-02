import sys
import pandas as pd
import ntpath
import csv


def _make_dataset(df, file):
    filename = ntpath.split(file)[-1]
    df['filename'] = filename
    return df


def out_of_memory_combine(paths):
    # create csv with header
    with open(paths[-1], 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['email_hash', 'category', 'filename'])

    # append to empty csv
    chunk_size = 10 ** 7
    for file in paths[:-1]:
        curr_df = pd.read_csv(file, chunksize=chunk_size)
        for chunk in curr_df:
            temp_df = _make_dataset(chunk, file)
            temp_df.to_csv(paths[-1], mode='a', index=False, header=False)


if __name__ == '__main__':
    out_of_memory_combine(sys.argv[1:])
