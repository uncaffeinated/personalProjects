import combat
# =============================================================================
# AutoOtto: Tool for the use of playing Otto Hildebrand in Pathfinder
# =============================================================================
name = "Otto Hildebrand"
HP = 50
AC = 20
mods = {"STR": 4, "DEX": 2, "CON": 2, "INT": 1, "WIS": 3, "CHA": -2}
weapon = {"atk": 9, "dmg": 10, "critMult": 3, "critRange": 20}
sacredWeapon = {"Uses": 5, "Merciful":False, "Defensive":False, "Flaming":False, "Frost":False, "Keen":False}
fervor = {"Uses": 5, "Divine":False, "Bull":False, "Bear": False, "Sanctuary":False, "Shield of Faith":False}

# =============================================================================
# Non-Combat Functions            
# =============================================================================
def main(HP, AC, mods, weapons, fervor, sacredWeapon):
    inGame = True
    while inGame:
        combAns = input("Are you in combat? ")
        if combAns == "Y":
            combat.combat(HP, mods, weapon, fervor, sacredWeapon)
        
                
main(HP, AC, mods, weapon, fervor, sacredWeapon)