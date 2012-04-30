#!/usr/bin/env python

import sys
import math
from pandas import *
import numpy as np

def gest(series, period):
  series = series[-period:]
  prevema = series[0]
  emaout = [prevema]
  
  for last in series[1:]:
    curema = prevema + (2.0/(period + 1.0))*(last - prevema)
    prevema = curema
    emaout.append(curema)
  
  emaout = np.asarray(emaout, np.float)
  return emaout

def main():
  d = read_csv('data/TrainingData.csv')
  s = read_csv('data/SubmissionZerosExceptNAs.csv')
  targets = ['target_1_57','target_10_4002','target_10_8003','target_11_1','target_11_32','target_11_50','target_11_64','target_11_1003','target_11_1601','target_11_4002','target_11_8003','target_14_4002','target_14_8003','target_15_57','target_2_57','target_3_1','target_3_50','target_3_57','target_3_1601','target_3_4002','target_3_6006','target_4_1','target_4_50','target_4_57','target_4_1018','target_4_1601','target_4_2001','target_4_4002','target_4_4101','target_4_6006','target_4_8003','target_5_6006','target_7_57','target_8_57','target_8_4002','target_8_6004','target_8_8003','target_9_4002','target_9_8003']
  for t in targets:
    s[t] = s[t] + 0.0
  
  currentChunk = 1.
  c = d[ d['chunkID'] == currentChunk ]
  for rowid, row in s.iterrows():
    if currentChunk != row['chunkID']:
      currentChunk = row['chunkID']
      print 'processing chunk ' + str(currentChunk)
      c = d[ d['chunkID'] == currentChunk ]
      
    for t in targets:
      if (row[t] != -1000000):
        series = c[c['hour'] == row['hour']][t].dropna()
        if len(series) > 0:
          s[t][rowid] = series.median()
        else:
          pass
    
  s.to_csv('data/SubmissionMedian.csv', index=False, na_rep=0)
  
if __name__=="__main__":
    main()
