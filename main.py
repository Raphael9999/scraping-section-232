import mine232 as mn

# individual request processing
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

# update yaml
# mn.UpdateProdClass()
# mn.UpdateHeader()

# process lists of exclusion requests
# my_erl = mn.ERList([25663, 25635, 9999999, 25635])
my_erl = mn.ERList(from_id=25000, to_id=25010)
# print(f"\nIDs: \n{my_erl.er_ids}")
print(f"\nerrors: \n{my_erl.errors}")
print(f"\nextracted: \n{my_erl.extracted}")
print(f"\nfrom-to: \n{my_erl.fromto}")
print(f"\nDataFrame: \n{my_erl.df.shape}")
my_erl.df.to_csv(f'result\extract_232_{my_erl.fromto}.csv', index = False) 