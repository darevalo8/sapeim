from django.shortcuts import render, redirect
from django.http import HttpResponse
#importo a formset :D
from django.forms.formsets import formset_factory
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import AddElementForm, AddBlandForm, UserProfileForm, UserForm
from .forms import PrestamoForm, DetalleForm, PrestaForm
from .models import Element, Bland, UserProfile, Prestamo, DetallePrestamo


class IndexView(ListView):
    model = Element
    template_name = 'sapeim/index.html'
    context_object_name = 'elemento'


class AddElement(CreateView):
    form_class = AddElementForm
    template_name = 'sapeim/add_elemento.html'
    success_url = '/'


class UpdateElement(UpdateView):
    form_class = AddElementForm
    model = Element
    template_name = 'sapeim/edit_element.html'
    #fields = ('bland', 'element_type', 'serial', 'serial_sena', 'modelo', 'features')
    # esta funcion es para que me deje en la misma url donde me encuentro :D

    def get_success_url(self):
    # esta funcion es para que me deje en la misma url donde me encuentro :D
        return self.request.path


class DeleteElement(DeleteView):
    #form_class = AddElementForm
    model = Element
    template_name = 'sapeim/delete_element.html'
    success_url = '/'


class ListBland(ListView):
    model = Bland
    template_name = 'sapeim/list_bland.html'
    context_object_name = 'lista'


class AddBland(CreateView):
    form_class = AddBlandForm
    success_url = 'list-bland'
    template_name = 'sapeim/add_elemento.html'


class DeleteBland(DeleteView):
    model = Bland
    success_url = '/list-bland'
    template_name = 'sapeim/delete_element.html'
    context_object_name = 'lista'


def registro(request):
    if request.method == 'POST':
        user_pro = UserProfileForm(request.POST)
        user_u = UserForm(request.POST)
        if user_u.is_valid() and user_u.is_valid():
            user = user_u.save()
            user.set_password(user.password)#encrypto la pass
            user.save()
            profile_u = user_pro.save(commit=False)
            profile_u.username = user
            profile_u.save()
            return redirect('/')
        else:
            print("error")
    else:
        user_u = UserForm()
        user_pro = UserProfileForm()
    return render(request, 'sapeim/registro.html', {'user': user_u, 'profile': user_pro})


class ListPrestamo(ListView):
    model = Prestamo
    template_name = 'sapeim/list_prestamos.html'
    context_object_name = 'prestmos'
    queryset = Prestamo.objects.filter(devolucion=False)


class DetailPrestamo(DetailView):
    model = Prestamo
    template_name = 'sapeim/detail_prestamo.html'

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super(DetailPrestamo, self).get_context_data(**kwargs)
             #Add in a QuerySet of all the books
            context['elemento'] = DetallePrestamo.objects.filter()
            return context


def prestamo(request):
    query = request.POST.get('documento')
    user_pres = UserProfile.objects.get(documento=query)
    ########
    detalle_prestamo = formset_factory(DetalleForm, extra=2)
    #hago un formset_factory, los formset
    #sirver para agregar otro formulario mas por asi decirlo
    #reciben como parametro el form creado en forms.py y un parametro extra
    #que sera las vece que se repetira el modelo form
    #################################################
    if request.method == 'POST':
        prestamo = PrestamoForm(request.POST)
        detalle = detalle_prestamo(request.POST)

        if prestamo.is_valid() and detalle.is_valid():
            pres = prestamo.save(commit=False)
            pres.user = user_pres
            pres.save()
            ############################
            # hago un for con el formulario detalle porque
            # el es un formset ya osea que tiene que guardar la cantidad
            # de registro guardada en este caso yo le puse extra = 2 asi que itera
            #dos veces
            #############################
            for gurdar in detalle:
                detail = gurdar.save(commit=False)
                detail.prestamo = pres# añado el prestamo al cual pertenece elemento
                elemento = detail.element# le asigno a la variable elemento el , elemento del prestamo, el no retorna un id retorna el modelo del elemento
                element = Element.objects.get(modelo=elemento)#aca filtro los elementos a prestamar por modelo ya que el modelo elemento retorna el modelo, lo filtro por modelo se lo asigno a la variable element
                element.state = 2#aca le cambio el estado al elemento a ocupado
                element.save()
                detail.save()
            return redirect('/')
        else:
            print("error")
    else:
        prestamo = PrestamoForm()
        detalle = detalle_prestamo()
        print("estoy aca")
    return render(request, 'sapeim/prestamo.html', {'prestamo': prestamo, 'detalle': detalle})


