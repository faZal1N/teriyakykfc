from random import randint

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from maps.forms import IntroducingEventForm, LocalMapCreatorForm
from maps.models import Event, LocalMap


# функция необходимая для работы программы, возвращает в виде JsonResponse события, найденные по id
def event_search_id(request):
    search_query = request.GET.get('term')
    results = Event.objects.filter(id=search_query)
    data = [{'id': r.id, 'value': r.name, 'name': r.name,
             'slug': r.slug,
             'begin': r.begin,
             'end': r.end,
             'description': r.description,
             'x': r.x,
             'y': r.y,
             'searchfield': r.searchfield,
             'kml': r.kml,
             'zoom': r.zoom
             } for r in results]

    return JsonResponse(tuple(data), safe=False)


# функция необходимая для работы программы, возвращает в виде JsonResponse события, найденные по запросу пользователя
def event_search(request):
    search_query = request.GET.get('term')
    results = Event.objects.filter(searchfield__icontains=search_query)
    data = [{'id': r.id, 'value': r.name, 'name': r.name,
             'slug': r.slug,
             'begin': r.begin,
             'end': r.end,
             'description': r.description,
             'x': r.x,
             'y': r.y,
             'searchfield': r.searchfield,
             'kml': r.kml,
             'zoom': r.zoom
             } for r in results]

    return JsonResponse(tuple(data), safe=False)


# Create your views here.
def show_maps(request):
    return render(request, 'maps.html', {'random_number': str(randint(1, 200))})


# функция возвращающая форму создания события
@login_required(login_url='login')
def event_introduction(request):
    if not request.user.editor_rights:
        return redirect('getting_editor')
    if request.method == 'POST':
        form = IntroducingEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maps')
    form = IntroducingEventForm()
    return render(request, 'map_introduction.html', {'form': form, 'button_title': 'Добавить событие на сайт'})


# функция необходимая для работы программы, возвращает в виде JsonResponse участников, найденных по id события
def _search_participants(request):
    search_query = request.GET.get('term')
    obj = Event.objects.get(id=search_query)
    participants = obj.person_set.all()
    data = [{'id': r.id, 'value': r.name, 'name': r.name,
             'slug': r.slug,
             'biography': r.biography,
             'photo': r.photo.url,
             } for r in participants]

    return JsonResponse(tuple(data), safe=False)


# функция необходимая для работы программы, возвращает в виде JsonResponse локальные карты, найденные по id события
def _search_local_maps(request):
    search_query = request.GET.get('term')
    results = LocalMap.objects.filter(event_link=search_query)
    data = [{'id': r.id, 'value': r.name, 'name': r.name,
             'slug': r.slug,
             'description': r.description,
             'small_map': r.small_map.url,
             'url': r.x,
             'x': r.x,
             'y': r.y,
             } for r in results]
    return JsonResponse(tuple(data), safe=False)


# функция возвращающая страницу события
def event_page(request, slug):
    obj = Event.objects.get(slug=slug)
    participants = obj.person_set.all()
    maps = LocalMap.objects.filter(event_link=obj)
    return render(request, 'event.html', {'obj': obj, 'expansion': participants, 'local_maps': maps})


# функция возвращающая форму для изменения события
@login_required(login_url='login')
def event_editing(request, slug):
    if not request.user.editor_rights:
        return redirect('getting_editor')
    obj = Event.objects.get(slug=slug)
    if request.method == 'POST':
        form = IntroducingEventForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('maps')
    form = IntroducingEventForm(instance=obj)
    participants = obj.person_set.all()
    maps = LocalMap.objects.filter(event_link=obj)
    return render(request, 'map_introduction.html',
                  {'form': form, 'button_title': 'Изменить данные о событии', 'editing': 1, 'maps': maps,
                   'participants': participants})


# функция возвращающая форму для создания локальной карты
@login_required(login_url='login')
def local_map_creator(request):
    if not request.user.editor_rights:
        return redirect('getting_editor')
    if request.method == 'POST':
        form = LocalMapCreatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maps')
    form = LocalMapCreatorForm()
    return render(request, 'local_map_creator.html', {'form': form, 'button_title': 'Добавить событие на сайт'})


# функция возвращающая форму для изменения локальной карты
@login_required(login_url='login')
def edit_local_map(request, slug):
    if not request.user.editor_rights:
        return redirect('getting_editor')
    obj = LocalMap.objects.get(slug=slug)
    if request.method == 'POST':
        form = LocalMapCreatorForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('maps')
    form = LocalMapCreatorForm(instance=obj)
    return render(request, 'local_map_editor.html', {'form': form, 'button_title': 'Изменить локальную карту'})
