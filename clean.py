import pandas
import numpy as np

def load_data(fp="./data/TrainingData.csv"):
    return pandas.DataFrame.from_csv(fp)

def fill_with_avg(start_index, end_index, col):
    if end_index == None:
        pass
    else:
        avg = ( col[start_index-2:start_index-1] -
                col[end_index+1:end_index+2]
                ) / 2
        for i in range(start_index, end_index+1):
            #print i, avg
            col[i-1, i] = avg

def find_nan(col):
    """ Assuming the col [A, nan, nan, B, C] is indexed from 1..5, 
    yield (2, 3)"""
    chunk_start = None
    last_i = -2 # None
    for i,val in col.iteritems():
        if isinstance(val, str):
            continue

        if last_i + 1 != i:
            # Handle the end of every chunk
            if chunk_start:
                print 'end of chunk'
                last_i = -2
                yield (chunk_start, None)
            # Handle the beginning of every chunk?
            #else:
                #yield ('start_of_chunk', None)

        # Handle beginning and middle of every chunk
        if np.isnan(val):
            if chunk_start == None:
                chunk_start = i
        elif chunk_start:
            yield (chunk_start, last_i)
            chunk_start = None
        #print 'end for i,v: %s, %s' % (i,val)
        last_i = i

def clean_data(data):
    for key in data.columns:
        col = data.get(key)
        for start_i, end_i in find_nan(col):
            print col.name, start_i, end_i
            fill_with_avg(start_i, end_i, col)











