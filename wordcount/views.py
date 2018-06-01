from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    #return HttpResponse('Welcome to my world!!!')
    return render(request,'home.html',{"Name":"My name is Pinaki Mishra"})

def destiny(request):
    return HttpResponse("<h1>Destiny for me!!!</h1>")

def count(request):
    myinput = request.GET['myinput']
    #print(myinput)
    wordlist = myinput.split()
    worddictionary ={}
    for word in wordlist:
        if word in worddictionary:
            # Increase the count
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    # Sort the word list
    sortedlist = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=False)#Sort as Ascending order

    return render(request,'count.html',{'myinput':myinput,'wordcount':len(wordlist),'sortedlist':sortedlist})

def about(request):
    return render(request,'About.html',{"Name":"Pinaki Prasad Mishra","Company":"Test",
                                        "Role":"Lead QA Engineer"})