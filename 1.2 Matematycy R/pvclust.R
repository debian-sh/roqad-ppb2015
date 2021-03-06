install.packages("pvclust")
library("pvclust")
fit<- pvclust(dis, method.hclust="ward.D2", method.dist="euclidean")
plot(fit)
pvrect(fit, alpha=.95)
pvpick(fit)
