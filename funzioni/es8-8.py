'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.'''




def make_album(artist_name:str, album_title:str, n_songs:int=None) -> dict:
    

    if n_songs is None:
        return {'Artista':artist_name, 'Album':album_title}
    
    if n_songs!=None:
        
        return {'Artista':artist_name, 'Album':album_title, 'Numero canzoni':n_songs}






dream = make_album("Dream Theater", "Images and words", 8)




while True:
    
    enter_artist:str = str(input("Inserisci nome artista ('esc' per uscire): "))
    
    
    if enter_artist=="esc":
        break

    enter_album:str = str(input("Inserisci titolo album ('esc' per uscire): "))

    if enter_album=="esc":
        break

    enter_n_songs:str = str(input("Inserire il numero di canzoni (opzionale). ('no' per andare avanti, 'esc' per uscire): "))
    
    if enter_n_songs=="esc":
        break
    elif enter_n_songs=="no":
        print(make_album(artist_name=enter_artist, album_title=enter_album))
    


   #prova is digit 
    elif enter_n_songs!=None and type(int(enter_n_songs))==int:

        print(make_album(artist_name=enter_artist, album_title=enter_album, n_songs=enter_n_songs))
    else:
        print(make_album(artist_name=enter_artist, album_title=enter_album))






