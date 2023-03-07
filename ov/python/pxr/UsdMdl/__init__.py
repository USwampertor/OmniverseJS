#******************************************************************************
# * Copyright 2019 NVIDIA Corporation. All rights reserved.
# *****************************************************************************
#
# NVIDIA Material Definition Language (MDL) USD plugins.
#
# MDL Search Paths
# ================
# At startup (i.e. when the MDL SDK is loaded) MDL search path is set in this order:
# 1/ Dedicated environement variable
#    If it is set, PXR_USDMDL_PLUGIN_SEARCH_PATHS overwrites any MDL search path.
#    PXR_USDMDL_PLUGIN_SEARCH_PATHS can be set to a list of paths.
# 2/ System and User Path
#    if PXR_USDMDL_PLUGIN_SEARCH_PATHS is not set:
#    a/ If set, add MDL_SYSTEM_PATH to the MDL search path
#    b/ If set, add MDL_USER_PATH to the MDL search path
#
# Discovery plugin
# ================
# MDL discovery plugin is derived from NdrDiscoveryPlugin interface.
# This plugin finds MDL functions and materials from all the modules found in the
# MDL search paths.
# This discovery plugin is executed as soon as the registry is instantiated,
# for example in Python:
#
#    >>> from pxr import Sdr
#    >>> reg = Sdr.Registry()
#
# MDL discovery plugin creates a discovery result (NdrNodeDiscoveryResult)
# for each material and each function that is found.
#
# Parser plugin
# ================
# MDL parser plugin is derived from NdrParserPlugin interface.
# This plugin is responsible to parse a given MDL function or material and
# create an NdrNode instance. 
# The parser plugin which is run is decided based on the discovery result discoveryType.
# The parser plugin is invoked whenever a shader node is requested, for example in Python:
#
#    >>> from pxr import Sdr
#    >>> MDLQualifiedName = "::material_examples::architectural::architectural"
#    >>> Sdr.Registry().GetShaderNodeByIdentifierAndType(MDLQualifiedName, "mdl")
#
# NdrNodes which is created contains a list of properties which are translated
# from MDL parameters.
#
from . import _usdMdl
from pxr import Tf
Tf.PrepareModule(_usdMdl, locals())
del Tf

try:
    import __DOC
    __DOC.Execute(locals())
    del __DOC
except Exception:
    try:
        import __tmpDoc
        __tmpDoc.Execute(locals())
        del __tmpDoc
    except:
        pass
