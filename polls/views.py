from django.shortcuts import render,redirect
import pickle


import numpy as np

# Create your views here.
def index_func(request):
    res=''
     
    
    if request.method =='POST':
        input_text= request.POST['inputtext']
        if  input_text !=  '':
            text_x1=[input_text]
            filename2 = 'polls/senticv.pickle'
            cv1=pickle.load(open(filename2,'rb'))
            test_x2=cv1.transform(text_x1)
     
            filename1 = 'polls/senti.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))

            res = loaded_model.predict(test_x2)
        

            if res == 0:
               res = "Sad"
            elif res == 1:
                res = 'Happy'
        
            else:
                return redirect('homepage')
        else:
            res == ' '
            return redirect('homepage')      
    else:
        pass

    return render(request, "index.html", {'response':res})