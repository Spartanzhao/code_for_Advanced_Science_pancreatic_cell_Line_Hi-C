library(ggplot2)
library(gridExtra)
library(tidyverse)


colnames(BxPC3) <- c("Var1", "type", "Freq","Num","Freq2")
colnames(PANC1) <- c("Var1", "type", "Freq","Num","Freq2")
PANC1_sp_sv_on_chrom <- ggplot(PANC1, aes(x=Var1, y=Freq2,fill=type)) +
  geom_bar(stat="identity", position="stack")+ 
  theme_bw() + theme(panel.grid = element_blank()) +
  scale_fill_manual(values=my14colors) + 
  labs(title="PANC1",x="Chromosome", y = "Normalized Count") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  theme(legend.key.size=unit(3,'mm')) +
  ylim(c(0,2500))
#x<-length(BxPC3_specific_sv$types)
#x=Member, y=Percentage, fill = factor(Percentage))

BxPC3_sp_sv_on_chrom <- ggplot(BxPC3, aes(x = Var1, y=Freq2,fill=type)) +
  geom_bar(stat="identity", position="stack") + 
  theme_bw() + theme(panel.grid = element_blank()) +
  scale_fill_manual(values=my14colors) + 
  labs(title="BxPC3",x="Chromosome", y = "Normalized Count") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  theme(legend.key.size=unit(3,'mm')) +
  ylim(c(0,2500))

grid.arrange(BxPC3_sp_sv_on_chrom,PANC1_sp_sv_on_chrom, nrow=2)
