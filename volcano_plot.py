import os
import matplotlib as mpl
mpl.use('Agg')
import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import math
import argparse
parser = argparse.ArgumentParser( description='filter false postive fithic result')
parser.add_argument('-i', '--input', type=str, required=True, help='Path to an input file')
parser.add_argument('-o', '--output', type=str, required=True, help='Path to an output file')
parser.add_argument('-l', '--list', type=str, required=True, help='Path to an gene list')
parser.add_argument('-opt', '--option', type=str, required=True, help='options to decide to use gene number or gene name as the tag')
args = parser.parse_args()

df=pd.read_table(args.input,sep='\t')
#columns=['Gene','BXPC32_count','BXPC32_normalize','HPDE6C7_count','HPDE6C7_normalize','FoldChange','Log2FoldChange','pval','padj','Up/Down','Significant','GeneName','Biotype','Position']
#df=df.loc[:,columns]

fold=df['Log2FoldChange']
qval=df['padj']

qval=np.array(qval)
qval[qval==0.0]=1e-300
q_log=[]
for i in qval:
    q_log.append(-math.log10(i))

resultdir_pos=args.output.rindex('/')
resultdir=args.output[:resultdir_pos]
if os.path.exists(resultdir) == False:
    os.mkdir(resultdir)

colors=[]
for i in range(len(df['Up/Down'])):
    if df['Up/Down'][i]=='up' and df['Significant'][i]=='yes':
        colors.append('red')
    elif df['Up/Down'][i]=='down' and df['Significant'][i]=='yes':
        colors.append('green')
    elif df['Significant'][i]=='no':
        colors.append('yellow')

gene=[]
file=open(args.list)
for i in file:
    i=i.strip().split('\t')
    gene.append(i)
tag=[]
for j in gene:
    x=[]
    for i in range(len(df['Gene'])):
        if df['Gene'][i]==j[0]:
            x.append(fold[i])
            x.append(q_log[i])
    tag.append(x)
plt.scatter(fold, q_log, alpha=0.3,cmap='viridis',c=colors)
for i in range(len(tag)):
    if args.option == str(1):
        if len(tag[i])==2:
            text='-'+gene[i][0]
            plt.text(tag[i][0], tag[i][1], text, fontsize=9)
    elif args.option == str(2):
        if len(tag[i])==2:
            text='-'+gene[i][1]
            plt.text(tag[i][0], tag[i][1], text, fontsize=9)
plt.savefig(args.output)
