import random as rand

# =============================================================================
# STAT BLOCK
# =============================================================================
name = "Otto Hildebrand"
HP = 50
AC = 20
mods = {"STR": 4, "DEX": 2, "CON": 2, "INT": 1, "WIS": 3, "CHA": -2}
weapon = {"atk": 9, "dmg": 10, "critMult": 3, "critRange": 20}
sacredWeapon = {"Uses": 5, "Merciful":False, "Defensive":False, "Flaming":False, "Frost":False, "Keen":False}
fervor = {"Uses": 5, "Divine":False, "Bull":False, "Bear": False, "Sanctuary":False, "Shield of Faith":False}

# =============================================================================
# FUNCTIONS
# =============================================================================
# Rolling to attack
def attackRoll(weapon, fervor, sacredWeapon):
    crit = False
    roll = rand.randint(1, 20)
    nat = roll
    
    # Crit checks
    if sacredWeapon["Keen"] == True:
        if roll >= 19:
            crit = True
    elif roll == 20:
        crit = True
        
    # Did we use fervor at all?
    if fervor["Divine"] == True:
        roll += 2
    if fervor["Bull"] == True:
        roll += 2
    
    # Adding our attack modified
    roll += weapon["atk"]
    atkRoll = [roll, crit, nat]
    return atkRoll

# Rolling for damage
def damageRoll(mods, weapon, crit, fervor, sacredWeapon):
    # Rolling for raw damage
    dmg = rand.randint(1, weapon["dmg"]) + mods["STR"]
    print("Raw Damage:", dmg)
    
    # Adding any possible fervor damage modifiers
    if fervor["Divine"] == True:
        dmg += 2
        print("Divine Favor:", str(2))
    if fervor["Bull"] == True:
        dmg += 2
        print("Bull's Strength:", str(2))
     
    # Checking for crit
    if crit == True:
         dmg *= weapon["critMult"]
        
    dmgTotal = dmg
    
    # Adding any possible additional damage dice from Sacred Weapon
    if sacredWeapon["Merciful"] == True:
        mercifulDmg = rand.randint(1, 6)
        print("Merciful: ", mercifulDmg)
        dmgTotal += mercifulDmg
    if sacredWeapon["Flaming"] == True:
        flamingDmg= rand.randint(1, 6)
        print("Flaming: ", flamingDmg)
        dmgTotal += flamingDmg
    if sacredWeapon["Frost"] == True:
        frostDmg= rand.randint(1, 6)
        dmgTotal += frostDmg
        print("Frost: ", frostDmg)
        
    return dmgTotal

# Going through your turn
def myTurn(mods, weapon, fervor, sacredWeapon):
    print("It's your turn!")
    swiftAction = True
    
    # Attack Roll
    atkAns = input("Would you like to attack? ")
    if atkAns == "Y":
        # Checks if we would like to use Keen
        if sacredWeapon["Uses"] != 0:
            keen = input("Would you like to use keen? ")
            if keen == "Y":
                sacredWeapon["Keen"] = True
                sacredWeapon["Uses"] -= 1
                swiftAction = False
        
        # Seeing if we want to use fervor
        if swiftAction == True:
            if fervor["Uses"] != 0:
                fervAns = input("Would you like to use Fervor? ")
                if fervAns == "Y":
                    tryFerv = True
                    while tryFerv == True:
                        divine = input("Divine Favor? ")
                        if (divine == "Y"): 
                            fervor["Divine"] = True
                            fervor["Uses"] -= 1
                            swiftAction = False
                            tryFerv = False
                        
                        if tryFerv == True:
                            bull = input("Bull's Strength? ")
                            if (bull == "Y"):
                                fervor["Bull"] = True
                                fervor["Uses"] -= 1
                                swiftAction = False
                                tryFerv = False
                       
                        #Breaks if the user decided against it.
                        tryFerv = False
       
        # Okay, let's actually go for the attack roll now.
        critFail = False
        if atkAns == "Y":
            atkRoll = attackRoll(weapon, fervor, sacredWeapon)
            if atkRoll[1] == True:
                print("A critical success!")
                crit = True
            elif atkRoll[2] == 1:
                print("A critical failure!")
                critFail = True
            else:
                crit = False
            print("Your attack roll:", atkRoll[0], "Nat:", atkRoll[2])
    
        
        # Damage Roll
        if critFail != True:
            dmgAns = input("Did you hit? ")
            if dmgAns == "Y":
                while swiftAction == True:
                    if sacredWeapon["Uses"] != 0:
                        sacrAns = input("Would you like to use Sacred Weapon? ")
                        if sacrAns == "Y":
                            
                            merciful = input("Merciful? ")
                            if merciful == "Y":
                                sacredWeapon["Merciful"] = True
                                sacredWeapon["Uses"] -= 1
                                swiftAction = False
                            if swiftAction == True:
                                flaming = input("Flaming? ")
                                if flaming == "Y":
                                    sacredWeapon["Flaming"] = True
                                    sacredWeapon["Uses"] -= 1
                                    swiftAction = False
                            if swiftAction == True:
                                frost = input("Frost? ")
                                if frost == "Y":
                                    sacredWeapon["Frost"] = True
                                    sacredWeapon["Uses"] -= 1
                                    swiftAction = False
                        else:
                            swiftAction = False
                    else:
                        swiftAction = False
                dmg = damageRoll(mods, weapon, crit, fervor, sacredWeapon)
                print("Total Damage:", dmg)
    results = [fervor["Uses"], sacredWeapon["Uses"]]
    return results


def main(HP, mods, weapon, fervor, sacredWeapon):
    battle = True
    turn = 1
    while battle == True:
        askTurn = input("Is it your turn? ")
        if askTurn == "Y":
            print("=========================================")
            print("Turn", turn, "HP:", HP)
            print("=========================================")
            
            results = myTurn(mods, weapon, fervor, sacredWeapon)
            
            #Resetting everything but the uses of Fervor and Sacred Weapon
            sacredWeapon = {"Uses": results[1], "Merciful":False, "Defensive":False, "Flaming":False, "Frost":False, "Keen":False}
            fervor = {"Uses": results[0], "Divine":False, "Bull":False, "Bear": False, "Sanctuary":False, "Shield of Faith":False}
            turn += 1
            print("=========================================")
            print("END OF YOUR TURN")
            print("=========================================", end="")
        # Did we take damage?
        try:
            healthDamage = int(input("How much damage did you take this turn? "))
            HP -= healthDamage
            print("Total HP:", HP)
        except:
            print("Total HP:", HP)
            
# =============================================================================
# ... FIGHT!
# =============================================================================
main(HP, mods, weapon, fervor, sacredWeapon)
    
            
    
    

    
    
