from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

# Create your views here.

from django_tables2 import SingleTableView

from .models import Road
from .models import Region
from .models import Station
# from rzd.models import Zdanie

from .forms import RoadForm
from .forms import RegionForm
from .forms import StationForm
from .tables import RoadTable


# from .tables import RegionTable
# from .tables import StationTable


def index(request):
    #    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'web/index.html')


def rzd_map(request):
    stations = Station.objects.all()
    return render(request, 'rzd-map.html', {'stations': stations})


# отображение на основе функции
def road_list(request):
    roads = Road.objects.all()
    return render(request, 'rzd/road_list.html', {'roads': roads})

def road_add(request):
    error = ''
    if request.method == 'POST':  # нажата кнопка Добавить
        form = RoadForm(request.POST)  # получаем данные с формы ввода
        if form.is_valid():  # проверяем корректность данных
            form.save()
            return redirect('road')  # need import redirect
        else:
            error = 'Форма неверна'

    form = RoadForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'rzd/road_create.html', data)




# отображение на основе предопределенного класса
class RoadListView(ListView):
    model = Road
    # template_name = 'rzd/road_list.html' #default: <app-name>rzd/<model-name>_list.html = rzd/goroga_list.html
    template_name = 'rzd/road_list.html'
    # template_name = 'rzd/def_listview.html'
    context_object_name = 'roads'  # название ключа, по которому запись передается внутрь шаблона, default: object_list
    extra_context = {'title': 'Дороги', 'url_add': '/rzd/road/add', 'url_add_name': 'Добавить дорогу',
                     'url_edit': '/rzd/road/edit', 'url_edit_name': 'Редактировать дорогу'}
    queryset = Road.objects.all().order_by('kod')

class RoadTableView(SingleTableView):
    model = Road
    table = RoadTable
    context_object_name = 'roads'
    template_name = 'rzd/road_table.html'
    queryset = Road.objects.all().order_by('kod')

class RoadCreateView(CreateView):
    model = Road
    template_name = 'rzd/road_create.html'
    form_class = RoadForm
    success_url = 'road_list/'
'''
    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
	    context[’roads’] = Road.objects.all()
	    return context
'''

class RoadDetailView(DetailView):
    model = Road
    template_name = 'rzd/road_detail.html'
    context_object_name = 'road'  # название ключа, по которому запись передантся внутрь шаблона, default: object_list
    # extra_context = {'title': 'РЖД Дороги'} #not work


class RoadUpdateView(UpdateView):
    model = Road
    template_name = 'rzd/road_create.html'
    # fields = ['name', 'short_name', 'kod'] #use form_class
    form_class = RoadForm


class RoadDeleteView(DeleteView):
    model = Road
    success_url = '/rzd/road/'  # dont use url, use name
    # success_url = reverse_lazy('road')
    template_name = 'rzd/road_delete.html'


def region_list(request):
    regions = Region.objects.all()
    return render(request, 'rzd/region_list.html', {'regions': regions})


class RegionListView(ListView):
    model = Region
    # template_name = 'rzd/region_list.html' #default: rzd/region_list.html
    # context_object_name = 'regions' # default: object_list


# class RegionTableView(SingleTableView):
#    model = Region
#    table = RegionTable
#    template_name = 'region_table.html'
##    queryset = Region.objects.all().order_by('kod')

# class RegionDetailView(DetailView):
#    model = Region
#    #template_name = 'rzd/region_detail.html' #default: rzd/region_detail.html

class RegionUpdateView(UpdateView):
    model = Region
    template_name = 'rzd/region_create.html'
    # fields = ['name', 'short_name', 'kod'] #use form_class
    form_class = RegionForm


class RegionDeleteView(DeleteView):
    model = Region
    success_url = '/rzd/region/'  # dont use url, use name
    # success_url = reverse_lazy('region')
    template_name = 'rzd/region_delete.html'  # default: rzd/region_confirm_delete.html


class RegionCreateView(CreateView):
    model = Region
    template_name = 'rzd/region_create.html'
    form_class = RegionForm
    success_url = 'region_list/'


def region_add(request):
    error = ''
    if request.method == 'POST':  # нажата кнопка Добавить
        form = RegionForm(request.POST)  # получаем данные с формы ввода
        if form.is_valid():  # проверяем корректность данных
            form.save()
            return redirect('region')  # need import redirect
        else:
            error = 'Форма неверна'

    form = RegionForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'rzd/region_create.html', data)


class StationListView(ListView):
    model = Station
    # template_name = 'rzd/station_list.html' #default: rzd/station_list.html
    # context_object_name = 'stations' # default: object_list
    paginate_by = 17


class StationTableView(SingleTableView):
    model = Station
    # table = StationTable
    # template_name = 'station_table.html'


class StationDetailView(DetailView):
    model = Station
    # template_name = 'rzd/station_detail.html' #default rzd/station_detail.html


class StationUpdateView(UpdateView):
    model = Station
    template_name = 'rzd/station_create.html'
    # fields = ['name', 'short_name', 'kod'] #use form_class
    form_class = StationForm


class StationDeleteView(DeleteView):
    model = Station
    success_url = '/rzd/station/'  # dont use url, use name
    # success_url = reverse_lazy('Station')
    template_name = 'rzd/station_delete.html'  # default: rzd/station_confirm_delete.html


def station_add(request):
    error = ''
    if request.method == 'POST':  # нажата кнопка Добавить
        form = StationForm(request.POST)  # получаем данные с формы ввода
        if form.is_valid():  # проверяем корректность данных
            form.save()
            return redirect('region')  # need import redirect
        else:
            error = 'Форма неверна'

    form = StationForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'rzd/station_create.html', data)


