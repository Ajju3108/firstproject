from django.shortcuts import render

# Create your views here.
def index(resquest):

    return render(resquest,'News24App/index.html')

def sportsnews(resquest):
    my_dict = {'head_msg': 'Sports Information',
               'sub_msg1': 'Anushka Sharma Firing Like anything',
               'sub_msg2': 'Kohli updating in game anything can happend',
               'sub_msg3': 'Worst Performance by India-Sehwag',
               'photo': 'images/yuvraj.jpg'}
    return render(resquest,'News24Ap/news.html',context=my_dict)

def politics(resquest):
    my_dict = {'head_msg': 'Politics Information',
               'sub_msg1': 'Achhce Din Aaa gaya',
               'sub_msg2': 'Rupee Value now 1$:70Rs',
               'sub_msg3': 'In India Single Paisa Black money No more',
               'photo': 'images/saheb..jpg'}
    return render(resquest,'News24App/news.html',context=my_dict)

def bollywood(resquest):
    my_dict = {'head_msg': 'Movies Information',
               'sub_msg1': 'Sushant singh Commited to sucide',
               'sub_msg2': 'kangana reacts strongly to nepotism',
               'sub_msg3': 'Salman Khan ready to marriage',
               'photo': 'images/sushant.jpg'
               }

    return render(resquest,'News24App/news.html',context=my_dict)