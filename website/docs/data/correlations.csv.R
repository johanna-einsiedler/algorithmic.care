# Attach libraries (must be installed)
library(readr)
library(dplyr)
library(tidyr)
#setwd('/Users/htr365/Documents/Side_Projects/09_founding_lab/03_spring_term/project/')
#surveyData <- read.csv('/Users/htr365/Documents/Side_Projects/09_founding_lab/03_spring_term/project/dashboard_v1/docs/data/study_data.csv')
surveyData <- read.csv('docs/data/data_sources/study_data.csv')
#allData<- read.csv('/Users/htr365/Documents/Side_Projects/09_founding_lab/03_spring_term/project/dashboard_v1/docs/data/features.csv')
#featuresBiosignals <- read.csv('/Users/htr365/Documents/Side_Projects/09_founding_lab/03_spring_term/project/dashboard_v1/docs/data/features_biosignals.csv')
#orgData <- read.csv('/Users/htr365/Documents/Side_Projects/09_founding_lab/03_spring_term/project/dashboard_v1/docs/data/concated_data.csv')
featuresBiosignals <- read.csv('docs/data/data_sources/features_biosignals.csv')
orgData <- read.csv('docs/data/data_sources/concated_data.csv')



signalData <- orgData %>% left_join(featuresBiosignals, by=c('id'='id'))


signalData <- signalData %>% mutate(muscle_PM = paste0(muscle,'_',time_of_day)) %>% group_by(date,muscle_PM) %>% slice(1)
mean_median_freq <- signalData %>% select(c(date,muscle_PM, mean_median_freq)) %>% 
  pivot_wider(id_cols=date,names_from=muscle_PM, values_from=c(mean_median_freq))%>% mutate(date=as.Date(date))
max_median_freq <- signalData %>% select(c(date,muscle_PM, max_median_freq)) %>% 
  pivot_wider(id_cols=date,names_from=muscle_PM, values_from=c(max_median_freq)) %>% mutate(date=as.Date(date))

surveyData_numeric <- surveyData %>% 
  mutate_at(vars(steps,fatigue,dress_shower,stairs,common,pain, rash,wellness,tomorrow,pred_yesterday),
as.numeric
) %>% mutate(date=as.Date(date,format='%m/%d/%Y'))


surveyData_numeric <- surveyData_numeric %>% mutate(fatigue_next_day = lead(fatigue))
finalData <- surveyData_numeric %>% left_join(mean_median_freq, by=c('date'='date')) %>% select(!c(id,date,symptoms))

#%>% 
 # left_join(max_median_freq, by=c('date'='date')) 

correlations <- data.frame(cor(finalData, use='pairwise.complete.obs'))
correlations$v1 <- rownames(correlations)
correlations <- correlations %>% pivot_longer(cols=names(correlations)[1:length(names(correlations))-1])
names(correlations) <- c('v1','v2','cor')
surveyLong <- surveyData %>% pivot_longer(cols=c('wellness','tomorrow','steps','fatigue','dress_shower',
                                   'stairs','common','pain','rash','pred_yesterday'),
                                   names_to = 'variable',
                                   values_to = 'y')
cat(format_csv(correlations))