import subprocess
import os

subprocess.Popen(["paplay", f"{os.path.dirname(__file__)}/test.wav"])
