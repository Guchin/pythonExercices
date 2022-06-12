
"""" 
 to develop a python program in which we have given a string and in one condition we need to make the all possible combinations
  and substring using that string that start with consonants and in another condition, we need to make the all possible combinations 
  that start with vowels.

"""


def algorithm(string):
    scoreVowels = 0
    scoreConsonants =0
    vowels =['A','E','I','O','U']
    stringLength =len(string)
    fragments =[]
    arrayString =list(string)
    for letter in range(stringLength):
        fragmentArray = arrayString[letter:stringLength]
        fragmentedWord = ''.join(fragmentArray)        
        fragments.append(fragmentedWord)
    print(fragments)
    for fragment in fragments:
        if fragment[0] in vowels: 
            scoreVowels +=1
        else:
            scoreConsonants +=1  

    print(scoreVowels)    

    scoreWinner = max(scoreVowels,scoreConsonants)
    
    
    scoreWinner = max(scoreVowels, scoreConsonants)
    return scoreVowels, scoreConsonants, scoreWinner



def minion_game(string):
    scorePlayerVowels, scorePlayerConsonants,scoreWinner = algorithm(string)
    playerVowels ='Kevin'
    playerConsonants ='Stuart'
    
    if  scorePlayerVowels > scorePlayerConsonants:
        winner = playerVowels      
    elif  scorePlayerConsonants > scorePlayerVowels:
        winner =  playerConsonants
    elif   scorePlayerConsonants == scorePlayerVowels:
        winner = None
            
    if scorePlayerVowels != scorePlayerConsonants:
        return winner+ " " + str(scoreWinner)
    else: 
        return "Draw"
    

if __name__ == '__main__':

    print(minion_game("PALABRA"))