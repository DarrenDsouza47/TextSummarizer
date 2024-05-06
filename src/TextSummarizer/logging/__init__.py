import os
import logging
import sys

format_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

file_dir="logs"
file_path=os.path.join(file_dir,"running_logs.logs")
os.makedirs(file_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=format_str,
    handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("TextSummarizerLogger")
