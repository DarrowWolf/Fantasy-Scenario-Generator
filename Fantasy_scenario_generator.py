import random
import os

species = ["Wolf", "Fox", "Cat", "Dog", "Bear", "Eagle", "Snake", "Rabbit", "Deer", "Owl", "Rat", "Squirrel", "Lizard", "Hyena", "Coyote", "Boar", "Horse", "Leopard", "Lion", "Mouse", "Badger", "Hawk", "Ferret", "Lynx", "Otter", "Skunk", "Gazelle", "Kangaroo", "Monkey", "Armadillo", "Dragon", "Griffon", "Gryphon"]
scenarios = ["Leading an army of mythical creatures into battle",
"Discovering a powerful artifact and defending it from those who would take it for themselves",
"Traveling through enchanted forests and over dangerous mountain passes to reach a distant land",
"Navigating a world filled with danger and intrigue, where every ally could be a potential enemy",
"Participating in ritualistic magic to unlock hidden powers and abilities",
"Uncovering the truth behind a mysterious curse that has befallen a kingdom",
"Stealing forbidden knowledge from a powerful mage or sorcerer",
"Battling rival factions in order to gain control of a powerful magical artifact",
"Exploring ancient ruins and tombs in search of powerful magical artifacts",
"Being forced to choose between loyalty to one's kingdom and loyalty to one's friends and allies",
"Wearing elaborate armor and carrying a magic sword",
"Wielding a powerful magical staff or wand",
"Engaged in hand-to-hand combat with an enemy warrior",
"Wearing flowing robes and carrying a small, hidden dagger",
"Searching for hidden treasures in ancient ruins",
"Riding a fearsome beast into battle", 
"Training with a master swordsman or sorcerer",
"Using stealth and agility to navigate dangerous territory",
"Protecting a village or kingdom from invasion or attack",
"Engaged in a duel with a rival swordsman or sorcerer",
"Exploring dark and dangerous caves or forests",
"Summoning elemental forces to do their bidding",
"Protecting a valuable artifact or enchanted object",
"Traveling through portals to other dimensions or realms",
"Participating in large-scale battles and sieges",
"Quest to find a missing prince or princess",
"Journey to the underworld to retrieve a stolen soul",
"Mission to recover a powerful magical artifact from a dangerous dragon",
"Attempt to overthrow a tyrannical king or queen",
"Battle to stop a powerful necromancer from raising an army of the dead",
"Search for a cure for a mysterious disease that is plaguing the land",
"Rescue mission to save a captive friend or loved one",
"Investigation into strange and unexplained supernatural events",
"Confrontation with a powerful and ancient evil entity",
"Race against time to prevent the unleashing of a powerful and destructive force",
"Pilgrimage to a holy site to seek enlightenment or receive a prophecy",
"Journey to a far-off land to find a lost city of legend",
"Confrontation with a rival group of adventurers seeking the same goal",
"Journey through a magical and dangerous maze to reach a hidden treasure",
"Battle to protect a kingdom from an invading army of orcs or other monstrous creatures",
"Journey to the edge of the world to find a rare and powerful ingredient for a magical ritual",
"Protecting a sacred temple from raiders seeking its ancient relics",
"Embarking on a perilous journey through a treacherous swamp filled with dangerous creatures and magic",
"Rescuing a captive prince from a powerful sorceress's castle",
"Undertaking a quest to find the fabled Sword of the Gods, a weapon said to possess immense power",
"Battling a rival kingdom for control of a valuable resource, such as a magical spring or enchanted forest",
"Fighting against a cult that seeks to bring about the end of the world through the use of dark magic",
"Confronting a powerful demon or evil spirit that is causing destruction and chaos in the land",
"Journey to a mysterious island to find the source of a strange and powerful magic",
"Infiltrating a secret society of wizards to uncover their plans and stop their evil schemes",
"Defending a city against a horde of invading monsters",
"Escaping from a haunted and cursed castle, filled with ghosts and other supernatural beings",
"Sneaking into a powerful wizard's tower to steal a valuable spell book",
"Pursuing a thief who has stolen a powerful magical artifact",
"Battling a powerful witch who is terrorizing a village and practicing dark magic",
"Discovering the truth behind a mysterious prophecy and fulfilling its destiny",
"Navigating treacherous political waters, balancing loyalty to one's own kingdom and alliances with others",
"Journey to the depths of the underworld to retrieve a powerful artifact from the grasp of the dead"]

def generate_sentence(species, scenarios):
  chosen_species = random.choice(species)

  if not scenarios:
    return None

  chosen_scenarios = random.choice(scenarios)
  scenarios.remove(chosen_scenarios)

  sentence = "A " + chosen_species + " " + chosen_scenarios + "."
  
  return sentence

i = 0
while True:
  filename = "generated_sentences_" + str(i) + ".txt"
  if not os.path.exists(filename):
    break
  i += 1

with open(filename, "w") as file:
  while True:
    sentence = generate_sentence(species, scenarios)
    if sentence is None:
      break
    file.write(sentence + "\n")
