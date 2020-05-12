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


def moolist(request):
    moos = []
    all_moos = MooText.objects.all().order_by('-pk')
    for i in range(0, 10):
        moos.append([i + 1, all_moos[i].text])
    return render(request, 'moo_list.html', {
        'moos': moos, })
