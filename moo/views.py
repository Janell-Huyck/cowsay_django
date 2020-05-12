from django.shortcuts import render
from moo.models import MooText

from moo.forms import MooForm
from moo import get_cow


def index(request):
    cow_list = []
    html = "moo_form.html"
    message_before = "What does the cow say?"
    if request.method == "POST":
        form = MooForm(request.POST)
        if form.is_valid():
            words = form.cleaned_data['text']
            if "'" in words:
                form = MooForm()
                message_before = """Sorry, cows can't speak with apostrophes.
                  Try again?"""
                context = {
                    'form': form,
                    'message_before': message_before,
                    'cow_list': cow_list,
                    'html': html,
                }
                return render(request, 'index.html', context)

            cow_byte_string = get_cow.get_cow(words)
            cow_list = cow_byte_string.decode()
            MooText.objects.create(
                text=words
            )
    form = MooForm()
    context = {
        'form': form,
        'message_before': message_before,
        'cow_list': cow_list,
        'html': html,
    }
    return render(request, 'index.html', context)


def history(request):
    moos = []
    all_moos = MooText.objects.all().order_by('-pk')
    for i in range(0, 10):
        moos.append([i + 1, all_moos[i].text])
    return render(request, 'history.html', {
        'moos': moos, })
