# Copyright 2008, Red Hat, Inc
# Steve Salevan <ssalevan@redhat.com>
#
# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import func_module
import func.overlord.client as fc
from certmaster import certmaster as certmaster
from func import utils

class OverlordModule(func_module.FuncModule):

    version = "0.0.1"
    api_version = "0.0.1"
    description = "Module for controlling minions that are also overlords."

    def map_minions(self,get_only_alive=False):
        """
        Builds a recursive map of the minions currently assigned to this
        overlord
        """
        maphash = {}
        current_minions = []
        if get_only_alive:
            ping_results = fc.Overlord("*").test.ping()
            for minion in ping_results.keys():
                if ping_results[minion] == 1: #if minion is alive
                    current_minions.append(minion) #add it to the list of current minions
        else:
            cm = certmaster.CertMaster()
            current_minions = cm.get_signed_certs()
        for current_minion in current_minions:
            maphash[current_minion] = fc.Overlord(current_minion).overlord.map_minions()[current_minion]
        return maphash
        
    
