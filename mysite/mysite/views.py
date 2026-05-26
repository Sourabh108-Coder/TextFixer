from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def text_check(request):

    djtext = request.POST.get('text', '').strip()

    remove_punc = request.POST.get('val')
    capitalize = request.POST.get('val1')
    remove_spaces = request.POST.get('spr')
    remove_newlines = request.POST.get('nlr')

    # Empty input check
    if not djtext:
        messages.info(request, "Please Enter Some Text!")
        return redirect('/')

    analyzed_text = djtext
    operations = []

    # Remove punctuations
    if remove_punc == "on":

        punc_list = '''`~!@#$%^&*()_-+=[]{}|\\:;"'<>,.?/'''

        analyzed_text = "".join(
            char for char in analyzed_text
            if char not in punc_list
        )

        operations.append("Removed Punctuations")

    # Capitalize text
    if capitalize == "on":

        analyzed_text = analyzed_text.upper()

        operations.append("Capitalized Text")

    # Remove extra spaces
    if remove_spaces == "on":

        analyzed_text = " ".join(analyzed_text.split())

        operations.append("Removed Extra Spaces")

    # Remove new lines
    if remove_newlines == "on":

        analyzed_text = analyzed_text.replace("\n", "").replace("\r", "")

        operations.append("Removed New Lines")

    # No option selected
    if not operations:

        messages.warning(request, "Please Select an Option!")
        return redirect('/')

    params = {
        'purpose': ", ".join(operations),
        'analyzed_text': analyzed_text
    }

    return render(request, 'analyze.html', params)