from typing import Union, Optional, Literal
from pathlib import Path

import pandas as pd 
import os 

PathLike = Union[str, Path]
ListofStrOrInt = list[Union[str, int]]

class TORPDataset:
    '''
    Utility class for loading the Tornado Algorithm CSV
    files as a merged pandas.DataFrame
    
    Attrs
    -----------
    dirpath : path-like, str : root dir where the data is stored
    years : list of int : Which years to load.
    dataset_type : 'pretornadic' or 'Storm_Reports': default = 'Storm_Reports'
        Storm reports are from NCEI, linearly interpolated to 1-min resolution, 
        and fit to the nearest AzShear max within 10 km. 
        Pre-tornadic are manually identified 0-60 min pre-tornadic tracks
    '''
    # List of all available years as separate CSV files
    _DEFAULT_YEARS = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    
    def __init__(self, 
                 dirpath : PathLike, 
                 years : Optional[ListofStrOrInt ] = None,
                 dataset_type : Literal['pretornadic', 'Storm_Reports'] = 'Storm_Reports'
                ):
        
        self._years = years or self._DEFAULT_YEARS
        self._dirpath = dirpath 
        self._dataset_type = dataset_type
    
    def load_dataframe(self):
        
        typ = f'{self._dataset_type}_expanded' 
        if self._dataset_type == 'Storm_Reports':
            typ = typ.replace('expanded', 'Expanded')
        
        paths = [os.path.join(self._dirpath, 
                              f'{y}_{typ}_tilt0050_radar_r2500_nodup.csv')
                 for y in self._years
                ]
       
        dfs = [pd.read_csv(p, low_memory=False) for p in paths]
        
        df = pd.concat(dfs, axis=0)
    
        return df
        
dataset = TORPDataset(dirpath='/work2/mflora/torp_datasets/ML_data',
                      #years=[2011, 2013, 2014]
                     )

dataset.load_dataframe()