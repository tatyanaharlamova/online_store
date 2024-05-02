import json

from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contacts_dict = {"name": name, "phone": phone, "message": message[:]}

        with open("contacts.json", "w") as file:
            json.dump(contacts_dict, file, ensure_ascii=False, indent=4)

    return render(request, 'contacts.html')
