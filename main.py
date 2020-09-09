import mine232 as mn

# mn.UpdateProdClass()
# mn.UpdateHeader()

# my_request = mn.ExclusionRequest(25663) #25635)
# print(f"ID: {my_request.id}")
# print(f"url: {my_request.url}")
# print(f"\nhtml: \n{my_request.html[0:200]}")
# print(f"\nsoup: \n{str(my_request.soup)[0:200]}")
# print(f"\npretty: \n{str(my_request.pretty())[0:200]}")
# print(f"\ntags: \n")
# print(f"\ndata: \n{my_request.data}")
# print(f"\nvalues: \n{my_request.values()}")
# print(f"\ncaptions: \n{my_request.captions()}")

my_erl = mn.ERList([25635, 25663, 9999999])
print(f"\nIDs: \n{my_erl.er_ids}")
print(f"\nerrors: \n{my_erl.errors}")
print(f"\nextracted: \n{my_erl.extracted}")
# print(f"\ndata: \n{my_erl.data}")
print(f"\nDataFrame: \n{my_erl.df}")