library(ggplot2)
library(gridExtra)

setwd("/Users/yuezhao/Desktop/")
df <- read.csv("AB_compare.xls",sep="\t")
df$count = 1

AB_swith_color <- c("#B41C25", '#E27678', '#85AFBD', '#2B5983')

df$HPDE6C7_BxPC3 <- factor(df$HPDE6C7_BxPC3, levels=c('StableA', 'AtoB', 'BtoA', 'StableB'))
df$HPDE6C7_PANC1 <- factor(df$HPDE6C7_PANC1, levels=c('StableA', 'AtoB', 'BtoA', 'StableB'))


df2 <- df
df2$chrom <- "AllGenome"

df3 <- rbind(df2,df)

chroms <- c('chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'AllGenome')
df3$HPDE6C7_BxPC3 <- factor(df3$HPDE6C7_BxPC3, levels=c('StableA', 'AtoB', 'BtoA', 'StableB'))
df3$chrom <- factor(df3$chrom, levels=chroms)

#df3 = df3[df3$HPDE6C7 !=0 | df3$BxPC3 !=0 | df3$PANC1 !=0]
#print (df3$HPDE6C7_BxPC3)
#pdf("AB_switch.pdf",w=6.42,h=3.91)

p_BxPC3_ABswitch <- ggplot(data=df3, mapping=aes(x=chrom, y=count, fill=HPDE6C7_BxPC3)) +
  geom_bar(stat = "identity", position="fill") + 
  theme_bw() + theme(panel.grid = element_blank()) +
  scale_fill_manual(values=AB_swith_color) +
  coord_flip() +
  labs(title="BxPC3 to HPDE6C7",x="", y = "Percent") + 
  theme(legend.key.size=unit(4,'mm')) +
  theme(legend.title=element_blank())

p_PANC1_ABswitch <- ggplot(data=df3, mapping=aes(x=chrom, y=count, fill=HPDE6C7_PANC1)) +
  geom_bar(stat = "identity", position="fill") + 
  theme_bw() + theme(panel.grid = element_blank()) +
  scale_fill_manual(values=AB_swith_color) +
  coord_flip() +
  labs(title="PANC1 to HPDE6C7",x="", y = "Percent") + 
  theme(legend.key.size=unit(4,'mm')) +
  theme(legend.title=element_blank())


grid.arrange(p_BxPC3_ABswitch, p_PANC1_ABswitch, nrow=1)
pdf("/Users/yuezhao/Desktop/AB_change.pdf")
plot<-grid.arrange(p_BxPC3_ABswitch,p_PANC1_ABswitch, nrow=1)
print (plot)
dev.off()
