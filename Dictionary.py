#Dictionary in Python using version3.6
import requests 
import json
#Application id and key for API

app_id = '9b4b4412'
app_key = '3551d89a66ae39ce6a1879151b2e22ce'
while True:
    language = 'en'
    print("input the word :")
    word=input()
#To make key value pair in dictionary by separating a line with respect to' = '
    with open('abc.txt', 'r') as f:
        answer = {}
        for line in f:
            k, v = line.strip().split('=')
            answer[k.strip()] = v.strip()
    if word in answer:
            str2= answer.get(word)
            print(answer[word])
            continue
#if we found the word in the lookup table then there is no need to go further
#documentation in oxford website for the use of API 
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()
    try:
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    except:
        print("Error in reading file")
#its basically status that there is no problem in the program and data has been replaced properly   
    if r.status_code==200:
                        json_data = json.loads(r.text)
                        fdata=json_data.get('results')
                        if len(fdata[0])>0:
                            fdata=fdata[0].get('lexicalEntries')
                            if len(fdata[0])>0:
                                fdata=fdata[0].get('entries')
                                if len(fdata[0])>0:
                                    fdata=fdata[0].get('senses')
                                    if len(fdata[0])>0:
                                        fdata=fdata[0].get('definitions')
                                         
#it basically segregates data from the dictionary json file according to its index in the file
                                        str1 = ''.join(fdata)
                                        print(str1)
                                        with open('abc.txt', 'a') as f:
                                            f.write(word+" = "+str1+"\n") 
#open text file in their respective folder where python projects are saved,it would automatically get updated
                                    else:
                                        print("word not found")
                                else:
                                     print("word not found")
                            else:
                                print("word not found")
                        else:
                            print("word not found")
                            
                        
                         
    else:                 
                        print("u have typed a wrong word") 
#if wrong word it won't be able to get status 200 leading to false statement     
                        continue
    
   