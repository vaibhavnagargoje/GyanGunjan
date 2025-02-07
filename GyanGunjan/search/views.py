from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from .models import PDFDocument
from .utils.search_utils import SearchEngine

class PDFUploadView(View):
    def get(self, request):
        return render(request, 'search/upload.html')

    def post(self, request):
        if 'pdf' in request.FILES:
            pdf_file = request.FILES['pdf']
            fs = FileSystemStorage()
            filename = fs.save(pdf_file.name, pdf_file)
            
            # Create and process document
            pdf_doc = PDFDocument.objects.create(
                title=filename,
                file=filename,
                content=''
            )
            self._process_pdf(pdf_doc.id)
            return redirect('search')
        return render(request, 'search/upload.html', {'error': True})

    def _process_pdf(self, doc_id):
        from PyPDF2 import PdfReader
        try:
            doc = PDFDocument.objects.get(id=doc_id)
            reader = PdfReader(doc.file.path)
            content = [page.extract_text() or '' for page in reader.pages]
            doc.content = '\n'.join(content)
            doc.processed = True
            doc.save()
        except Exception as e:
            doc.delete()
            raise e

class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        results = []
        
        if query:
            engine = SearchEngine()
            results = engine.search(query)
            
        return render(request, 'search/results.html', {
            'query': query,
            'results': results
        })