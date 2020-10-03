#              Logging
#Purpose: Record progress and Problems
#Levels: Debug(10), Info(20), Warning(30), Error(40), Critical(50)

import logging

#! in logging dir all capped words are constants. Cap first letters 
#! are classes. lower case first letter are functions

#create and configure logger
logging.basicConfig(filename= "logger.txt", level= __debug__)
#! message level must be greater than set level to get into file
#! right now set level is debug which is 10
logger = logging.getLogger()

logger.info("Our first message")

print(logger.level)