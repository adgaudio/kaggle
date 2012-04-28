import pandas
import numpy as np

def load_data(fp="./data/TrainingData.csv"):
    data = pandas.DataFrame.from_csv(fp)
    #return data.reindex(index=range(len(data)))
    return data

def fill(start_index, end_index, col):
    failed = False
    try:
        start = col[start_index - 1]
    except:
        # Back fill start of chunk
        col[start_index-1:end_index].\
                fillna( method="bfill", inplace=True)
        failed = True
    try:
        end = col[end_index + 1]
    except:
        # Forward fill end of chunk
        col[start_index-1:end_index].\
                fillna( method="ffill", inplace=True)
        failed = True
    if not failed:
        # Fill rest of chunks with average of the end points
        avg = ( start - end ) / 2
        col[start_index-1:end_index].fillna(avg, inplace=True)

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
                last_i = -2
                yield (chunk_start, None)
        # Handle beginning and middle of every chunk
        if np.isnan(val):
            if chunk_start == None:
                chunk_start = i
        elif chunk_start:
            yield (chunk_start, last_i)
            chunk_start = None
        #print 'end for i,v: %s, %s' % (i,val)
        last_i = i

def chunkify(data):
    chunks = data.groupby(by='chunkID')
    return {name: group.dropna(axis=1) for name,group in chunks}

def clean_data(data):
    for key in data.columns:
        col = data.get(key)
        for start_i, end_i in find_nan(col):
            fill(start_i, end_i, col)


def main():
    data = load_data()
    clean_data(data)
    data.to_csv("./cleaned_TrainingData.csv")
    chunks = chunkify(data)
    return chunks
