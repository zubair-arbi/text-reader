import logging

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from text_reader.apps.textreader.forms import DocumentUploadForm
from text_reader.apps.textreader.models import Document

LOGGER = logging.getLogger(__name__)


def documents_view(request):
    """
    Render view for documents listing page.
    """
    user_full_name = ''
    if not request.user.is_authenticated:
        LOGGER.info('User %s is not authenticated' % request.user)
        # TODO: return to login page
        return None

    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_document = Document(document_file=request.FILES['document_file'])
            new_document.description = request.POST.get('description')
            new_document.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('textreader:view_documents'))

    documents = Document.objects.all()
    context = {
        'documents': documents,
        'document_form': DocumentUploadForm(),
    }

    return render(request, 'textreader/documents.html', context)
