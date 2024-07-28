# Attach libraries (must be installed)
library(readr)
library(dplyr)
library(tidyr)
#surveyData <- read.csv('/Users/htr365/Documents/Side_Projects/09_founding_lab/amanda_johanna/quantified_self/website/docs/data/data_sources/study_data.csv')
surveyData <- read.csv('docs/data/data_sources/study_data.csv')

surveyData <- surveyData %>% select(!symptoms,!steps,!tomorrow, !pred_yesterday) %>%  mutate_at(vars(steps,fatigue,dress_shower,stairs,common,pain, rash,wellness,tomorrow,pred_yesterday),
                           as.numeric) %>% pivot_longer(cols = c('fatigue','dress_shower','stairs','common','pain','rash','wellness'))


cat(format_csv(surveyData))
