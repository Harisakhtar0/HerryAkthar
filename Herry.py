import os, platform

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from herry import Herry

    Herry()

elif bit == '32bit':

    from details import Herry

    Herry()
