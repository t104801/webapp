# zuteilungen/views.py
# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView
from django.db.models import Count, Max
from .models import ZuBaseFilNr, ZuBaseFilNrDet, ZuBaseWabe, ZuBaseWabeKat, MyUtil, EIGENSCHAFT_CHOICES
from .forms import NewEffdt, FilialForm, WabeForm
from datetime import datetime
from queryset_sequence import QuerySetSequence


# Create your views here.

class ZuBaseFilNrList(FormView, TemplateView):

    template_name = 'zuteilung/filialen/filialen.html'
    form_class = NewEffdt
    initial = {'effdt': datetime.now().strftime('%d') + '.' + datetime.now().strftime('%m') + '.' + str(datetime.now().year)}
    success_url = "/zuteilung/"

    def datum(self,**kwargs):
        datum = ''
        if 'year' in kwargs:
            datum = kwargs['year'] + '-' + kwargs['month'] + '-' + kwargs['day']
        else:
            datum = ZuBaseFilNrDet.objects.values('effdt').annotate(max=Max('effdt')).latest('effdt')['effdt']
        return datum

    def filialen(self, **kwargs):
        return QuerySetSequence(ZuBaseFilNr.objects.all(), ZuBaseFilNrDet.objects.all(), ZuBaseWabeKat.objects.all()).filter(**{'#': 1, 'effdt': self.datum()}).order_by('filiale__lanr')

    def datis(self, **kwargs):
        effdt = []

        for i in ZuBaseFilNrDet.objects.values('effdt').annotate(dcount=Count('effdt')).order_by('-effdt'):
            if 'year' in kwargs and 'month' in kwargs and 'day' in kwargs:
                if kwargs['year'] == str(i['effdt'].year) and kwargs['month'] == str(i['effdt'].strftime('%m')) and \
                                kwargs['day'] == str(i['effdt'].strftime('%d')):
                    effdt += [{'effdt': i['effdt'], 'year': i['effdt'].year, 'month': i['effdt'].strftime('%m'),
                               'day': i['effdt'].strftime('%d'), 'aktiv': True}]
                else:
                    effdt += [{'effdt': i['effdt'], 'year': i['effdt'].year, 'month': i['effdt'].strftime('%m'),
                               'day': i['effdt'].strftime('%d'), 'aktiv': False}]
            else:
                if i['effdt'] == self.datum():
                    effdt += [{'effdt': i['effdt'], 'year': i['effdt'].year, 'month': i['effdt'].strftime('%m'),
                               'day': i['effdt'].strftime('%d'), 'aktiv': True}]
                else:
                    effdt += [{'effdt': i['effdt'], 'year': i['effdt'].year, 'month': i['effdt'].strftime('%m'),
                               'day': i['effdt'].strftime('%d'), 'aktiv': False}]
        return effdt

    def wabe(self):
        return ZuBaseWabe.objects.all().order_by("wabe")

    def get_context_data(self, **kwargs):
        context = super(ZuBaseFilNrList, self).get_context_data(**kwargs)

        context['datis'] = self.datis()
        context['filialen']=self.filialen()
        context['wabe'] =  self.wabe() #ZuBaseWabe.objects.all().order_by("wabe")
        context['form'] = NewEffdt()
        context['eigenschaft'] = EIGENSCHAFT_CHOICES
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # ZuBaseFilNrDet replizieren mit neuem Effdt

        max_effdt = ZuBaseFilNrDet.objects.filter(effdt__lte = form.cleaned_data['effdt']).aggregate(Max('effdt'))['effdt__max']

        my_util = MyUtil()
        zubasefilnrdet = ZuBaseFilNrDet.objects.filter(effdt=max_effdt).select_related()
        for object in zubasefilnrdet:
            obj_id = object.id
            object.id = None
            object.effdt = form.cleaned_data['effdt']
            object.umsatz = my_util.getfilialumsatz(form.cleaned_data['effdt'].strftime('%Y'), object.filiale.mandant,
                                             object.filiale.lanr)
            object.save()

            # ZuBaseWabeKat  replizieren in Abhängikeit zu ZuBaseFilNrDet
            for zubasewabekat in ZuBaseWabeKat.objects.filter(filiale=obj_id):
                zubasewabekat.id = None
                zubasewabekat.umsatz = my_util.getfilialumsatzwabe(form.cleaned_data['effdt'].strftime('%Y'),
                                                                   object.filiale.mandant, object.filiale.lanr,
                                                                   zubasewabekat.wabe.wabe)
                zubasewabekat.filiale = object
                zubasewabekat.save()

                # form.send_email()
        return super(ZuBaseFilNrList, self).form_valid(form)
        #return super(NewEffdt, self).form_valid(neweffdtform)
