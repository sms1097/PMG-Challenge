import sys
import dask
import dask.dataframe as dd
import ntpath
import pandas as pd


@dask.delayed
def make_dataset(file):
    df = pd.read_csv(file)
    filename = ntpath.split(file)[-1]
    df['filename'] = filename
    return df


def main(paths):
    files = [make_dataset(file) for file in paths]
    df = dd.from_delayed(files)
    df.to_csv(paths[-1], single_file=True)


if __name__ == '__main__':
    main(sys.argv[1:])
