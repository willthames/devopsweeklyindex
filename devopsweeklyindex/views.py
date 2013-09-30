from django.shortcuts import render
from search.forms import SearchForm
from search.models import SearchResult
from datetime import datetime

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, error_class=ErrorBox)
        if form.is_valid():
            csf = form.cleaned_data
            survey = TeamTemperature(creation_date = datetime.now(),
                                     password = make_password(csf['password']),
                                     creator = user,
                                     id = form_id)
            survey.save()
            return render(request, 'results.html', {'form': form})
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form': form})
