import pandas as pd
import numpy as np
import argparse
import re,sys,os,math,gc
#plot module
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
plt.rcParams.update({'figure.max_open_warning': 100})
plt.style.use('seaborn-colorblind')
mpl.rcParams['ytick.direction'] = 'out'

#可P
import matplotlib as mpl
mpl.rcParams['pdf.fonttype']=42
mpl.rcParams['ps.fonttype']=42

#match two intervals
from bx.intervals.intersection import Intersecter, Interval
def match_interval(df,dfg,chr_list):
    interval_dic={}
    for i in chr_list:
        interval=Intersecter()
        interval_dic[i]=interval
        dfs=df[df['chrs']==i]
        dfs=dfs.reset_index(drop=True)
        for j in range(len(dfs)):
            interval.add_interval(Interval(dfs['start'][j], dfs['end'][j]))
    lists=[]
    for i in chr_list:
        index=[]
        dfgs=dfg[dfg['chrs']==i]
        dfgs=dfgs.reset_index(drop=True)
        for j in range(len(dfgs)):
            x=interval_dic[i].find(dfgs['start'][j],dfgs['end'][j])
            if len(x)>0:
                index.append(j)
        dfos=dfgs.loc[index,:]
        lists.append(dfos)
    dfo=pd.concat(lists)
    return dfo

#intervals tag
from bx.intervals.intersection import Intersecter, Interval
def match_interval(chrs,start,end,dfg,chr_list):
    interval=Intersecter()
    interval.add_interval(Interval(start, end))
    lists=[]
    dfgs=dfg[dfg['chrs']==chrs]
    dfgs=dfgs.reset_index(drop=True)
    index=[]
    for j in range(len(dfgs)):
        x=interval.find(dfgs['start'][j],dfgs['end'][j])
        if len(x)>0:
            index.append(j)
    dfos=dfgs.loc[index,:]
    dfos=dfos.reset_index(drop=True)
    x=''
    for i in range(len(dfos)):
        x+=dfos['GeneName'][i]+';'
    return x
  
  #秩和检验
from scipy import stats
stat_val, p1 = stats.mannwhitneyu(datalist[0], datalist[4], use_continuity = True, alternative = None )

#fisher  exact test
#fisher exact
from scipy.stats import fisher_exact
oddsr, p = fisher_exact([[2662,1383],[6098,11027]], alternative='two-sided')
