# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:30:06 2021

@author: colomich
"""
from multiprocessing import Pool
import os

def workerfunction(element):
    #print(os.getpid())
    return(element**2)
    

long_list = range(30)

if __name__ == '__main__':
    with Pool(4) as p:
        p.map(workerfunction, long_list)
        
    