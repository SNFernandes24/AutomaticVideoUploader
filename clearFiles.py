import os
import glob

def clearDirectory():
    file_path = glob.glob(os.path.dirname(os.path.realpath(__file__)) + "\\RedditDownload\\*")
    for f in file_path:
        os.remove(f)