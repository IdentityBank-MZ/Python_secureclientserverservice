# -*- coding: utf-8 -*-
# * ********************************************************************* *
# *                                                                       *
# *   Secure Client-Server Service module                                 *
# *   This file is part of secureclientserverservice.                     *
# *   This project may be found at:                                       *
# *   https://github.com/IdentityBank/Python_secureclientserverservice.   *
# *                                                                       *
# *   Copyright (C) 2020 by Identity Bank. All Rights Reserved.           *
# *   https://www.identitybank.eu - You belong to you                     *
# *                                                                       *
# *   This program is free software: you can redistribute it and/or       *
# *   modify it under the terms of the GNU Affero General Public          *
# *   License as published by the Free Software Foundation, either        *
# *   version 3 of the License, or (at your option) any later version.    *
# *                                                                       *
# *   This program is distributed in the hope that it will be useful,     *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of      *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the        *
# *   GNU Affero General Public License for more details.                 *
# *                                                                       *
# *   You should have received a copy of the GNU Affero General Public    *
# *   License along with this program. If not, see                        *
# *   https://www.gnu.org/licenses/.                                      *
# *                                                                       *
# * ********************************************************************* *

################################################################################
# Import(s)                                                                    #
################################################################################

from .scsscommon import ScssCommon, ScssConfig
from .scsssecurity import ScssSecurityFirewall, ScssSecurityType, ScssSecurityHelper
from .scssprotocol import ScssProtocol
from .scssclient import ScssClient, ScssClientInet, ScssEchoClientInet
from .scssserver import ScssServer, ScssServerInet, ScssEchoServerInet, ScssServerUnix
from .scsshelper import ScssServerHelper, ScssClientHelper


################################################################################
# Module                                                                       #
################################################################################

def startServer(serverConfig):
    return False


def connectClient(connectionConfig):
    return False


__all__ = ('ScssCommon',
           'ScssConfig',
           'ScssProtocol',
           'ScssSecurityFirewall',
           'ScssSecurityType',
           'ScssSecurityHelper',
           'ScssClient',
           'ScssClientInet',
           'ScssEchoClientInet',
           'ScssServer',
           'ScssServerInet',
           'ScssEchoServerInet',
           'ScssServerUnix',
           'ScssServerHelper',
           'ScssClientHelper')

################################################################################
#                                End of file                                   #
################################################################################