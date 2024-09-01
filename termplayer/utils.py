import logging
import os
import shutil

def setup_logging(log_level):
    logging.basicConfig(level=getattr(logging, log_level.upper()))

def cleanup_resources():
    resources = "../resources"
    if os.path.exists(resources):
        shutil.rmtree(resources)
    os.mkdir(resources)
    os.mkdir(resources + "/frames")
