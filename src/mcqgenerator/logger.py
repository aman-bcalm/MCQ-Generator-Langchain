import logging
import os
from datetime import datetime

#get the current date n time. 
# format it and store as datenow.log file
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#get current working direct and create folder logs inside it
#get that path for the above
log_path=os.path.join(os.getcwd(),"logs")

#pass the path to the makedirs method to create it
os.makedirs(log_path,exist_ok=True)


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

#level from INFO onwards capture all information
logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)