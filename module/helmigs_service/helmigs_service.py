import logging

import openerp.release
import openerp.tools
from openerp.tools.translate import _

import security

_logger = logging.getLogger(__name__)

RPC_VERSION_1 = {
        'server_version': openerp.release.version,
        'server_version_info': openerp.release.version_info,
        'server_serie': openerp.release.serie,
        'protocol_version': 1,
}

def exp_version():
    return RPC_VERSION_1
