from django.shortcuts import render
from .models import Guest

def invite_view(request):
    if request.method == 'POST':
        guest_name = request.POST.get('guest_name')
        print(f"Получено имя: {guest_name}") # Это появится в терминале VS Code
        
        if guest_name:
            new_guest = Guest.objects.create(name=guest_name)
            print(f"Создан объект: {new_guest.id}") # Проверка создания
            return render(request, 'articles/base.html', {'success': True})
    
    return render(request, 'articles/base.html')
