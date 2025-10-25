Here_the_Anime_list = [ ]

while True:
	anime1 =input("Enter the title for an anime list (or type 'exit' to finish): ").lower()
	
	if anime1 == 'exit':
		print('Your anime list')
		break
	
	else:
		Here_the_Anime_list.append(anime1)
		print(f'{anime1}, has been added to your list')
		
print("Here the Anime list: ")
for anime in Here_the_Anime_list:
	print(f"* {anime} ")