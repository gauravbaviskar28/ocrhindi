from django.shortcuts import  redirect, render
from ocr.forms import OcrForm
from ocr.models import ocrmodel,ocrmodelcoord
from ocr.ocrcode import ocrfunc

def home(request):
    if request.method == 'POST':
        form=OcrForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            img=form.cleaned_data['img']
            newobj=ocrmodel.objects.create(img=img,desc='')
            lis=ocrfunc(newobj.img.path)
            newobj.desc=lis[-1]
            newobj.save()
            for item in lis[:len(lis)-1]:
                obj=ocrmodelcoord.objects.create(
                    ocrmodel1=newobj,
                    top=item[0][0][0],
                    left=item[0][0][1],
                    word=item[1]
                )
                obj.save()

            
            my_thing = {
                'img' : newobj.img.url,
                'desc': newobj.desc,
                'id':int(newobj.id),

            }
            #print(lis)
            request.session['my_thing'] = my_thing

            return redirect('output')
        else:
            pass
    else:
        form=OcrForm()
    context={
        'form' :form,
    }
    return render(request,'home.html',context)

def output(request):
    #newobjectid=None
    context = request.session.get('my_thing', None)
    return render(request,'output.html',context)

def gentemplate(request):
    #newobjectid=None
    context = request.session.get('my_thing', None)
    objs=ocrmodelcoord.objects.filter(ocrmodel1=ocrmodel.objects.get(id=context['id']))
    context['objs']=objs
    #print(context)
    return render(request,'gettemplate.html',context)