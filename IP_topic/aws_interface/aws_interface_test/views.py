from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Document
from django.views.generic import ListView

# Create your views here.
class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'upload_file.html'
    success_url = reverse_lazy('home')

def download(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    response = HttpResponse(document.document, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.document.name}"'
    return response

class DocumentListView(ListView):
    model = Document
    template_name = 'download_file.html'
    context_object_name = 'documents'