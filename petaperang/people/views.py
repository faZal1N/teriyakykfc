from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse

from people.forms import IntroducingPersonForm, SearchingPersonalityForm
from people.models import Person


# функция необходимая для работы программы, возвращает в виде JsonResponse события, найденные по запросу пользователя
def people_ssearch(request):
    search_query = request.GET.get('term')
    results = Person.objects.filter(searchfield__icontains=search_query)
    data = [
        {'id': r.id, 'value': r.name, 'name': r.name, 'slug': r.slug, 'biography': r.biography, 'photo': r.photo.url}
        for r in results]
    return JsonResponse(tuple(data), safe=False)


# функция возвращающая людей, которые присутствуют на сайте
def show_people(request):
    form = SearchingPersonalityForm()
    search_query = request.POST.get('search_engine', '')
    result = Person.objects.filter(Q(name__icontains=search_query) | Q(biography__icontains=search_query))
    if not result:
        result = Person.objects.all()
    return render(request, 'people.html', {'result': result, 'form': form})


# функция возвращает форму для создания человека на сайте
@login_required(login_url='login')
def person_introduction(request):
    if not request.user.editor_rights:
        return redirect('getting_editor')
    if request.method == 'POST':
        form = IntroducingPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('people')
    form = IntroducingPersonForm()
    return render(request, 'person_introduction.html', {'form': form, 'button_title': 'Добавить человека на сайт'})


# функция возвращает страницу человека
def personality_page(request, slug):
    obj = Person.objects.get(slug=slug)
    events = obj.events.all()
    return render(request, 'personality.html',
                  {'obj': obj, 'expansions': events, 'button_title': 'Изменить данные о человеке'})


# функция возвращает форму для изменнения человека на сайте
@login_required(login_url='login')
def personality_editing(request, slug):
    if not request.user.editor_rights:
        return redirect('getting_editor')
    obj = Person.objects.get(slug=slug)
    if request.method == 'POST':
        form = IntroducingPersonForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('people')
    form = IntroducingPersonForm(instance=obj)
    return render(request, 'person_introduction.html', {'form': form})
