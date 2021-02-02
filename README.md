# PMG-Challenge
## CSV Combiner

The best script I wrote was `src/combine.py`. This uses the python csv writer, which because it wraps around a document pointer saves a lot on memory usage. 
To run use the following:
``` 
python src/combine.py <input_files> <output_files>
```

I wrote two slower implementations below. The problem with using Dask, which should be faster, is that to load dask data frames to csv it needs to fit all partitions in memory first. Normal dask usage would be fine for this data since it could be stored in partitions and loaded quickly, however that wasn't the task of this challenge.

The other approach uses chunking with pandas data frames to append to a csv. This ended up being slow due to the write operation to the output file. 

The `test.py` file takes outputs from all methods and asserts they are equal. I tested by expanding the `generate_fixtures.py` script and adding more classes. I tested this for a few different generated data sets and saw passing results. 
