from django.shortcuts import render, redirect
from stnk.forms import TambahOpdForm, TambahAssetForm
from stnk.models import Asset, Opd
from django.views import View

def home(request):
    return render(request,'stnk/home.html')

class TambahOpd(View):
    template_name = 'stnk/tambah_opd.html'
    def get(self, request):
        form = TambahOpdForm
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = TambahOpdForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('listdata')
        return render(request, self.template_name,{'form':form})

class LihatAsset(View):
    template_name = 'stnk/list_stnk.html'
    def get(self, request):
        stnk = Asset.objects.all()
        return render(request, self.template_name,{'stnk':stnk})

class TambahAsset(View):
    template_name = 'stnk/tambah_data.html'
    def get(self, request):
        form = TambahAssetForm
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = TambahAssetForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('listdata')
        return render(request, 'stnk/tambah_data.html', {'form':form})

class EditAsset(View):
    template_name = 'stnk/edit_data.html'    
    def get(self, request, id):
        asset = Asset.objects.get(id=id)
        data = {
            'form': TambahAssetForm(instance=asset)
        }
        return render(request, self.template_name, data)

    def post(self,request, id):
        asset = Asset.objects.get(id=id)
        form = TambahAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('listdata')

class HapusAsset(View):
    def get(self, request, id):
        asset = Asset.objects.get(id=id)
        asset.delete()
        return redirect('listdata')



class UpdateData(View):
    def get(self, request, id):
        asset = Asset.objects.get(id=id)
        asset.aktif = False
        asset.save()
        return redirect ('listdata')
