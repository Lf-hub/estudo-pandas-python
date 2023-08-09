from django.shortcuts import render
from django.views.generic import View, ListView

from common.models import File, Lines
from common.process import ProcessLine


class CommonIndexView(ListView):
    model = Lines
    template_name = 'index.html'


class ImportFile(View):
    model = File
    
    def post(self, request):
        # Pega arquivo
        file = self.request.FILES.get('file')
        process = ProcessLine
        process.execute(file)
        return render(request, 'index.html')