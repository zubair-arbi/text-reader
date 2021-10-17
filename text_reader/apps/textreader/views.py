import logging

from django.contrib import messages
from django.shortcuts import render

from text_reader.apps.textreader.models import Document

LOGGER = logging.getLogger(__name__)


def documents_view(request):
    """
    Render view for documents listing page.
    """
    user_full_name = ''
    if not request.user.is_authenticated:
        # TODO: return to login page
        return None

    documents = Document.objects.all()
    context = {
        'documents': documents,
    }

    return render(request, 'textreader/documents.html', context)
