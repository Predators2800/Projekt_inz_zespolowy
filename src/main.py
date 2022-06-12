from dict_parser import parser_run
from frontend import app_init,interface_init,set_global_callbacks,app_run,app_cleanup
from backend import *

"""INITIALIZE"""
parser_run()
app_init()
interface_init()
set_global_callbacks()

"""RUN MAIN LOOP"""
app_run()

"""CLEANUP"""
app_cleanup()