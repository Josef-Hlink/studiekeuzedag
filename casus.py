#-------------------------------------------------------------------------#
# Een variabele is een stukje geheugen waar je informatie in kan opslaan

# Dit kan een getal zijn
heel_getal = 10
decimaal_getal = 3.14
#print('Heel getal:', heel_getal)
#print('Decimaal getal:', decimaal_getal)


# Dit kan een letter of woord zijn
letter = 'f'
woord = 'studiekeuzedag'
#print('Letter:', letter)
#print('Woord:', woord)


# Dit kan ook een lijst zijn, met letters, woorden of nog veel meer
een_variabele = '010110'
lijst = [1, '2', 3.14, 'hoi', een_variabele]
#print('Lijst:', lijst)
#-------------------------------------------------------------------------#
# Behalve gewoon printen kan je met deze variabelen ook dingen doen

# Je kunt rekenen
twee: int = 2
drie: int = 3
som: int = twee + drie
#print('2+3 =', som)


# Je kunt woorden aanpassen
stad_waarin_ik_woon: str = 'Leiden'
feit: str = stad_waarin_ik_woon + ' is de leukste stad in Nederland.'
#print(feit)


# Je kunt elementen uit een lijst aanpassen
originele_lijst: list = [1, 2, 3, 4, 9, 6, 1]
# "indexen" gaat zo:     0  1  2  3  4  5  6 

aangepaste_lijst: list = originele_lijst.copy() # kopieer de lijst
aangepaste_lijst[4] = 5 # zet het vierde element op 5

#print('Origineel:', originele_lijst)
#print('Aangepast:', aangepaste_lijst)

# Wat moeten we intypen om de lijst helemaal oplopend te maken en daarna
# te printen in de Shell?




#-------------------------------------------------------------------------#
# Maar het allerleukste van programmeren is toch wel zogeheten "operators"

# Als eerste de if-statement
leeftijd: int = 17
if leeftijd >= 18:
    #print('Je mag eindelijk je eigen drank kopen!')
    ...
else:
    #print('Nog even wachten...')
    ...
    

# En de for-loop
kleine_lijst_met_nummers: list = [0, 1, 2, 8]
for nummer in kleine_lijst_met_nummers:
    #print(nummer)
    ...


# En nu samen
langere_lijst_met_nummers: list = [1, 2, 3, 8, 6, 4, 5, 9]
# Wat moeten we intypen als we uit deze lijst alleen de nummers willen
# printen die groter zijn dan 4?






#-------------------------------------------------------------------------#
