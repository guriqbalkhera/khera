import requests
import json

fo = open("Dictionarii.txt", "a")

print("Name of the file: ", fo.name)

dict={}
app_id = '9b4b4412'
app_key = '3551d89a66ae39ce6a1879151b2e22ce'
while True:
    language = 'en'
    id=input('input the word :')
    word_id = id

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})


    #print("code {}\n".format(r.status_code))

    if r.status_code==200:
                          a=9
    else:                 
                         print("wrong word")      
                         continue
                        
    json_data = json.loads(r.text)
    fdata=json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
    str1 = ''.join(fdata)
    
    if word_id in dict:
                       str2= dict.get(word_id)
                       print(dict[word_id])
    else:
                            dict[word_id]=str1
                            print(dict[word_id])
                            fo = open("Dictionarii.txt", "a")
                            fo.write(word_id) 
                            fo.write(": ")
                            fo.write(str1)
                            fo.write("\n")
                            fo.close()                           
                            fo = open("Dictionarii.txt", "r")
                            print(fo.read())   
                            fo.close()