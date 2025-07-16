import subprocess

result = subprocess.run(["host","8.8.8.8"], capture_output=True)
print(result.returncode)
# hasil = 0

print(result.stdout)
# hasil = b'8.8.8.8.in-addr.arpa domain name pointer dns.google. \n'

print(result.stdout.decodde().split())
# hasil = ['b'8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

result = subprocess.run(["rm","does_not_exist"],capture_output=True)
print(result.returncode)
#hasil = 1
print(result.stdout)
#hasil = b''
print(result.stderr)
#hasil = b"rm: cannot remove 'does_not_exist': No such file or directory"


