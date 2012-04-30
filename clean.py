import pandas
import scipy
from collections import defaultdict
import numpy as np
from pylab import plot, xlabel, ylabel

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
    return col

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

def clean_data(data):
    for key in data.columns:
        col = data[key]
        for start_i, end_i in find_nan(col):
            data[key] = fill(start_i, end_i, col)
    return data[data['position_within_chunk'] < 144]

def main():
    data = load_data()
    data = clean_data(data)
    data.to_csv("./cleaned_TrainingData.csv")
    #chunks = chunkify(data)
    #return chunks

#other funcs
def groupby_site(data):
    grps = defaultdict(list)
    # Drop all columns that don't have location
    for col in data.columns:
        try: key = int(col.split('_')[-1])
        except: continue
        grps[key].append(col)
    # Add chunkID column
    for v in grps.values():
        v.append('chunkID')
    return {k:data[v] for k,v in grps.items()}

def groupby_chunk(data):
    chunks = data.groupby(by='chunkID')
    return {name: group.dropna(axis=1) for name,group in chunks}

def groupby_site_and_chunk(data):
    grps = groupby_site(data)
    for site, table in grps.items():
        grps[site] = groupby_chunk(table)
    return grps

def _plot_sample():
 for x in range(1, 10):
     grps[1][x]['WindSpeed..Resultant_1'].plot(figsize=(1,0))
     raw_input()

def plotSpectrum(y,Fs=150):
 """
 Plots a Single-Sided Amplitude Spectrum of y(t)
 """
 n = len(y) # length of the signal
 k = np.arange(n)
 T = n/Fs
 frq = k/T # two sides frequency range
 frq = frq[range(n/2)] # one side frequency range

 Y = scipy.fft(y)/n # fft computing and normalization
 Y = Y[range(n/2)]
 
 plot(frq,abs(Y),'r.') # plotting the spectrum
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')
 return frq, Y

#if 'data' not in locals():
    #data = load_data()
    #grps = groupby_site_and_chunk(data)

