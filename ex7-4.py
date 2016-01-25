def testme(item):
	if len(item) < 5:
		return False
	else:
		if not item.isdigit() and item.isalnum():
			for char in item:
				if char.isdigit():
					return True
		else:
			return False