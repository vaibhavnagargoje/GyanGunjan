from django.contrib import admin
from .models import PDFDocument

@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'processed')
    list_filter = ('processed',)
    search_fields = ('title', 'content')
    readonly_fields = ('uploaded_at',)