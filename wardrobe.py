class Wardrobe:
    def __init__(self, name, material, status_door, position, broke):
        self.name = name
        self.material = material
        self.status_door = status_door
        self.position = position
        self.broke = broke

    # Programma loopt net zo lang tot je de leeuw hebt ontmoet
    # londen
    # kickt tegen de kast
    # open de kast
    # stap erin kans 1 op 100 in narnia
    # als je in narnia bent dan witch verslaan: kans dat dat lukt is gebaseerd op het aantal x in Narnia
    # 1e x 1 op 100
    # 2e x 2 op 100

    #versla je heks praten met de leeuw - einde Programm
    #niet verslagen weer buiten de kast in de londen opnieuw starten (edited)

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

wardrobe1 = Wardrobe(name='billy', material='wood', status_door='open', position = 'into', broke = False)
print(wardrobe1)
wardrobe1.close()
print(wardrobe1)
