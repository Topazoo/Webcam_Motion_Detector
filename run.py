#!/usr/bin/env python
import sys
from lib.interface.clahandler import CLA_Handler, Dispatcher

def run(cla=" ".join(sys.argv[1::])):

    # Read CLAs
    cla_handler = CLA_Handler()
    commands = cla_handler.parse(cla)

    # Execute CLAs
    dispatcher = Dispatcher()
    dispatcher.run(commands)

run()