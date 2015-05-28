# -*- coding: utf-8 -*-
"""
This file contains the QuDi console GUI module.

QuDi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

QuDi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with QuDi. If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2015 Jan M. Binder jan.binder@uni-ulm.de
"""
import os
import numpy as np
from collections import OrderedDict
from gui.GUIBase import GUIBase
from IPython.lib.kernel import connect_qtconsole

class IPythonGui(GUIBase):
    """
    """
    _modclass = 'IPythonGui'
    _modtype = 'gui'
    def __init__(self, manager, name, config, **kwargs):
        """Create the console gui object.
          @param object manager: Manager object that this module was loaded from
          @param str name: Unique module name
          @param dict config: Module configuration
          @param dict kwargs: Optional arguments as a dict
        """
        c_dict = {'onactivate': self.initUI}
        super().__init__(manager, name, config, c_dict)

        ## declare connectors
        self.connector['in']['ipythonlogic'] = OrderedDict()
        self.connector['in']['ipythonlogic']['class'] = 'IPythonLogic'
        self.connector['in']['ipythonlogic']['object'] = None

        self.consoles = list()

    def initUI(self, e=None):
        """Create all UI objects and show the window.
          @param object e: Fysom state change notice
        """
        pass
       
    def show(self):
        """Make sure that the window is visible and at the top.
        """
        ipythonlogic = self.connector['in']['ipythonlogic']['object'] 
        if ipythonlogic.getState() != 'deactivated':
            con = connect_qtconsole(ipythonlogic.ipykernel.connection_file)
        self.consoles.append(con)
 