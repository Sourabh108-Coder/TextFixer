from django.http import HttpResponse

from django.shortcuts import redirect, render

from django.contrib import messages

def index(request):
    return render(request,'index.html')


def text_check(request):

    djtext=(request.POST.get('text','default'))
    on_off1=(request.POST.get('val','off'))
    on_off2=(request.POST.get('val1','off'))
    on_off3=(request.POST.get('spr','off'))
    on_off4=(request.POST.get('nlr','off'))

    if(djtext==""):
        messages.info(request, "Please Enter Some Text!!")
        return redirect('/')


    if(on_off1=="on"):

        analyze=""

        punc_list='''`~!@#$%^&?/\|=:;'''

        for char in djtext:

            if char not in punc_list:
                analyze=analyze+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyze}

        djtext=analyze

    if(on_off2=="on"):

        analyze=""

        for char in djtext:

            analyze=analyze+char.upper()

        params={'purpose':'Captalize Text','analyzed_text':analyze}

        djtext=analyze

    if(on_off3=="on"):

        analyze=""

        for index,char in enumerate(djtext):

            if djtext[index]==" " and djtext[index+1]==" ":

               pass

            else:
                analyze=analyze+char

        params={'purpose':'Space Removing','analyzed_text':analyze}

        djtext=analyze

    if(on_off4=="on"):

        analyze=""

        for char in djtext:

            if char!="\n" and char!="\r":

                analyze=analyze+char

        params={'purpose':'Newline Removing','analyzed_text':analyze}

        djtext=analyze

    if(on_off1!="on" and on_off2!="on" and on_off3!="on" and on_off4!="on"):

        messages.warning(request, "Please Select a Radio Button!!")
        return redirect('/')

    
    return render(request,'analyze.html',params)
