# PMG-Challenge
## CSV Combiner

The best script I wrote was `src/combine.py`. This uses the python csv writer, which because it wraps around a document pointer saves a lot on memory usage. 
To run use the following:
``` 
python src/combine.py <input_files> <output_files>
```

I wrote two slower implementations below. Dask does require the data set be saved to memory before writing so this doesn't work well in this application. The benefit of this script is that dask can be trivially scaled horizontally, and if each worker loads a data set the speed increase would be superior to scaling the `combine.py` vertically. 

The other approach uses chunking with pandas data frames to append to a csv. This ended up being slow due to the write operation to the output file. Overall I can't think of any advantage to this approach. 

The `test.py` file takes outputs from all methods and asserts they are equal. I tested by expanding the `generate_fixtures.py` script and adding more classes. I tested this for a few different generated data sets and saw passing results. 
