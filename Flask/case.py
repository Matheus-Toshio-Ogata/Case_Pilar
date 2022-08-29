from urllib import response
from flask import Flask,  request
app = Flask(__name__)

@app.post("/vowel_count")
def vowel_count() : 
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  response = {}
  list_words = request.get_json()["words"]
  for i in range(1, len(list_words)) :
    response[list_words[i]] = len([j for j in list_words[i] if j in vowels])
  #for  word in request.get_json()["words"] : 
    #response[word] = len([i for i in word if i in vowels])
  return response

@app.post("/sort")
def sort_word() :
    if request.get_json()["order"] == 'asc' :
        request.get_json()["words"].sort(key=str.lower)
        return request.get_json()["words"]
    else : 
        request.get_json()["words"].sort(reverse = True, key=str.lower)
        return request.get_json()["words"]