# Copyright (c) 2023 Innodisk Corporation
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
import time
import zipfile
import gdown
import subprocess as sp
import logging as log

try:
    from ..common import SERV_CONF
    from ..handlers import model_handler
except:
    from common import SERV_CONF
    from handlers import model_handler

try:
    from .palette import palette
except:
    from palette import palette
"""
This is a utils for samples
Use gdown to download ai model and testing data.
"""

def extract_file(zip_path:str, folder_name:str=None):
    
    if not os.path.exists(zip_path):
        raise FileNotFoundError("ZIP Path is unavailable: {}".format(zip_path))
    
    if not folder_name:
        folder_name = os.path.splitext(zip_path)[0]

    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(path=folder_name)

    os.remove(zip_path)

def download_file(file_path, file_url):
    check_data = file_path
    if os.path.splitext(file_path)[1] == '.zip':
        check_data = os.path.splitext(file_path)[0]

    if os.path.exists(check_data):
        return

    gdown.download(url=file_url, output=file_path, quiet=False, fuzzy=True)

def download_model(file_name, file_url):

    file_path = os.path.join(SERV_CONF["MODEL_DIR"], file_name)

    if os.path.exists(file_path):
        log.debug(f'Model exists ({file_path})')
        return

    ext = '.zip'
    if not ext in file_path:
        file_path += ext
    download_file(file_path, file_url)
    extract_file(file_path)
    model_folder_path = os.path.splitext(file_path)[0]
    model_handler.convert_model(model_folder_path)

def download_data(file_name, file_url):
    file_path = os.path.join(SERV_CONF["DATA_DIR"], file_name)
    download_file(file_path, file_url)


def load_palette(label_path:str) -> dict:
    """Trying to generate a whole label palette"""
    with open(label_path, 'r') as f:

        ret = {}
        for idx, line in enumerate(f.readlines()):
            line = line.strip()
            ret[line] = palette[str(idx+1)]
    
    return ret
            