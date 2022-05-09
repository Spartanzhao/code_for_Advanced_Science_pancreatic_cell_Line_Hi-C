#draw horizontal barplot
def draw_bar(sampleLst,datalist,outfile):
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4), sharex=False)
    axes.set_ylabel('GO term')
    axes.set_xlabel('-log10(pval)')
    medianprops = dict(linestyle='-', linewidth=1, color='black')
    boxprops = dict(linestyle='-', linewidth=1, color='black')
    colors = ["#E69F00","#56B4E9","#E27678"]
    bplot = axes.barh(tick_list, datalist, edgecolor='grey',width=0.5,alpha=1,color=colors)
    axes.set_yticks([])
    axes.set_yticklabels([])
    axes.spines['bottom'].set_linewidth(1)
    axes.spines['left'].set_linewidth(1)
    axes.spines['right'].set_linewidth(0)
    axes.spines['top'].set_linewidth(0)
    fig.savefig('{}.bar.pdf'.format(outfile))
    fig.savefig('{}.bar.png'.format(outfile))
    
#boxplot1:
def draw_ratio(sampleLst,datalist,outfile,ylabel,n,compare_list):
    fig = plt.figure(figsize=(6,4))
    axes = fig.add_axes([0.13,0.1,0.7,0.7])
    axes.set_ylabel(ylabel)
    tick_list=[]
    x=0
    for i in sampleLst:
        x+=(n-1)/2+0.5
        tick_list.append(x)
        x+=n
    position=[]
    x=0
    for i in sampleLst:
        for j in range(n):
            position.append(x+j)
        x+=n+1
    color_list2=['#007E00','#F49800','#EC0000']*3
    color_list=['#D3E6D2','#FCECCC','#FBE1E1']*3
    bbox_list=[]
    for  i in range(len(datalist)):
        x=position[i]
        medianprops = dict(linestyle='-', linewidth=1, color=color_list2[i])
        boxprops = dict(linestyle='-', linewidth=1, color=color_list2[i])
        whiskerprops = dict(color=color_list2[i], linewidth=1,linestyle='-')
        capprops =dict(color=color_list2[i], linewidth=1,linestyle='-')
        bplot=axes.boxplot(datalist[i], showfliers=False, patch_artist=True, widths=0.7, vert=True, positions=[x],medianprops=medianprops, boxprops=boxprops,whiskerprops=whiskerprops,capprops=capprops)
        patch =bplot['boxes'][0]
        patch.set(facecolor=color_list[i], alpha=1)
        patch.set(edgecolor=color_list[i], linewidth=1)
        bbox_list.append(bplot["boxes"][0])
    axes.spines['bottom'].set_linewidth(1)
    axes.spines['left'].set_linewidth(1)
    axes.spines['right'].set_linewidth(0)
    axes.spines['top'].set_linewidth(0)
    axes.tick_params(top=False,right=False,width=1,colors='black',direction='out')
    axes.set_xticks(tick_list)
    axes.set_xticklabels(sampleLst)
    axes.set_xticklabels(axes.get_xticklabels(),rotation=0,fontsize=8,ha="center")
    if n>1:
        bbox_list2=[]
        for i in range(n):
            bbox_list2.append(bbox_list[i])
        axes.legend(bbox_list, compare_list,loc='upper center',bbox_to_anchor=(0.5, 1.2),handlelength=2,handleheight=1.236,fontsize=10,ncol=n,frameon=False)
    axes.set_xlim(-1,position[-1]+1)
    fig.savefig('{}.pdf'.format(outfile))

    
 #boxplot2
def draw_ratio(sampleLst,datalist,outfile,ylabel):
    fig = plt.figure(figsize=(5,3))
    axes = fig.add_axes([0.15,0.15,0.7,0.7])
    axes.set_ylabel(ylabel)
    tick_list=[]
    for i in range(len(sampleLst)):
        tick_list.append(i)
    medianprops = dict(linestyle='-', linewidth=1, color='black')
    boxprops = dict(linestyle='-', linewidth=1, color='black')
    bplot = axes.boxplot(datalist, showfliers=False, patch_artist=True, widths=0.7, vert=True, positions=tick_list,medianprops=medianprops, boxprops=boxprops)
    colors=['#F97502','#FEC200','#EFE6C9','#D3A2BF','#9B6D91','#2EB1E7','#4794C2','#F3D5CA','#286568','#152B1E','#D56E07','#676101','#CE9863','#F9CC4A','#C10B24','#FFE921','#3E7874','#86BBD3','#7B9FC5','#5A685B','#FEC79E','#EBA874','#F89331','#C46D5B','#FBA702','#02B7FE','#70F8C6','#065DD7','#FD3614']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    axes.spines['bottom'].set_linewidth(1)
    axes.spines['left'].set_linewidth(1)
    axes.spines['right'].set_linewidth(0)
    axes.spines['top'].set_linewidth(0)
    axes.tick_params(top=False,right=False,width=1,colors='black',direction='out')
    axes.set_xticks(tick_list)
    axes.set_xticklabels(sampleLst)
    axes.set_xticklabels(axes.get_xticklabels(),rotation=45,fontsize=8,ha="right")
    fig.savefig('{}.png'.format(outfile))
    

