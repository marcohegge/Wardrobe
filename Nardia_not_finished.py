import random

class Wardrobe:
    def __init__(self, name, material, status_door, position, broke):
        self.name = name
        self.material = material
        self.status_door = status_door
        self.position = position
        self.broke = broke

    def open(self):
        '''
        function to open the door when it is closed
        '''
        if self.status_door == "close":
            print('The door of the wardrobe goes open')
            self.status_door = "open"
        else:
            print('The door is already open')
        return self.status_door

    def close(self):
        '''
        function to close the door if it is Open
        '''
        if self.status_door == 'open':
            print('The door of the wardrobe closes')
            self.status_door = 'close'
        else:
            print('The door of the wardrobe was already close')
        return self.status_door

    def get_in(self):
        '''
        function to get in when de door is Open
        '''
        if self.position == 'out' and self.status_door == 'open':
            print('Get into the wardrobe')
            self.position = 'into'
        else:
            print('Youre are already in the wardrobe or the door is close')
        return self.position

    def get_out(self):
        '''
        function to get out, if you are in and the door is Open
        '''
        if self.position == 'into' and self.status_door == 'open':
            print('Get out the wardrobe')
            self.position = 'out'
        else:
            print('You are not in the wardrobe or the door is close')
        return self.position

    def kick(self):
        ''' kick the wardrobe; if glass dan broke and else still good'''
        if self.material == 'glass':
            print('De Wardrobe is broke')
            self.broke == True
        elif self.material == 'wood' or self.material == 'carbon':
            print('De wardrobe is still good')
            self.broke == False
        else:
            print('Material is not wood, caron or glass')
        return self.broke

    def __str__(self):
        return self.name+ ' ' + self.material + ' ' + self.status_door + ' ' + self.position + ' ' + str(self.broke)


class Lion:
    '''
    Speak to the Lion after winning the battle with the witch
    '''
    def __init__(self, visit):          #can be use in the future to visit the Lion more times
        self.visit = visit

    Print('Hello I am the Lion of Nardia and you won!')

class Witch:
    '''
    If you are in Nardia you have to battle with the witch
    '''
    def __init__(self, times_narnia, fight):
        self.times_narnia = times_narnia
        self.figth = fight

    def battle(slef, times_narnia):
        chance = random.randint(1,(100/self.times_narnia + 1))        #amount of times been in Nardia improved your chance to winn

        if chance == 1:            #if random = 1 then win battle form Witch
            print('You won the battle of the witch')
            self.figtht = True
        else:
            print('The Witch won')
            self.figth = False
        return self.fight

# Kast staat in Londen
# Programma loopt net zo lang tot je de leeuw hebt ontmoet
# 1: kickt tegen de kast
# 2: open de kast
# 3: Stap erin kans 1 op 100 in narnia (random generator)
# 4: Als je in narnia bent dan witch verslaan: kans dat dat lukt is gebaseerd op het aantal x in Narnia; 1e x 1 op 100 and  2e x 2 op 100
# 5: versla je heks praten met de leeuw - einde Programm
# 6: niet verslagen weer buiten de kast in de londen opnieuw starten (edited)

#Needed for de amount of visit in Nardia
narnia = 1
wardrobe1 = Wardrobe(name='billy', material='wood', status_door='close', position = 'out', broke = False)
while:
    wardrobe1.kick()
    if wadrobe1.broke = False:    #Check if the wardrobe is broken  --> hast to be improved
        wardrobe.open()

        if wardrobe1.status_door == 'open':       #Check if the door is open
            wardrobe1.get_in()

            if wardrobe1.posintion == 'into':
                chance = random.randint(1,101)        #generate a random number between 1 and 100

                    if chance == 50:                  #if number is 50 then you are in Nardia
                        Witch.battle(narnia)
                        narnia =+ 1

                        if Witch.figth == True:
                            Lion()                     #the Lion speaks to you
                            break                      #leave the while loop

    else:   #wardrobe is broke, ceate a new wardrobe
        wardrobe1 = Wardrobe(name='billy', material='wood', status_door='close', position = 'out', broke = False)
