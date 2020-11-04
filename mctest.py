from mcrcon import MCRcon

#host = "127.0.0.1"
#port = "1244"
#password = "Psx300ctf"

host = ("localhost", int(1244))
password = "Psx300ctf"

with MCRcon(host, password) as mcr:
	resp = mcr.command("/who")
	print(resp)
