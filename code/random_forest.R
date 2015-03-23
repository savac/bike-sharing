library(randomForest)

# Load the data set
d <- read.csv(file="../data/train.csv",head=TRUE,sep=",");
d <- d[,!names(d) %in% c("casual", "registered")];

tmp <- as.character(d[,"datetime"]);
d[,"datetime"] <- as.factor(sapply(strsplit(tmp, " "), "[[", 2)) # remove the date

d_test <- read.csv("../data/test.csv",head=TRUE,sep=',');
submission <- data.frame(d_test[["datetime"]]);
tmp <- as.character(d_test[,"datetime"]);
d_test[,"datetime"] <- as.factor(sapply(strsplit(tmp, " "), "[[", 2)) # remove the date

rf <- randomForest(d[,!names(d) %in% c("count")], d[,"count"], ntree = 1000, mtry = 20);
d_pred <- predict(rf, d_test);

submission[["count"]] <- d_pred;
colnames(submission) <- c("datetime", "count");
write.csv(submission, "../data/sub1.csv", row.names=F, quote=F);
