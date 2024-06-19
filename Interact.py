from ascii_magic import AsciiArt

from Inventory import Inventory
from map import Map


class Interact():
    def __init__(self, rooms_clues):
        self.rooms_clues = rooms_clues
        self.inv = Inventory()
        self.map = Map()
        self.my_art = AsciiArt.from_image('easter egg.png')
        self.output = self.my_art.to_ascii(columns=70)
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
            
            "Weapon Rack":{
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
                "Response":"<>Whispers>This will come in handy."
            },
            
            
                
        }
        
        self.suspects = {
            "Turk Barrett": {
                "location": "Warehouse",
                "description": "A low-level informant with a history of petty crimes.",
                "evidence": "Documents detailing an illegal shipment.",
                "dialogue": [
                    "Daredevil: Where were you last night, Turk?",
                    "Turk Barrett: I ain't know nothin' man. I was just here, minding"+
                    "my own business.",
                    "Daredevil: We've got documents that say otherwise, Turk."+
                    "Start talking.",
                    "Turk Barrett: Okay, okay! I might have seen something, "+
                    "but I ain't no snitch!**gives Documents**"
                    
                ]
            },

            "ThugA": {
                "location": "Smuggler's Den",
                "description": "A nervous thug, likely low on the criminal hierarchy.",
                "evidence": "A smuggled weapon found at the scene.",
                "dialogue": [
                    "Daredevil: Who are you working for?",
                    "ThugA: (nervous) I... I ain't sayin' nothin'.",
                    "Daredevil: We know you're not the mastermind. Give us a name.",
                    "ThugA: You don't get it, man. If I talk, I'm dead!",
                    "Daredevil beats the thug unconscious."
                ]
            },

            "ThugB": {
                "location": "Smuggler's Den",
                "description": "A stubborn thug with a tough exterior.",
                "evidence": "A key to a hidden stash.",
                "dialogue": [
                    "Daredevil: You were seen at the scene. What do you have to say?",
                    "ThugB: I ain't no snitch. Do your worst.",
                    "Daredevil: We'll see how long you can hold out.",
                    "ThugB: (sighs) Fine, but you didn't hear it from me."
                ]
            },

            "Carl Hoffman": {
                "location": "Torture Chamber",
                "description": "A hardened criminal with ties to the Kingpin.",
                "evidence": "A note with the Kingpin's name.",
                "dialogue": [
                    "Daredevil: Tell me about the Kingpin.",
                    "Carl Hoffman: You think I'm scared of you? You don't know who you're dealing with.",
                    "Daredevil: We have ways of making you talk, Hoffman.",
                    "Carl Hoffman: Alright, alright! The Kingpin's name is Fisk. Wilson Fisk."
                ]
            },

            "Guard": {
                "location": "Guard Room",
                "description": "A corrupt guard who knows the prison's inner workings.",
                "evidence": "Security protocol documents.",
                "dialogue": [
                    "Daredevil: What do you have on the incoming and outgoing prsioners?",
                    "Guard: I can't tell you that. I'll lose my job.",
                    "Daredevil: Your job is the least of your worries right now. Start "+
                    "talking.",
                    "Guard: Fine, heres a document with all that info. That's all"+
                    "I know!"
                ]
            },

            "Warden": {
                "location": "Warden's Office",
                "description": "The authoritative figure in the prison, with hidden"+
                "secrets.",
                "evidence": "A ledger of illegal transactions.",
                "dialogue": [
                    "Daredevil: We know you're hiding something.",
                    "Warden: You have no authority here. Leave my office immediately.",
                    "Daredevil: This can go one of two ways. Cooperate, or face the "+
                    "consequences.",
                    "Warden: Alright, alright! There's a ledger hidden in my desk. "+
                    "It has all the dirty deals."
                ]
            },

            "Prisoner": {
                "location": "Cafeteria",
                "description": "A prisoner with loose lips and a fear of solitary.",
                "evidence": "A map of the prison with escape routes marked.",
                "dialogue": [
                    "Daredevil: What do you know about the recent breakout?",
                    "Prisoner: I heard some things, but I ain't involved. Promise.",
                    "Daredevil: If you want to stay out of solitary, you better start"+
                    "talking. Who's the new guy in solitary?",
                    "Prisoner: Okay, okay! They call him the punisher.They drew his"+ 
                    "sign over there"+
                    "**points to the Mysterious Logo**"
                ]
            }

           
        }
    def examine_clues(self, item_name, current_location):
        """
        Allows the player to examine items/clues
        """
        if item_name in self.evidence_items[item_name]['location'] == current_location:
            return self.evidence_items[item_name]['description']
        else:
            return f"The item {item_name} is not present in the current location"

    def pick_up_item(self, item_name, current_location):
        """
        Allows players to pick up items
        """
        if item_name in self.evidence_items[item_name]['location'] == current_location:
            self.inv.add_item(item_name)
        else:
            return f"The item {item_name} is not present in the current location"
        
        
    
        
            


        


 