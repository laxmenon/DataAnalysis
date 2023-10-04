#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:55:28 2022

@author: lakshmimenont
"""

import pandas as pd
import numpy as np

def sortGroups(gr):
    groupSortByDate = gr.sort_values(['DateTime'],ascending=True)
    return groupSortByDate
    

def renamePictures(S):
    print(S)
    photolist = S.split("\n")
    photoNameSplitList = []
    for photo in photolist:
        photoNameSplit = photo.split(",")
        photoNameSplitStripped = [s.strip() for s in photoNameSplit]
        photoNameSplitList.append(photoNameSplitStripped)
        
        
    photolistdf = pd.DataFrame(photoNameSplitList, columns =['Name', 'Place', 'DateTime']) 
    
    photolistdf['DateTime']= pd.to_datetime(photolistdf['DateTime'])
    print(photolistdf.info())
    print(photolistdf)
    
    photolistdfGrouped = photolistdf.groupby('Place')
    photolistdfBeforeGroupedSorted = photolistdfGrouped.apply(lambda x: x.sort_values(['DateTime'],ascending=True))
    #photolistdfBeforeGroupedSorted['localCount'] = photolistdfBeforeGroupedSorted.apply(lambda x: np.arange(len(x)))
    photolistdfBeforeGroupedSorted.index = range(len(photolistdfBeforeGroupedSorted))
    photolistdfBeforeGroupedSorted['localCount'] = photolistdfBeforeGroupedSorted.groupby('Place').cumcount()+1
    print(photolistdfBeforeGroupedSorted)
    
    maxLocalCount = photolistdfBeforeGroupedSorted["localCount"].max()
    maxDigitsLocalCount = len(str(maxLocalCount))
    print(maxDigitsLocalCount)
    
    #photolistdfBeforeGroupedSorted['Type'] = photolistdfBeforeGroupedSorted['Name'].rpartition('.')[2]
    photolistdfBeforeGroupedSorted['Type']  = photolistdfBeforeGroupedSorted.apply(lambda x: x['Name'].rpartition('.')[2], axis=1)
    print(photolistdfBeforeGroupedSorted['Type'])
    photolistdfBeforeGroupedSorted['localCountPadded']  = photolistdfBeforeGroupedSorted.apply(lambda x: str(x['localCount']).zfill(maxDigitsLocalCount), axis=1)
    print(photolistdfBeforeGroupedSorted['localCountPadded'])
    
    photolistdfBeforeGroupedSorted['NewName'] = photolistdfBeforeGroupedSorted['Place'] + photolistdfBeforeGroupedSorted['localCountPadded'] + "." + photolistdfBeforeGroupedSorted['Type']
    photolistdfBeforeGroupedSortedNew = photolistdfBeforeGroupedSorted.filter(['Name','NewName'])
    print(photolistdfBeforeGroupedSortedNew)
    #for group_name, group in photolistdfGrouped:
     #   print(group_name)
     
    finalSortedList = pd.merge(photolistdf,photolistdfBeforeGroupedSortedNew,on='Name')
    print(finalSortedList)
    
    
    
    
    return

def main():
    
    S = "photo.jpj, Warsaw, 2012-09-05 14:08:15\njohn.jpj, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00;02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11"
    renamePictures(S)
    
    
main()
    