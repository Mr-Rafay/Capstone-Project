from ascii_magic import AsciiArt, from_image

from Inventory import Inventory
from map import DetailedMap, Map


class Interact():
    def __init__(self, rooms_clues):
        self.rooms_clues = rooms_clues
        self.inv = Inventory()
        self.map = Map()
        #self.my_art = AsciiArt.from_image('easter egg.png')Will use it
        #self.output = self.my_art.to_ascii(columns=70)
        self.evidence_items = {
            "Guns": {
                "location": "Shipping Bay",
                "description": "By how it feels, there is AK-47, Glock and an M4A1."+
                "Some serious firepower",
                "Response": "What is the Kingpin trying to bring to the streets?"+
                "Especially with this firepower.",
            },
            "Cargo Logs":{
                "location": "Shipping Bay",
                "description": "Detailed logs of all shipments passing through" +
                "the docks",
                "Response": "Whatever this file reads will be useful to Foggy"
            },
            "Weapn Rack":{
                "location": "Weapon Storage",
                "description":"An empty weapon rack.",
                "Response": "I am late, the weapons are already in use."
            
            },
            "Recorded Audio of Meeting":{
            "location": "Surveillance Room",
            "description":"An audio of a meeting is playing: "+
                "'Business as usual. Look I provide you guns you show me the money"+
                " that seems a good deal to me.' Another voice goes 'Yes Mr.Turk it is" 
                " but this time I can't, you see cash is short and we as an upcoming" +
                " gang need to do something quick and get the atten' (gunshots)."+
                " Turk: Clean the bodies, I don't want the boss to know this."
                + "<end audio>",
            
            "Response": "Huh..Looks like who ever is new to gangs ain't know "+
                "how to be tough, these gang members need to pay."
            },
            "Security Protocols":{
                "location": "Guard Room",
                "description":"A guard gives you documents of the various past " 
                + "protocols.",
                "Response":"<>Whispers>This will come in handy"
            },
            "Mysterious Logo":{
               "location": "Prison",
                "description": "",#Use the picture here
                "Response": "What type of logo is this", #Make a better response
            }
            
            
            
            
        }
        
        
        


    
    
