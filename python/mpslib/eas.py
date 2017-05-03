#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:06:14 2017

@author: tmeha

Examples

import eas;
import matplotlib.pyplot as plt;

# Get the JURA data
import urllib.request
urllib.request.urlretrieve('https://github.com/cultpenguin/mGstat/raw/master/examples/data/jura/prediction.dat', 'prediction.dat')

# Read the JURA data
file_eas='prediction.dat';
Oeas = eas.read(file_eas) 

i_show=5;
cm = plt.cm.get_cmap('RdYlBu')
sc=plt.scatter(Oeas['D'][:,0],Oeas['D'][:,1],s=8*Oeas['D'][:,i_show],c=Oeas['D'][:,i_show], cmap=cm)
plt.xlabel(Oeas['header'][0])
plt.ylabel(Oeas['header'][1])
plt.title(Oeas['header'][i_show])
plt.colorbar(sc);
plt.show();

"""
import numpy as np

debug_level=0;

def read(filename='eas.dat'):
    
    file = open(filename,"r") ;
    if (debug_level>0):
        print("eas: file ->%20s" % filename);        
    
    eas={};
    eas['title'] = (file.readline()).strip('\n');    
    
    if (debug_level>0):
        print("eas: title->%20s" % eas['title']);        
    
    dim_arr=eas['title'].split()
    if len(dim_arr)==3:
        eas['dim'] = {};
        eas['dim']['nx'] = np.int(dim_arr[0])        
        eas['dim']['ny'] = np.int(dim_arr[1])        
        eas['dim']['nz'] = np.int(dim_arr[2])        
    
    eas['n_cols'] = np.int(file.readline());    
    
    eas['header'] = [];
    for i in range(0, eas['n_cols']):
        # print (i)
        h_val = (file.readline()).strip('\n');
        eas['header'].append(h_val);

        if (debug_level>1):
            print("eas: header(%2d)-> %s" % (i,eas['header'][i] ) );        

    file.close();    


    try:
        eas['D'] = np.genfromtxt(filename, skip_header=2+eas['n_cols']);    
        if (debug_level>1):
            print("eas: Read data from %s" % filename );        
    except:
        print("eas: COULD NOT READ DATA FROM %s" % filename );        
        
    
    
    # If dimensions are given in title, then convert to 2D/3D array
    if "dim" in eas:
        eas['Dmat']=eas['D'].reshape((eas['dim']['ny'],eas['dim']['nx']));   
        if (debug_level>0):
            print("eas: converted data in matrixes (Dmat)");        

    
    return eas;
    
