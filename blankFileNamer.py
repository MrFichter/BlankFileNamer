##The purpose of this program is to create blank files,
##name them for each student,
##and then (optionally) place them in each student's network folder.

### = Something temporary that I'm working on.



##MENU / QUESTIONS


import os ##Lets me check or change the destinationDir.


def askYesNo(question):
    """Ask a yes or no question."""
    ## Created by: Mike Dawson.
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response


##print overview

print '''
Welcome to this file-creating program!
The files you create will start with
a base name (e.g. FractionsProject)
and will be followed by a student's
user name (e.g. FichterJ) and the file
type (e.g. doc, pdf, or mp3).
'''
print '''
If you had a student FichterJ and
another student SmithT, this program
could automatically create
FractionsProjectFichterJ.doc and
FractionsProjectSmithT.doc.
'''


##Ask for fileBaseName
print '''
To get started, please provide the
base name for your file. This should
be all one word, and should use only
letters and numbers. An example would be
"FractionsProject."
'''
fileBaseName = str(raw_input('base name>'))


##Ask for fileType
print '''
Now, please provide a file type, leaving
off the period. Examples:
doc
pdf
mp3
'''
fileType = str(raw_input('file type>'))


##Ask for text file with list of usernames.
print '''
Now, please create a text file (you can
do this with the Notepad program on your
computer) in which each line provides the
username of a student from whom you'd like
to create a copy of the file. A sample text
file might look like this:
FichterJ
SmithT
MouseM
'''
print'''
Now, please enter the name of the text
file you created. Example: usernames.txt
'''
textFileName = str(raw_input('text file name>'))


##Ask for location of this text file.
print'''
Now, please specify where on the computer
the text file is saved. Make sure to use
forward slashes (not back slashes) and to
include a forward slash as the final
character you type. Example:
C:/Users/Jonathan/MathProjects/
'''
textFilePath = str(raw_input('text file location>'))


##Concatenate textFileName and textFilePath to get the information the program needs to open the text file.
textFile = (textFilePath + textFileName)                


##Ask about destination file path.
print '''
It is now time to decide the
destination (i.e. the place on your
computer you would like to store the
new files you are creating). The default
destination is the following:
'''
print (os.getcwd())
print '''
You can keep this
destination, or you can specify a new one.
(N.B. If you want to place copies into
each student's network folder, you'll
probably want to specify a new destination.)
'''
keepDestination = askYesNo ('Would you like keep the current destination? y / n>')
if keepDestination == 'n': ##i.e. If the user wants to specify a custom destination
    print '''Please specify your
    desired destination. Make sure to use
    forward slashes (not back slashes) and to
    include a forward slash as the final
    character you type. Example:
    C:/Users/Jonathan/Desktop/
>'''
    destinationDir = str(raw_input('destination>'))
    os.chdir(destinationDir)

##Ask if program should also distribute copies of the file into folders named after the username.
folderDistribute = askYesNo ('Would you like to place copies into each student\'s network folder?')
### if folderDistribute == 'y' ###Work on this later.                


##CREATING THE FILES AND, OPTIONALLY, DISTRIBUTING THEM TO FOLDERS

#Loop through text file of usernames, turning each into a file.

for line in open(textFile):
    ##Create full file name
    fileNameFull = (fileBaseName + line.strip() + '.' + fileType)##Strip method gets rid of \n at the end of each line.
    open (fileNameFull , 'w')

    ##Opening a file in write mode automatically creates the file if it does not yet exist.
    ##Python will close the file when the script ends.
    ##The full file name is the file's base name (e.g. "Fractions project") plus the user name followed by the file type. E.g. "FractionsProjectFichterJ.py"





##FOR TESTING PURPOSES


##To check the path:
##import os
##os.getcwd()

##Also try os.chdir()
    
