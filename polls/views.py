from django.shortcuts import render,redirect
import pickle


import numpy as np

# Create your views here.
def index_func(request):
    res=3   
    
    if request.method =='POST':
        res=3
        input_text= request.POST['inputtext']
        text_x1=[input_text]
        filename2 = 'polls/senticv.pickle'
        cv1=pickle.load(open(filename2,'rb'))
        test_x2=cv1.transform(text_x1)
     
        filename1 = 'polls/senti.pickle'
        loaded_model = pickle.load(open(filename1, 'rb'))

        res = loaded_model.predict(test_x2)
        

        if res == 0:
            res = "Sad"
            # img='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-ztdzh&psig=AOvVaw1GjIol3yCcNvKgTHJ4mLa3&ust=1644041338295000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNC9h7yx5fUCFQAAAAAdAAAAABAD'
        elif res == 1:
            res = 'Happy'
            #img='https://i.ebayimg.com/images/g/22YAAOSwT4ZbCfHb/s-l400.jpg'
        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response':res})