def parse_official_type(username: str):
	if username == "admin":
		return 1
	if username == "tsg_official":
		return 2
	if username.endswith("governor"):
		return 3
	return 4