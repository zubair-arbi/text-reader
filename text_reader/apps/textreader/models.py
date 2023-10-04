# -*- coding: utf-8 -*-
import os
import uuid
from datetime import datetime

from django.db import models

from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


def document_file_path(instance, filename):
    """
    Returns a unique file path for the uploaded document.

    Arguments:
        instance (Document): Document object
        filename (str): file to upload

    Returns:
        path: path of image file, e.g. text_reader/files/9e5e516c-fe8a-4975-b955-5e0dc67760ce [2017-11-21 20:46:18].xlsx

    """
    extension = os.path.splitext(filename)[1].lower()
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_name = str(uuid.uuid4()) + ' [' + current_datetime + ']' + extension
    fullname = os.path.join('text_reader/files/', report_name)

    return fullname


def validate_document(value):
    """
    Validate the uploaded files.
    """
    valid_extensions = ['.png', 'jpg']

    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please upload a valid png or jpg file')


class Document(TimeStampedModel):

    description = models.CharField(
        verbose_name=_('Document description'),
        help_text=_('Short description of the document.'),
        max_length=100,
        null=True,
        blank=True,
    )
    document_file = models.FileField(
        verbose_name=_('Document for text reader'),
        upload_to=document_file_path,
        validators=[validate_document],
        help_text=_('Upload document for parsing and text reader.')
    )
