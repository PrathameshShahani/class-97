introString=input('Enter your Introduction: ')
print(introString)
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1

print('number of words in the introduction are: ',wordCount)
print(wordCount)
print('no. of characters are: '+str(characterCount))
print(characterCount)