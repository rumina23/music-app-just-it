#Importing MySQL Connector
#Command: pip3 install mysql-connector-python
#import connector
import mysql.connector

# Making Connection to MySQL
conn = mysql.connector.connect(host="localhost", user="root", passwd="sofia177", database="music_database")
if(conn):
  print('Connection Successful!')
else:
  print('Connection Failed!')

mycursor = conn.cursor()

#Function for the Menu
print('!Welcome to Our Music App!')
def mainMenu():
  # Displaying Menu
  print('\n\n\n!_______________________________!')
  print('1: View All Songs') #Done
  print('2: Add New Song')   #Done
  print('3: Delete a Song')  #Done
  print('4: Search a Song')
  print('5: Update a Song')
  print('6: Close the Program')
  print('!_______________________________!')

  # Taking input from the user using the input keyword.
  userInput = input('Enter Choice:')

  # return userInput
  return userInput

#Function to Insert Data
def insertData():

  print('!Enter Details of the Song/Music!')
  print('!________________________________!')

  name = input('Enter Song Name: ')
  composer = input('Enter Song Composer: ')
  released_in = input('Enter the Releasing Year: ')
  #Inserting into MySQL
  query = "INSERT INTO songs_list(song_name, composer, release_year) VALUES(%s, %s, %s);"
  data = tuple(( name, composer, released_in))
  print(data)
  mycursor.execute(query, data) #INserting Data
  print('Song Inserted Successfully!')

  conn.commit()
  mainMenu()  #Calling Main Menu Function

def listData():
  print('Here is the list of all songs.')
  #Reading/Fetching Data from MySQL
  query = "SELECT * FROM songs_list"
  mycursor.execute(query) #Executing Query
  songs = mycursor.fetchall() #fetching from the table
  conn.commit()
  print('!_____________________________________________!')
  print('ID | Title    | Composer    | Release Year')
  for row in songs:
    print(f'{row[0]} | {row[1]}    | {row[2]}    | {row[3]}')
  mainMenu()  #Calling Main Menu Function

def deleteData():
  #Calling function to display the list of songs.
  listData()  #Function Call
  # Deleting Data
  choice = input('\n\nEnter the ID of the song you want to delete:')

  #Deleting Song.
  query = f"DELETE FROM songs_list WHERE id = {choice}"
  mycursor.execute(query)   #Executing Query.
  conn.commit()
  print('Song has been deleted Successfully!')
  mainMenu()  #Calling Main Menu Function

def searchData():
  choice = input('Enter Name of the Song:') #Accept Data.
  query = f"SELECT * FROM songs_list WHERE song_name LIKE '%{choice}'"
  
  data = mycursor.execute(query) #Executing Query
  song = mycursor.fetchone()
  conn.commit()
  if(song):
    print('Song Exists, here are the details')
    print(f'Name: {song[1]}, Composer: {song[2]}, release Year: {song[3]}')
  else:
    print('Does not exist')
  # Displaying Main Menu
  mainMenu()  #Calling Main Menu Function

def updateData():
  listData()   #Calling Function.
  choice = input('\nEnter the Song ID you want to update:')
  print('\n\nEnter the details you want to update with!')

  # Asking Details from the User.
  title = input('Enter New Title: ')
  composer = input('Enter New Composer: ')
  release_year = input('Enter Release Year: ')

  # Code for Inserting Data to DB
  query = f"UPDATE songs_list set song_name = %s, composer = %s, release_year = %s WHERE id = {choice}"
  data = tuple(( title, composer, release_year))
  print(data)
  mycursor.execute(query, data) #Inserting Data
  print('Song Updated Successfully!')
  conn.commit()
  mainMenu()  #Calling Main Menu Function

data = mainMenu()
# typecasting of data
if int(data) == 1:     #If user Enters 1.
  listData() #Function Call...
elif int(data) == 2:
  insertData()  #calling the insertData function.
elif int(data) == 3:   #if User Enters 3.
  deleteData()
elif int(data) == 4:   #if user Enters 4.
  searchData()
elif int(data) == 5:  
  updateData()
elif int(data) == 6:
  print('Program will get terminated Now!')
else:
  print('Invalid Entry')
