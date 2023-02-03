# Requires Misc Military Assets mod :
# https://forum.dcs.world/topic/316494-misc-military-assets-by-currenthill/
#
from dcs import unittype

from game.modsupport import vehiclemod

@vehiclemod
class M142_HIMARS_GLSDB(unittype.VehicleType):
        id = "M142_HIMARS_GLSDB"
        name = "M142 HIMARS (GLSDB)"
        detection_range = 0
        threat_range = 150000
        air_weapon_dist = 150000
        eplrs = True
        
@vehiclemod
class M142_HIMARS_ATACMS(unittype.VehicleType):
        id = "M142_HIMARS_ATACMS"
        name = "M142 HIMARS (ATACMS)"
        detection_range = 0
        threat_range = 296000
        air_weapon_dist = 296000
        eplrs = True

@vehiclemod
class M142_HIMARS_GMLRS(unittype.VehicleType):
        id = "M142_HIMARS_GMLRS"
        name = "M142 HIMARS (GMLRS)"
        detection_range = 0
        threat_range = 92000
        air_weapon_dist = 92000
        eplrs = True