# PMG-Challenge
## CSV Combiner

There are two implementations that make different assumptions about the problem

To run either file use 
``` 
python src/<file> <input_files> <output_files>
```

### Data Set Fits in Memory
The script `src/in_memory_combine.py` uses dask to initialize the datasets in parallel and combine them into one dask dataframe. Dask can be scaled horizontally very easily, so the assumption that the dataframe fits in memory is not unreasonable. Outside of this dask would perform best if the data was preprocessed and the additional column 

### No Data Set Fits in Memory
The script `src/out_of_memory_combine.py` assumes that none of the data sets to be combined fit in memory. This method uses chunking to sequentially feed data into the output csv file. 
