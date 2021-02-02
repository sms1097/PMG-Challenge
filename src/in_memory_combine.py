import sys
import dask
import dask.dataframe as dd
import ntpath
import pandas as pd


@dask.delayed
def _make_dataset(file):
    df = pd.read_csv(file)
    filename = ntpath.split(file)[-1]
    df['filename'] = filename
    return df


def in_memory_combine(paths):
    files = [_make_dataset(file) for file in paths[:-1]]
    df = dd.from_delayed(files)
    df.to_csv(paths[-1], single_file=True, index=False)


if __name__ == '__main__':
    in_memory_combine(sys.argv[1:])
