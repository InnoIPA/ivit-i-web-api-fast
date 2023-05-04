# Copyright (c) 2023 Innodisk Corporation
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


# Basic
import json, threading, time, sys, os, re
import logging as log
from fastapi import APIRouter,status
from fastapi.responses import Response
from typing import Optional, Dict, List
from pydantic import BaseModel

from ..common import SERV_CONF
from ..handlers.mesg_handler import http_msg

# --------------------------------------------------------------------
# Router
proc_router = APIRouter(tags=["process"])


# Helper

def check_proc():
    if SERV_CONF.get("PROC") is None:
        SERV_CONF.update({"PROC": {}})


# API
@proc_router.get("/process")
async def get_model_proc_list():

    try:
        check_proc()
        return http_msg( content = SERV_CONF["PROC"], status_code = 200 )

    except Exception as e:
        return http_msg( content=e, status_code = 500 )

@proc_router.get("/process/{uid}")
async def get_model_proc_list(uid:str):

    try:
        check_proc()
        return http_msg( content = SERV_CONF["PROC"].get(uid), status_code = 200 )

    except Exception as e:
        return http_msg( content=e, status_code = 500 )