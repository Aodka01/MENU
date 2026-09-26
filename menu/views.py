from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Dish
from .forms import DishForm


def menu_list(request):
    q = request.GET.get('q', '').strip()
    dishes = Dish.objects.filter(available=True)
    if q:
        dishes = dishes.filter(name__icontains=q) | dishes.filter(description__icontains=q)
    dishes = dishes.order_by('name')
    return render(request, 'menu_list.html', {'dishes': dishes})


def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = DishForm()
    return render(request, 'menu_form.html', {'form': form, 'title': 'Crear platillo'})


def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'menu_form.html', {'form': form, 'title': 'Editar platillo'})


def dish_delete(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish.delete()
        return redirect('menu_list')
    return render(request, 'menu_confirm_delete.html', {'dish': dish})
