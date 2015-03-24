library(randomForest)

setwd("F:\\Applied machine learning\\bike-sharing\\code")
ntrees <- 1
mtry <- 1

#formula = registered~datetime+season+holiday+workingday+weather+temp+atemp+humidity+windspeed
output = 'registered'
output_file = "../data/sub1.csv"


### Load the data set
d <- read.csv(file="../data/train.csv",head=TRUE,sep=",");


y = d[[output]] # value to predict
d <- d[,!names(d) %in% c("casual", "registered", "count")]; # remove outputs
#d[[output]] <- y

### Transform the datetime into just the time
tmp <- as.character(d[,"datetime"]);
d[,"datetime"] <- as.factor(sapply(strsplit(tmp, " "), "[[", 2)) # remove the date

### Train the random forest
rf <- randomForest(d, y, ntrees=ntrees, mtry = mtry);


### Load the test set
d_test <- read.csv("../data/test.csv",head=TRUE,sep=',');
submission <- data.frame(d_test[["datetime"]]);

### Change datetime to time
tmp <- as.character(d_test[,"datetime"]);
d_test[,"datetime"] <- as.factor(sapply(strsplit(tmp, " "), "[[", 2)) # remove the date

### Predict the values
d_pred <- predict(rf, d_test);

### Save the predictions
submission[["count"]] <- d_pred;
colnames(submission) <- c("datetime", "count");
write.csv(submission, output_file, row.names=F, quote=F);
