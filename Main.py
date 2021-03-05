#Movie Store where user can add, remove and delete and Edit movies. Use can also search the movie name. User can see the list of all movies as well.

class Movies:
    global movieStore
    movieStore=["intersteller","the great gatsby","12 angry men","requiem for a dream","death note"]

    #Search movie
    def searchMovie(self, moviename):
        print("\nSearch Result:")
        for i in range(len(movieStore)):
            if(movieStore[i] == moviename):
                print(movieStore[i]+" is found in the store")
                break
            elif (i ==len(movieStore)-1 and movieStore[i] !=moviename):
                print("Movie Not found")
                break

    #Display movies list
    def movieList(self):
        print("List of Movies\n")
        print('\n'.join(movieStore))

    #Add movie to the list
    def addMovie(self, moviename):
        for i in range(len(movieStore)):
            if(i == len(movieStore)-1 and movieStore[i] !=moviename):
                movieStore.append(moviename)
                print("\n"+moviename+" is added to the Store")
                print("UPDATED MOVIES LIST:\n")
                print('\n'.join(movieStore))
                break
            elif(movieStore[i] == moviename):
                print("Movie is already in the Store")
                break

    #delete movie from the list
    def deleteMovie(self, moviename):   
        for i in range(len(movieStore)):
            if(i == len(movieStore)-1 and movieStore[i] !=moviename):
                print("Movie is not in the Store")
                break
            elif(movieStore[i] == moviename):
                movieStore.remove(moviename)
                print("\n"+moviename+" is removed from the movie list")
                print("UPDATED MOVIES LIST:\n")
                print('\n'.join(movieStore))
                break

    #Update movie from the list
    def updateMovie(self, moviename,updatedname):
        for i in range(len(movieStore)):
            if(i == len(movieStore)-1 and movieStore[i] !=moviename):
                print("Movie is not in the Store")
                break
            elif(movieStore[i] == moviename):
                print("\n"+moviename+" is changeed to "+updatedname)
                movieStore[i] = updatedname
                print("UPDATED MOVIES LIST:\n")
                print('\n'.join(movieStore))
                break
        
def main():
    loginpin = 3040
    attempt = 3
    print("\t\t******************** WELCOME TO THE MOVIES STORE ********************")
    print("\n\nYOU ARE ALLOWED ONLY 3 LOGIN ATTEMPT, IF YOU ARE FAILED THE PROGRAM WILL BE TERMINATED: \n\n")
    print("ENTER LOGIN PIN: ")
    for i in range(attempt):
        pin = int(input())
        if(pin == loginpin):
            movies = Movies()
            while(True):
                print("\nWELCOME TO THE MOVIE STORE\n1. MOVIE LIST\n2. SEARCH A MOVIE\n3. ADD MOVIE\n4.DELETE MOVIE\n5.UPDATE MOVIE\n6.EXIT\n")
                user = int(input())
                if(user == 1):
                    print("\nMOVIES LIST:\n")
                    movies.movieList()
                elif(user == 2):
                    print("ENTER MOVIE NAME: ")
                    name = input()
                    movies.searchMovie(name)
                elif(user == 3 ):
                    name = input("ADD MOVIE TO THE STORE:\n")
                    movies.addMovie(name)
                elif(user == 4):
                    name = input("DELETE MOVIE FROM THE STORE:\n")
                    movies.deleteMovie(name)
                elif(user == 5):
                    movies.movieList()
                    name = input("\nENTER THE MOVIE NAME YOU WANT TO CHANGE:\n")
                    updated = input("ENTER THE UPDATED MOVIE NAME:\n")
                    movies.updateMovie(name,updated)
                elif(user == 6):
                    exit()
                elif(user<1 or user>6):
                    print("invalid input!! Please enter the integer from 1-5 ")
            break
        else:
            atempt = attempt - 1
            print("Incorrect pin."+str(attempt)+" is left!")
        
            
main()

