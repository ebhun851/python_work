'''
Created on Sep 16, 2017

@author: NIS1526-mbp
'''
def printPersons(list):
    for person in list:
        print ("| name={0} || age={1} || salary={2} |".format(person[0],person[1],person[2]))
        
                
persons = [['jag','2','10'],['khaju','20','100'],['eswar','30','1000']]

printPersons(persons);
    