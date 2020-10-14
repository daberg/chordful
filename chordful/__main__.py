from chordful.run import runApp

import os
import sys


usage = "Chordful Web App\nUsage: python -m chordful [CONFIG_FILE]"

def die(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(-1)

if len(sys.argv) != 2:
    die(usage)

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(usage)
    sys.exit(0)

configPath = sys.argv[1]

if not os.path.isfile(configPath):
    die("Error: '{}' is not an accessible file".format(configPath))

runApp(configPath)
