#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# COsuji, 2022-Aug-14, Restructured script by adding functions for data addition and deletion
# COsuji, 2022-Aug-14, Restructured script by adding functions for writing to file and other functionalities
# COsuji, 2022-Aug-28, Restructured script to use list of objects instead of list of dictionaries
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd__iD: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:    
        def __init__(self, iD, title, artist) --> None
        def ID(self) --> self.__iD
        def ID(self, iD) --> None
        def title(self) --> self.__title
        def title(self, title) --> None
        def artist(self) --> self.__artist
        def artist(self, artist) --> None
        process_adding_data(iD, title, artist, table)  --> None
        process_deleting_data(table) --> None

    """
    def __init__(self, iD, title, artist):
        self.__iD = iD
        self.__title = title
        self.__artist = artist
        
    
    @property
    def ID(self):
        return self.__iD
    
    @ID.setter
    def ID(self, iD):
        self.__iD = iD
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, artist):
        self.__artist = artist
        
        
    def process_adding_data(iD, title, artist, table):
        
        """Function to mandaging the addition of Cd Objects to list
        
        Args:
            iD (int): CD ID entry
            title (string): CD title entry
            artist (string): CD arist name entry
            
        Returns: 
            None.
        """
        for row in table:
            print(row.__iD)
        cD = CD(iD, title, artist)
        table.append(cD)
        
    @staticmethod    
    def process_deleting_data(table):
        """Function to manage data deletion to table

        delets data entries based on user ID number data from 2D table (list of objects)

        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
        Returns:
            None.
        """
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except:
            print("Please enter a number as the inventory ID")
         
        else:
            intRowNr = -1
            blnCDRemoved = False
            for row in table:
                intRowNr += 1
                if row.__iD == intIDDel:
                    del table[intRowNr]
                    blnCDRemoved = True
                    break
            if blnCDRemoved:
                print('The CD was removed')
            else:
                print('Could not find this CD!')
        
            

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects
     
        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one dictionary row in table.
     
        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
     
        Returns:
            loaded_obj (list of objects): 2D data structure (list of objects) loaded from file
            
        """
        loaded_obj = []
        
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                obj = CD(int(data[0]),data[1],data[2])
               
                loaded_obj.append(obj)
            
        except:
            print("An error occured while attempting t read file")
            
        else:
            objFile.close()
        
        return loaded_obj
    @staticmethod
    def save_inventory(file_name, table):
        """Function to manage data emisson from a list of objects to a file
    
        Reads the data from a 2D table (list of objects) to a file identified by file_name 
    
        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
        Returns:
            None.
        """
        
        objFile = open(file_name, 'w')
        for row in table:
            objFile.write(str(row._CD__iD) + "," + row._CD__title + "," + row._CD__artist + '\n')
        objFile.close()
     
    
    
    
    
    
    
    


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
   

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
            
        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t {} (by:{})'.format(row._CD__iD ,row._CD__title, row._CD__artist ))
        print('======================================')
        
    @staticmethod
    def add_inventory(table):
        """Requests user data input for data entry


        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
            
        Returns:
            None.

        """
        strID = input('Enter ID: ').strip()

        try:
            iD = int(strID)
        except:
            print("Please enter a valid number")
            return
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        
        
        CD.process_adding_data(iD, strTitle, strArtist,table)
    
   
    
    
    

        

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

lstOfCDObjects.extend(FileIO.load_inventory(strFileName))
IO.show_inventory(lstOfCDObjects)

while True:
    
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break 
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects.clear()
            lstOfCDObjects.extend(FileIO.load_inventory(strFileName))
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
          # Ask user for new ID, CD Title and Artist
         
        IO.add_inventory(lstOfCDObjects)
         
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
      # process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
      # process delete a CD
    elif strChoice == 'd':
          # get Userinput for which CD to delete
          # display Inventory to user
        IO.show_inventory(lstOfCDObjects)
          # ask user which ID to remove
         
             
          # search thru table and delete CD
        
        CD.process_deleting_data(lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
      # process save inventory to file
    elif strChoice == 's':
          # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
         # Process choice
        if strYesNo == 'y':
               # save data
           
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        # continue  # start loop back at top.
      # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




