import requests#this project is based on python 3.6
import json
try:
    f = open("abc.txt", 'w')#it is important to open file here as in the start only we would be needing a file for lookup else it would show error
except IOError:
   print("Error: can\'t find file or read data")#to catch the error and not making program stop
app_id = '9b4b4412'
app_key = '3551d89a66ae39ce6a1879151b2e22ce'
while True:
    language = 'en'
    print("input the word :")
    word=input()
    try:
        f = open("abc.txt", 'r')
        answer = {}
        for line in f:
            k, v = line.strip().split('=')#it is basically done to make key value pair in dictionary by separating a line with respect to'='
            answer[k.strip()] = v.strip()
    
     
        if word in answer:
            str2= answer.get(word)
            print(answer[word])
            continue#if we found the word in the lookup table then there is no need to go further
     
    
        f.close()
    except:#here its not considered a good programming practice though, because it catches all exceptions but does not make the programmer identify the root cause of the problem that may occur.
        print("Error: can\'t find file or read data")
           
    
    
    try:
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()#it is basically based on documentation in oxford website for the use of API
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        if r.status_code==200:#its basically status that there is no problem in the program and data has been replaced properly
                            json_data = json.loads(r.text)
                            fdata=json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'] #it basically segregades data from the dictionary json file according to its index in the file
                            str1 = ''.join(fdata)
                            print(str1)
                            f = open("abc.txt", 'a')#text file in append mode
                            f.write(word) 
                            f.write(" = ")
                            f.write(str1)
                            f.write("\n")
                            f.close()#one could open txt file in their respective folder where python projects are saved,it would automatically get updated
                              
        else:                 
                            print("u have typed a wrong word") #if wrong word is typed than it won't be able to get status 200 leading to false statement,so wrong word     
                            continue
    except:
        print("Error: can\'t find file or read data")                    
    
   