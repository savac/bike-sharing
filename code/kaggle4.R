library(xts)
library(randomForest)

Sys.setlocale("LC_ALL","English")

train <- read.csv("../train.csv")
test <- read.csv("../test.csv")

## Train
#Convert datetime into timestamps (split day and hour)
train$datetime <- as.character(train$datetime)
train$datetime <- strptime(train$datetime, format="%Y-%m-%d %T", tz="EST")
ind_train <- unique(format(train$datetime, format = "%Y-%m"))

#convert hours to factors in separate feature
train$hour <- as.integer(substr(train$datetime, 12,13))
train$hour <- as.factor(train$hour)

#Day of the week
train$weekday <- as.factor(weekdays(train$datetime))

train$datetime <- strptime(train$datetime, format="%Y-%m-%d")

train_xts <- xts(train[,-1], order.by = train$datetime)

## Test
#Convert datetime into timestamps (split day and hour)
test$datetime <- as.character(test$datetime)
test$datetime <- strptime(test$datetime, format="%Y-%m-%d %T", tz="EST")

#convert hours to factors in separate feature
test$hour <- as.integer(substr(test$datetime, 12,13))
test$hour <- as.factor(test$hour)

#Day of the week
test$weekday <- as.factor(weekdays(test$datetime))

test$datetime <- strptime(test$datetime, format="%Y-%m-%d")

test_xts <- xts(test[,-1], order.by = test$datetime)

res <- NULL

for (ind in ind_train) {
  print(ind)
  
  # Growing window
  tmp <- as.data.frame(train_xts[paste0("/", ind)])
  tmp_test <- as.data.frame(test_xts[ind])
  row.names(tmp) <- NULL
  row.names(tmp_test) <- NULL
  
  y_casual <- as.numeric(tmp[,"casual"])
  y_reg <- as.numeric(tmp[,"registered"])
  tmp <- tmp[, !names(tmp) %in% c("casual", "registered", "count")]
  
  names <- c("season", "holiday", "workingday", "weather", "hour", "weekday") # Factors
  names_num <- c("temp", "atemp", "humidity", "windspeed") # Numerics
  
  dataset <- rbind(cbind(tmp, typ = 0), cbind(tmp_test, typ = 1))
  dataset[, names_num] <- lapply(dataset[,names_num], as.numeric)
  dataset[, names] <- lapply(dataset[,names], as.factor)

  casual <- randomForest(x = dataset[dataset$typ == 0, -11], y = y_casual, ntree = 500)
  registered <- randomForest(x = dataset[dataset$typ == 0, -11], y = y_reg, ntree = 500)
  pred_casual <- predict(casual, dataset[dataset$typ == 1, -11])
  pred_reg <- predict(registered, dataset[dataset$typ == 1, -11])
  res <- rbind(res, as.matrix(round(pred_casual + pred_reg, 0)))
  
}

sub <- read.csv("C:/c4/sampleSubmission.csv")
sub$count <- res
write.csv(sub, file = "C:/c4/sub4.csv", row.names = F, quote = F)
