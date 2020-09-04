import mine232 as mn

my_request = mn.ExclusionRequest(25635)
print(f"ID: {my_request.id}")
print(f"url: {my_request.url}")
print(f"\nhtml: \n{my_request.html[0:50]}")
print(f"\nsoup: \n{str(my_request.soup)[0:100]}")
print(f"\npretty: \n{str(my_request.pretty())[0:100]}")
print(f"\ntags: \n")
print(f"\ndata: \n{my_request.data}")