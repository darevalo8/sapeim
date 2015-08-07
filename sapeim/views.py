from django.shortcuts import render, redirect
from django.http import HttpResponse
#importo a formset :D
from django.forms.formsets import formset_factory
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import AddElementForm, AddBlandForm, UserProfileForm, UserForm
from .forms import PrestamoForm, DetalleForm, PrestaForm
from .models import Element, Bland, UserProfile, Prestamo, DetallePrestamo, ElementType


class IndexView(ListView):
    model = Element
    template_name = 'sapeim/index.html'
    context_object_name = 'elemento'


class AddElement(CreateView):
    form_class = AddElementForm
    template_name = 'sapeim/admin/add_elemento.html'
    success_url = '/'


class UpdateElement(UpdateView):
    form_class = AddElementForm
    model = Element
    template_name = 'sapeim/admin/edit_element.html'
    #fields = ('bland', 'element_type', 'serial', 'serial_sena', 'modelo', 'features')
    # esta funcion es para que me deje en la misma url donde me encuentro :D

    def get_success_url(self):
    # esta funcion es para que me deje en la misma url donde me encuentro :D
        return self.request.path


class DeleteElement(DeleteView):
    #form_class = AddElementForm
    model = Element
    template_name = 'sapeim/admin/delete_element.html'
    success_url = '/'


class ListBland(ListView):
    model = Bland
    template_name = 'sapeim/admin/list_bland.html'
    context_object_name = 'lista'


class AddBland(CreateView):
    form_class = AddBlandForm
    success_url = 'sapeim:list-bland'
    template_name = 'sapeim/admin/add_bland.html'
# falta hacer el update de marcas


class DeleteBland(DeleteView):
    model = Bland
    success_url = 'sapeim:list-bland'
    template_name = 'sapeim/admin/delete_element.html'
    context_object_name = 'lista'


class ListElementType(ListView):
    model = ElementType
    template_name = 'sapeim/admin/list_type.html'
    context_object_name = "tipo"


class AddElementType(CreateView):
    model = ElementType
    success_url = "sapeim:list-type"
    template_name = 'sapeim/admin/add_type.html'
    fields = ('element_type',)


class DeleteElementType(DeleteView):
    model = ElementType
    success_url = 'sapeim:list_type'
    template_name = 'sapeim/admin/delete_element.html'
    context_object_name = 'type'
#falta hacer el update de tipo de elemento


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
    return render(request, 'sapeim/admin/registro.html', {'user': user_u, 'profile': user_pro})


class ListPrestamo(ListView):
    model = Prestamo
    template_name = 'sapeim/admin/list_prestamos.html'
    context_object_name = 'prestmos'
    queryset = Prestamo.objects.filter(devolucion=False)


class DetailPrestamo(DetailView):
    model = Prestamo
    template_name = 'sapeim/admin/detail_prestamo.html'

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super(DetailPrestamo, self).get_context_data(**kwargs)
             #Add in a QuerySet of all the books
            context['elemento'] = DetallePrestamo.objects.filter()
            return context


def prestamo(request):
    query = request.POST.get('documento')
    print(query)
    if request.method == 'POST':
        user_pro = UserProfile.objects.get(documento=query)
        prestamo = PrestaForm(request.POST)
        detail = DetalleForm(request.POST)

        if prestamo.is_valid() and detail.is_valid():
            detalle = detail.save(commit=False)
            elemento = Element.objects.get(modelo=detalle.element)
            if elemento.state == 2:
                return HttpResponse('este elemento ya esta prestado :D')
            else:
                presta = prestamo.save(commit=False)
                presta.user = user_pro
                presta.save()
                elemento.state = 2
                elemento.save()
                detalle.prestamo = presta
                detalle.save()
        else:
            print("hola")
        return redirect('sapeim:prestamos')
    else:
        prestamo = PrestaForm()
        detail = DetalleForm()
    return render(request, 'sapeim/admin/prestamo.html', {'prestamo': prestamo, 'detalle': detail})


def devolucion(request, **kwargs):
    pk = kwargs.get('pk')
    prestamo = Prestamo.objects.get(pk=pk)
    detalle = DetallePrestamo.objects.get(prestamo=pk)
    if request.method == 'POST':
        presta = PrestamoForm(request.POST, instance=prestamo)
        if presta.is_valid():
            pres = presta.save(commit=False)
            if pres.devolucion:
                elemento = Element.objects.get(modelo=detalle.element)
                elemento.state = 1
                elemento.save()
                pres.save()
                return redirect('sapeim:prestamos')
    else:
        presta = PrestamoForm(instance=prestamo)
    return render(request, 'sapeim/admin/devoluciones.html', {'prestamo': presta, 'detalle': detalle})
