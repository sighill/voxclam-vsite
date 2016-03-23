from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import Group , Equipment
from django.template import loader
from .battleEngineCore import performBattle
from .forms import chooseBattle


# Create your views here.
'''
def battle(request):
    groupList = Group.objects.all()
    equipmentList = Equipment.objects.all()
    battleLogFinal = performBattle(Group.objects.get(pk=1) , Group.objects.get(pk=2) )
    template = loader.get_template('battleindex.html')
    context = {'groupList':groupList,'equipmentList':equipmentList,'battleLogFinal':battleLogFinal,}
    return HttpResponse(template.render(context, request))
'''
'''
def battleIndex(request):
    groupList = Group.objects.all()
    if request.method == 'POST':
        form = Group(request.POST)
        if form.is_valid():
            # Add data check but HOW YOU RETARDED TUTORIAL
            return HttpResponseRedirect('/thanks/')
        else:
            form = Group()
    template = loader.get_template('battleindex.html')
    context = {'groupList':groupList,}
    return HttpResponse(template.render(context , request ))
'''

# function called for URL /battle/select/
def battleSelect(request):
    if request.method == 'POST':
        # in case of POST, retreive GIDA and GIDB from POST...
        GIDA = request.POST[ 'GIDA' ]
        GIDB = request.POST[ 'GIDB' ]
        # ...and redirect to /battle/execute/GIDA/GIDB
        return HttpResponseRedirect( '/battle/execute/{}/{}'.format( GIDA, GIDB ) )
    else:
        # Else (first display of the page), display page for selection
        groupList = Group.objects.all()
        template = loader.get_template('battleindex.html')
        context = {'groupList':groupList,}
        return HttpResponse(template.render(context , request ))

# function called for URL /battle/execute/GIDA/GIDB/
def battleExecute(request , GIDA , GIDB ):
    groupList = Group.objects.all()
    equipmentList = Equipment.objects.all()
    battleLogFinal = performBattle(Group.objects.get(pk=GIDA) , Group.objects.get(pk=GIDB) )
    template = loader.get_template('battle.html')
    context = {'groupList':groupList,'equipmentList':equipmentList,'battleLogFinal':battleLogFinal,}
    return HttpResponse(template.render(context, request))
