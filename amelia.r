td = read.csv('./cleaned_TrainingData.csv')
td$weekday = as.integer(td$weekday)
td = apply(td, 2, as.numeric)
td[which(is.na(td))]=0

#filtered = filter(td, )
pca = prcomp(td)
lm

library(Amelia)
amelia(TrainingData, m = 5, ps2 = 1)

#getwd()
#TrainingData = read.csv("data/TrainingData.csv")
#summary(TrainingData)
#glm(TrainingData$Ambient.Max.Temperature_14 ~ TrainingData$target_4_1) -> fitx
#plot(fitx)
#TrainingData$weekday = as.integer(TrainingData$weekday)
#
#
#
# load('./data/cleaned.RData')
#
#library(Amelia)
#cleaned$weekday = as.integer(cleaned$weekday)
#amelia(cleaned)
