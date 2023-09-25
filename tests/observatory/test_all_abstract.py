import pytest

from pyscope.observatory import (
    WCS,
    Autofocus,
    Camera,
    CoverCalibrator,
    Device,
    Dome,
    FilterWheel,
    Focuser,
    ObservingConditions,
    Rotator,
    SafetyMonitor,
    Switch,
    Telescope,
)
from pyscope.observatory._docstring_inheritee import _DocstringInheritee


@pytest.mark.parametrize(
    "cls_name",
    [
        Autofocus,
        Camera,
        CoverCalibrator,
        Dome,
        Device,
        FilterWheel,
        Focuser,
        ObservingConditions,
        Rotator,
        SafetyMonitor,
        Switch,
        Telescope,
        WCS,
    ],
)
class TestAllAbstractClasses:
    def test_meta(self, cls_name):
        assert type(cls_name) is _DocstringInheritee

    def test_abstract(self, cls_name):
        with pytest.raises(TypeError):
            cls_name()

    '''def test_init_docstring(self, cls_name):
        assert cls_name.__doc__ is None
        assert (
            cls_name.__init__.__doc__
            != """Initialize self.  See help(type(self)) for accurate signature."""
        )'''

    """def test_func_docstring(self, cls_name):
        for name in cls_name.__dict__:
            if name != "__doc__":
                assert getattr(cls_name, name).__doc__ is not None"""


@pytest.mark.parametrize(
    "cls_name,methods",
    [
        (Autofocus, {"Run", "Abort", "__init__"}),
        (
            Camera,
            {
                "AbortExposure",
                "PulseGuide",
                "StartExposure",
                "StopExposure",
                "__init__",
                "BayerOffsetX",
                "BayerOffsetY",
                "BinX",
                "BinY",
                "CameraState",
                "CameraXSize",
                "CameraYSize",
                "CanAbortExposure",
                "CanAsymmetricBin",
                "CanFastReadout",
                "CanGetCoolerPower",
                "CanPulseGuide",
                "CanSetCCDTemperature",
                "CanStopExposure",
                "CCDTemperature",
                "CoolerOn",
                "CoolerPower",
                "ElectronsPerADU",
                "ExposureMax",
                "ExposureMin",
                "ExposureResolution",
                "FastReadout",
                "FullWellCapacity",
                "Gain",
                "GainMax",
                "GainMin",
                "Gains",
                "HasShutter",
                "HeatSinkTemperature",
                "ImageArray",
                "ImageReady",
                "IsPulseGuiding",
                "LastExposureDuration",
                "LastExposureStartTime",
                "MaxADU",
                "MaxBinX",
                "MaxBinY",
                "NumX",
                "NumY",
                "Offset",
                "OffsetMax",
                "OffsetMin",
                "Offsets",
                "PercentCompleted",
                "PixelSizeX",
                "PixelSizeY",
                "ReadoutMode",
                "ReadoutModes",
                "SensorName",
                "SensorType",
                "SetCCDTemperature",
                "StartX",
                "StartY",
                "SubExposureDuration",
            },
        ),
        (
            CoverCalibrator,
            {
                "CalibratorOff",
                "CalibratorOn",
                "CloseCover",
                "HaltCover",
                "OpenCover",
                "Brightness",
                "CalibratorState",
                "CoverState",
                "MaxBrightness",
                "__init__",
            },
        ),
        (
            Dome,
            {
                "AbortSlew",
                "CloseShutter",
                "FindHome",
                "OpenShutter",
                "Park",
                "SetPark",
                "SlewToAltitude",
                "SlewToAzimuth",
                "SyncToAzimuth",
                "Altitude",
                "AtHome",
                "AtPark",
                "Azimuth",
                "CanFindHome",
                "CanPark",
                "CanSetAltitude",
                "CanSetAzimuth",
                "CanSetPark",
                "CanSetShutter",
                "CanSlave",
                "CanSyncAzimuth",
                "ShutterStatus",
                "Slaved",
                "Slewing",
                "__init__",
            },
        ),
        (Device, {"Connected", "Name", "__init__"}),
        (FilterWheel, {"FocusOffsets", "Names", "Position", "__init__"}),
        (
            Focuser,
            {
                "Halt",
                "Move",
                "Absolute",
                "IsMoving",
                "Link",
                "MaxIncrement",
                "MaxStep",
                "Position",
                "StepSize",
                "TempComp",
                "TempCompAvailable",
                "Temperature",
                "__init__",
            },
        ),
        (
            ObservingConditions,
            {
                "Refresh",
                "SensorDescription",
                "TimeSinceLastUpdate",
                "AveragePeriod",
                "CloudCover",
                "DewPoint",
                "Humidity",
                "Pressure",
                "RainRate",
                "SkyBrightness",
                "SkyQuality",
                "SkyTemperature",
                "StarFWHM",
                "Temperature",
                "WindDirection",
                "WindGust",
                "WindSpeed",
                "__init__",
            },
        ),
        (
            Rotator,
            {
                "Halt",
                "Move",
                "MoveAbsolute",
                "MoveMechanical",
                "Sync",
                "CanReverse",
                "IsMoving",
                "MechanicalPosition",
                "Position",
                "Reverse",
                "StepSize",
                "TargetPosition",
                "__init__",
            },
        ),
        (SafetyMonitor, {"IsSafe", "__init__"}),
        (
            Switch,
            {
                "CanWrite",
                "GetSwitch",
                "GetSwitchDescription",
                "GetSwitchName",
                "MaxSwitchValue",
                "MinSwitchValue",
                "SetSwitch",
                "SetSwitchName",
                "SetSwitchValue",
                "SwitchStep",
                "MaxSwitch",
                "__init__",
            },
        ),
        (
            Telescope,
            {
                "AbortSlew",
                "AxisRates",
                "CanMoveAxis",
                "DestinationSideOfPier",
                "FindHome",
                "MoveAxis",
                "Park",
                "PulseGuide",
                "SetPark",
                "SlewToAltAz",
                "SlewToAltAzAsync",
                "SlewToCoordinates",
                "SlewToCoordinatesAsync",
                "SlewToTarget",
                "SlewToTargetAsync",
                "SyncToAltAz",
                "SyncToCoordinates",
                "SyncToTarget",
                "Unpark",
                "AlignmentMode",
                "Altitude",
                "ApertureArea",
                "ApertureDiameter",
                "AtHome",
                "AtPark",
                "Azimuth",
                "CanFindHome",
                "CanPark",
                "CanPulseGuide",
                "CanSetDeclinationRate",
                "CanSetGuideRates",
                "CanSetPark",
                "CanSetPierSide",
                "CanSetRightAscensionRate",
                "CanSetTracking",
                "CanSlew",
                "CanSlewAltAz",
                "CanSlewAltAzAsync",
                "CanSlewAsync",
                "CanSync",
                "CanSyncAltAz",
                "CanUnpark",
                "Declination",
                "DeclinationRate",
                "DoesRefraction",
                "EquatorialSystem",
                "FocalLength",
                "GuideRateDeclination",
                "GuideRateRightAscension",
                "IsPulseGuiding",
                "RightAscension",
                "RightAscensionRate",
                "SideOfPier",
                "SiderealTime",
                "SiteElevation",
                "SiteLatitude",
                "SiteLongitude",
                "Slewing",
                "SlewSettleTime",
                "TargetDeclination",
                "TargetRightAscension",
                "Tracking",
                "TrackingRate",
                "TrackingRates",
                "UTCDate",
                "__init__",
            },
        ),
        (WCS, {"Solve", "__init__"}),
    ],
)
class TestMethods:
    def test_methods(self, cls_name, methods):
        assert cls_name.__abstractmethods__ == frozenset(methods)