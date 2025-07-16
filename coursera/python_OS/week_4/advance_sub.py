import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/advance_sub/", my_env["PATH"]])
result = subprocess.run(["advance_sub"],env=my_env)

