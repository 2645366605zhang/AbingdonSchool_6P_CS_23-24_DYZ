
class LocationLevel:

    def __init__(self, localization: str) -> None:
        self._localization = localization
    
    def GetLocalization(self) -> str:
        return self._localization

locationLevels = {
    # For Travel Map
    "NML" : LocationLevel("No Man's Land"),
    "PST" : LocationLevel("Pastoral"),
    "RRL" : LocationLevel("Rural"),
    "STN" : LocationLevel("Small Town"),
    "MTN" : LocationLevel("Medium Town"),
    "LTN" : LocationLevel("Large Town"),
    "SCT" : LocationLevel("Small City"),
    "MCT" : LocationLevel("Medium City"),
    "LCT" : LocationLevel("Large City"),
    # For Cartesian Map
    "GND" : LocationLevel(" "), # Ground
    "COV" : LocationLevel("▒"), # Cover
    "WAL" : LocationLevel("▓") # Wall
}