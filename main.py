import mymining as mm
import os
os.system('cls' if os.name == 'nt' else 'clear')

my_request = mm.ExclusionRequest(25635)
print(f"ID: {my_request.id}")
print(f"url: {my_request.url}")
print(f"html: {my_request.html[0:50]}")
print(f"soup: {str(my_request.soup)[0:100]}")
print(f"pretty: {str(my_request.pretty)[0:100]}")
print(f"tags: ")
print(my_request.tags)