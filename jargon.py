'''
Created on Jul 30, 2014

@author: thor
'''
import csv
import sys

jargonCsv = 'jargon.csv'

def read_csv(path):
    
    reader = csv.reader(open(path, 'r'), delimiter=',', quotechar='"')
    reader.next()
    data = {}
     
    for row in reader:
        key = row[0]
        val = row[1]
        data[key] = val
        
    return data

def search_jargon(dictionary, jargonText):
    # open and override report file
    text = 'Jargon report for '+jargonText+'\n\n'
        
    with open(jargonText) as textfile:
        linenumber = 1
        for line in textfile:
            linenumber = linenumber + 1
            for key in dictionary.keys():
                if key in line:
                    text = text + 'Line '+str(linenumber)+': "'+key+'" \n'
                    text = text + ' - substitute with "'+dictionary[key]+'"? \n'
        
    return text
        
if __name__ == '__main__':
    
    jargonDictionary = read_csv(jargonCsv)
    targetFile = sys.argv[1]
    
    text = search_jargon(jargonDictionary, targetFile)

    print text
    
        
    
    