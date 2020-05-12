from django.shortcuts import render

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
    form = MooForm()
    context = {
        'form': form,
        'message_before': message_before,
        'cow_list': cow_list,
        'html': html,
    }
    return render(request, 'index.html', context)
