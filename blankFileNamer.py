##The purpose of this program is to create blank files,
##name them for each student,
##and then place them in each student's network folder.


##MENU / QUESTIONS

##Ask for fileBaseName
## Note: Dawnson has functions for number question and yes / no question.

##Ask for fileType

##Ask for text with with list of usernames.
##(Tell user that usernames will be used to name each copy of the file.)

##Ask if program should also distribute copies of the file into folders named after the username.
##(If this is the case, the program should ask for the dirBaseline.)




##CREATING THE FILES AND, OPTIONALLY, DISTRIBUTING THEM TO FOLDERS

#Loop through text file of usernames, turning each into a file.

for line in open('textFile'):
    open (%s , 'w') % (fileBaseName + '.' + fileType)
    ##Opening a file in write mode automatically creates the file if it does not yet exist.
    ##Python will close the file when the script ends.
    ##The full file name is the file's base name (e.g. "Fractions project") plus the user name followed by the file type. E.g. "FractionsProjectFichterJ.py"
    
    
