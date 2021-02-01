import sys
import ntpath
import pandas as pd
import dask
from dask.distributed import Client


@dask.delayed
def make_dataset(file):
    df = pd.read_csv(file)
    filename = ntpath.split(file)[-1]
    df['filename'] = filename
    return df


@dask.delayed
def combine(df1, df2):
    df = df1.copy()
    return df.append(df2)


def main(paths):
    # import datasets
    datasets = [make_dataset(x) for x in paths[:-1]]
    dask.compute(*datasets)

    # combine datasets
    files = datasets
    while len(files) > 1:
        new_files = []
        for i in range(0, len(files), 2):
            try:
                temp_combine = combine(files[i], files[i+1])
            except IndexError:
                temp_combine = files[i]

            new_files.append(temp_combine)
        files = new_files

    output = dask.compute(files)
    df = output[0][0]

    df.to_csv(paths[-1], index=False)


if __name__ == '__main__':
    main(sys.argv[1:])
