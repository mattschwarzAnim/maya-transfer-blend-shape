name = "maya_transferblendshape"
version = "1.1.1"

requires = [
    "maya>=2022",
    "numpy",
    "scipy",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

def commands():
    env.MAYA_PLUG_IN_PATH.append("{root}/plug-ins/")
    env.MAYA_SCRIPT_PATH.append("{root}/scripts")
    env.PYTHONPATH.append("{root}/scripts")
    env.XBMLANGPATH.append("{root}/icons")
