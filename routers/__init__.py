from os import listdir
from pathlib import Path

path_parent = Path("./routers")

for module in listdir(path_parent):
    if 'router' in module:
        __import__(
            f'routers.{module[0:-3]}',
            locals(),
            globals()
        )