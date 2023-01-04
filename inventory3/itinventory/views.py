from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Monitor, Platz, Rooms, Pcs
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('itinventory'))


@login_required
def index(request):
    myrooms = Rooms.objects.filter().exclude(id=11).values()
    template = loader.get_template('index.html')
    context = {
        'myrooms': myrooms,
    }
    return HttpResponse(template.render(context, request))


def raumview(request):
    template = loader.get_template('raum.html')
    return HttpResponse(template.render({}, request))


def addraum(request):
    template = loader.get_template('addraum.html')
    return HttpResponse(template.render({}, request))


def addraumRecord(request):

    addraumRecord_roomname = request.POST['roomname']
    addraumRecord_anzahlplaetze = request.POST['anzahlplaetze']
    myroom = Rooms(roomname=addraumRecord_roomname,
                   anzahlplaetze=addraumRecord_anzahlplaetze,
                   )
    myroom.save()

    return HttpResponseRedirect(reverse('itinventory'))


def delraum(request, id):
    myroom = Rooms.objects.get(id=id)
    myroom.delete()
    return HttpResponseRedirect(reverse('itinventory', request))


def platzview(request):
    template = loader.get_template('platz.html')
    return HttpResponse(template.render({}, request))


@login_required
def platzview(request):
    myplaetze = Platz.objects.all().values()
    template = loader.get_template('platz.html')
    context = {
        'myplaetze': myplaetze,
    }
    return HttpResponse(template.render(context, request))


def platzviewFliter(request, id):
    myplaetze = Platz.objects.filter(room_id=id)
    mypcs = Pcs.objects.filter(id=id)
    myrooms = Rooms.objects.get(id=id)

    template = loader.get_template('platz.html')
    context = {
        'myplaetze': myplaetze,
        'myrooms': myrooms,
        'mypcs': mypcs,
    }
    return HttpResponse(template.render(context, request))


def platzviewFilterGesamt(request):
    myplaetze = Platz.objects.filter().select_related()
    template = loader.get_template('platzAll.html')
    context = {
        'myplaetze': myplaetze,
    }
    return HttpResponse(template.render(context, request))


def platzviewFilterVerleih(request, id):
    myplaetze = Platz.objects.filter(room_id=id)
    mypcs = Pcs.objects.filter(id=id)
    myrooms = Rooms.objects.get(id=id)

    template = loader.get_template('platzVerleih.html')
    context = {
        'myplaetze': myplaetze,
        'myrooms': myrooms,
        'mypcs': mypcs,
    }
    return HttpResponse(template.render(context, request))



def addplatz(RequestContext):
    mypcs = Pcs.objects.all().values()
    myrooms = Rooms.objects.all().values()
    mymonitors = Monitor.objects.all().values()
    template = loader.get_template('addplatz.html')
    context = {
        'mypcs': mypcs,
        'mymonitors': mymonitors,
        'myrooms': myrooms
    }
    return HttpResponse(template.render(context, RequestContext))


def addPlatzRaum(Request, id):
    MaxAnzahl = Rooms.objects.get(id=id).anzahlplaetze
    myPlace = Platz.objects.filter(room_id=id)
    mypcs = Pcs.objects.all().values()
    myrooms = Rooms.objects.all().values()
    myRoom = Rooms.objects.get(id=id) 
    mymonitors = Monitor.objects.all().values().order_by('serialnummer')
    template = loader.get_template('addplatz.html')
    if myPlace.count() < MaxAnzahl:
        context = {
            'mypcs': mypcs,
            'mymonitors': mymonitors,
            'myrooms': myrooms,
            'myRoom': myRoom,
            'id': id,
        }
        return HttpResponse(template.render(context, Request))
    else:
        # Meldung fehlt
        return HttpResponseRedirect(reverse('platzviewFilter', args=[id]))        



def addplatzRecord(request):
    addplatzRecord_bezeichnung = request.POST['bezeichnung']
    addplatzRecord_room = request.POST['room']
    #addplatzRecord_room = request.POST['room']
    #addplatzRecord_pc = request.POST['pc']
    #addplatzRecord_monitor1 = request.POST['monitor1']
    #addplatzRecord_monitor2 = request.POST['monitor2']
    #addplatzRecord_maus = request.POST['maus']
    #addplatzRecord_tastatur = request.POST['tastator']

    myplaetze = Platz(
                    bezeichnung=addplatzRecord_bezeichnung,
                    room_id=addplatzRecord_room
     #                 pc_id=addplatzRecord_pc,
      #                monitor1_id=addplatzRecord_monitor1,
       #               monitor2_id=addplatzRecord_monitor2,
    #              maus=addplatzRecord_maus,
     #                 tastatur=addplatzRecord_tastatur,

                      )
    myplaetze.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[addplatzRecord_room]))


def updatePlatz(request, id):
    myplaetze = Platz.objects.get(id=id)

    mypcs = Pcs.objects.filter().exclude(id=myplaetze.pc_id).values()
    mymonitors1 = Monitor.objects.filter().exclude(id=myplaetze.monitor1_id).values()
    mymonitors2 = Monitor.objects.filter().exclude(id=myplaetze.monitor2_id).values()

    template = loader.get_template('updateplatz.html')
    context = {
        'myplaetze': myplaetze,
        'mypcs': mypcs,
        'mymonitors1': mymonitors1,
        'mymonitors2': mymonitors2,
    }
    return HttpResponse(template.render(context, request))
    
def updatePlatzRecord(request, id):
    updatePcRecord_bezeichnung = request.POST['bezeichnung']
    updatePcRecord_room = request.POST['room']
    updatePcRecord_pc = request.POST['pc']
    updatePcRecord_monitor1 = request.POST['monitor1']
    updatePcRecord_monitor2 = request.POST['monitor2']
    updatePcRecord_maus = request.POST['maus']
    updatePcRecord_tastator = request.POST['tastator']

    myplaetze = Platz.objects.get(id=id)
    myplaetze.bezeichnung = updatePcRecord_bezeichnung
    myplaetze.room_id = updatePcRecord_room
    myplaetze.pc_id = updatePcRecord_pc
    myplaetze.monitor1_id = updatePcRecord_monitor1
    myplaetze.monitor2_id = updatePcRecord_monitor2
    myplaetze.maus = updatePcRecord_maus
    myplaetze.tastator = updatePcRecord_tastator

    myplaetze.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[updatePcRecord_room]))



def updatePC(request, id):
    myplaetze = Platz.objects.get(id=id)
    mypcs = Pcs.objects.filter().exclude(id=myplaetze.pc_id).values()
    template = loader.get_template('updatePC.html')
    context = {
        'myplaetze': myplaetze,
        'mypcs': mypcs,

    }
    return HttpResponse(template.render(context, request))
def updatePlatzPC(request, id):
    myplaetze = Platz.objects.get(id=id)
    mypcs = Pcs.objects.filter().exclude(id=myplaetze.pc_id).values()


    template = loader.get_template('updateplatzpc.html')
    context = {
        'myplaetze': myplaetze,
        'mypcs': mypcs,

    }
    return HttpResponse(template.render(context, request))
def updatePlatzPCRecord(request, id):

    updatePcRecord_pc = request.POST['pc']
    updatePcRecord_room = request.POST['room']


    myplaetze = Platz.objects.get(id=id)
    myplaetze.pc_id = updatePcRecord_pc
    myplaetze.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[updatePcRecord_room]))


def delplatz(request, id, id_room):
    myplatz = Platz.objects.get(id=id)
    myplatz.delete()
    return HttpResponseRedirect(reverse('platzviewFilter', args=[id_room]))

def updatePlatzMonitor1(request, id):
    myplaetze = Platz.objects.get(id=id)
    #mymonitors1 = Monitor.objects.filter().exclude(id=myplaetze.monitor1_id).values()
    mymonitors1 = Monitor.objects.get(id=myplaetze.monitor1_id)


    template = loader.get_template('updateplatzmonitor1.html')
    context = {
        'myplaetze': myplaetze,
        'mymonitors1': mymonitors1,
    }
    return HttpResponse(template.render(context, request))

def updatePlatzMonitor1Record(request, id):
    updatePcRecord_room = request.POST['room']
    # updatePcRecord_monitor1 = request.POST['monitor1']
    updatePcRecord_schnittstelle = request.POST['schnittstelle']
    updatePcRecord_serialnummer = request.POST['serialnummer']
    updatePcRecord_bemaerkung = request.POST['bemaerkung']
    updatePcRecord_status = request.POST['status']



    myplaetze = Platz.objects.get(id=id)
    myMonitor = Monitor.objects.get(id=myplaetze.monitor1_id )

    myMonitor.schnittstelle = updatePcRecord_schnittstelle
    myMonitor.serialnummer = updatePcRecord_serialnummer
    myMonitor.bemaerkung = updatePcRecord_bemaerkung
    myMonitor.status = updatePcRecord_status
    myMonitor.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[updatePcRecord_room]))

def updatePlatzMonitor2(request, id):
    myplaetze = Platz.objects.get(id=id)

    mypcs = Pcs.objects.filter().exclude(id=myplaetze.pc_id).values()
    mymonitors1 = Monitor.objects.filter().exclude(id=myplaetze.monitor1_id).values()
    mymonitors2 = Monitor.objects.filter().exclude(id=myplaetze.monitor2_id).values()

    template = loader.get_template('updateplatzmonitor2.html')
    context = {
        'myplaetze': myplaetze,
        'mypcs': mypcs,
        'mymonitors1': mymonitors1,
        'mymonitors2': mymonitors2,
    }
    return HttpResponse(template.render(context, request))
def updatePlatzMonitor2Record(request, id):
    updatePcRecord_room = request.POST['room']
    updatePcRecord_monitor2 = request.POST['monitor2']


    myplaetze = Platz.objects.get(id=id)
    myplaetze.monitor2_id = updatePcRecord_monitor2
    myplaetze.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[updatePcRecord_room]))


@login_required
def pcview(request):
    mypcs = Pcs.objects.all().values()
    template = loader.get_template('pc.html')
    context = {
        'mypcs': mypcs,
    }
    return HttpResponse(template.render(context, request))

def pcs(request):
    mypcs = Pcs.objects.all().values()
    template = loader.get_template('pcs.html')
    context = {
        'mypcs': mypcs,
    }
    return HttpResponse(template.render(context, request))


@login_required
def pcviewFilter(request, id):
    mypcs = Pcs.objects.filter(id=id)
    myplaetze = Platz.objects.get(id=id)
    template = loader.get_template('pc.html')
    context = {
        'mypcs': mypcs,
        'myplaetze': myplaetze
    }
    return HttpResponse(template.render(context, request))


def updatePc(request, id, id_room):
    #if request == post
    mypcs = Pcs.objects.get(id=id)
    myFreePlatz = Platz.objects.all().select_related('room').filter(pc_id__isnull=True)
    template = loader.get_template('updatePc.html')
    context = {
        'mypcs': mypcs,
        'id_room': id_room,
        'myFreePlatz': myFreePlatz,
    }
    return HttpResponse(template.render(context, request))


def updatePcRecord(request, id_pc, id_room):
    if 'save' in request.POST:
        # add the user email in database
        #updatePcRecord_id = request.POST['id']
        updatePcRecord_modell = request.POST['modell']
        updatePcRecord_RAM = request.POST['RAM']
        updatePcRecord_CPU = request.POST['CPU']
        updatePcRecord_anzahlkerne = request.POST['anzahlkerne']
        updatePcRecord_festplatte = request.POST['festplatte']
        # updatePcRecord_pc = request.POST['pc']
        updatePcRecord_serialnummer = request.POST['serialnummer']

        mypcs = Pcs.objects.get(id=id_pc)
        # mypcs.id = updatePcRecord_id
        mypcs.modell = updatePcRecord_modell
        mypcs.RAM = updatePcRecord_RAM
        mypcs.CPU = updatePcRecord_CPU
        mypcs.anzahlkerne = updatePcRecord_anzahlkerne
        mypcs.festplatte = updatePcRecord_festplatte
        # mypcs.pc = updatePcRecord_pc
        mypcs.serialnummer = updatePcRecord_serialnummer
        mypcs.save()

        return HttpResponseRedirect(reverse('platzviewFilter', args=[id_room]))
    if 'movePc' in request.POST:
        # remove the user email from database
        id_platz = request.POST['id_platz']
        # Neuen Pc dem Platz hinzufügen
        myFreePlatz = Platz.objects.get(id=id_platz)
        myFreePlatz.pc_id = id_pc
        myFreePlatz.save()
        return HttpResponseRedirect(reverse('platzviewFilter', args=[id_room]))


def addpc(RequestContext):
    mypcs = Pcs.objects.all().values()
    myFreePlatz = Platz.objects.all().select_related('room').filter(pc_id__isnull=True)
    template = loader.get_template('addpc.html')
    context = {
        'mypcs': mypcs,
        'id': id,
        'myFreePlatz': myFreePlatz,
    }
    return HttpResponse(template.render(context, RequestContext))


def addpcRecord(request):
    addpcRecord_modell = request.POST['modell']
    addpcRecord_RAM = request.POST['RAM']
    addpcRecord_CPU = request.POST['CPU']
    addpcRecord_anzahlkerne = request.POST['anzahlkerne']
    addpcRecord_festplatte = request.POST['festplatte']
    id_platz = request.POST['id_platz']
    # addpcRecord_monitor1 = request.POST['monitor1']
    # addpcRecord_monitor2 = request.POST['monitor2']

    mypcs = Pcs(
        modell=addpcRecord_modell,
        RAM=addpcRecord_RAM,
        CPU=addpcRecord_CPU,
        anzahlkerne=addpcRecord_anzahlkerne,
        festplatte=addpcRecord_festplatte,
        # pc=addpcRecord_pc,
        # monitor1=addpcRecord_monitor1,
        # monitor2=addpcRecord_monitor2
    )
    mypcs.save()

    # Neuen Pc dem Platz hinzufügen
    myFreePlatz = Platz.objects.get(id=id_platz)
    myFreePlatz.pc_id = mypcs.id
    myFreePlatz.save()

    return HttpResponseRedirect(reverse('pcs'))








def delPc(RequestContext, id):

    mypcs = Pcs.objects.all().values()

    template = loader.get_template('delpc.html')
    context = {
        'mypcs': mypcs,
        'id': id,
    }
    return HttpResponse(template.render(context, RequestContext))


def delPcRecord(request, id):
    delPcRecord_pc = request.POST['pc']

    mypcs = Pcs.objects.get(id=delPcRecord_pc)
    mypcs.delete()

    return HttpResponseRedirect(reverse('updatePlatz', args=[id]))


@login_required
def monitorview(request):
    mymonitors = Monitor.objects.all().values()
    template = loader.get_template('monitor.html')
    context = {
        'mymonitors': mymonitors
    }
    return HttpResponse(template.render(context, request))


@login_required
def monitorviewFilter(request, id):
    mymonitors = Monitor.objects.filter(id=id)
    mypcs = Pcs.objects.get(id=id)
    template = loader.get_template('monitor.html')
    context = {
        'mymonitors': mymonitors,
        'mypcs': mypcs
    }
    return HttpResponse(template.render(context, request))


def updateMonitor(request, id, id_room):
    mymonitors = Monitor.objects.get(id=id)
    mypcs = Pcs.objects.get(id=id)
    template = loader.get_template('updatemonitor.html')
    context = {
        'mymonitors': mymonitors,
        'mypcs': mypcs,
        'id_room': id_room,
    }
    return HttpResponse(template.render(context, request))


def updateMonitorRecord(request, id, id_room):
    #updateMonitorRecord_id = request.POST['id']
    updateMonitorRecord_schnittstelle = request.POST['schnittstelle']
    updateMonitorRecord_serialnummer = request.POST['serialnummer']

    mymonitors = Monitor.objects.get(id=id)
    #mymonitors.id = updateMonitorRecord_id
    mymonitors.schnittstelle = updateMonitorRecord_schnittstelle
    mymonitors.serialnummer = updateMonitorRecord_serialnummer

    mymonitors.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[id_room]))


def addmonitor(RequestContext, id):
    mymonitors = Monitor.objects.all().values()

    template = loader.get_template('addmonitor.html')
    context = {
        'mymonitors': mymonitors,
        'id': id,
    }
    return HttpResponse(template.render(context, RequestContext))


def addMonitorRecord(request, id):
    addMonitorRecord_schnittstelle = request.POST['schnittstelle']
    addMonitorRecord_serialnummer = request.POST['serialnummer']
    addMonitorRecord_bemaerkung = request.POST['bemaerkung']
    addMonitorRecord_status = request.POST['status']

    myMonitor = Monitor(
        schnittstelle=addMonitorRecord_schnittstelle,
        serialnummer=addMonitorRecord_serialnummer,
        bemaerkung=addMonitorRecord_bemaerkung,
        status=addMonitorRecord_status,

    )

    myMonitor.save()

    return HttpResponseRedirect(reverse('platzviewFilter', args=[id]))

def delPc(RequestContext, id):
    mypcs = Pcs.objects.all().values()

    template = loader.get_template('delpc.html')
    context = {
        'mypcs': mypcs,
        'id': id,
    }
    return HttpResponse(template.render(context, RequestContext))


def delPcRecord(request, id):
    delPcRecord_pc = request.POST['pc']

    mypcs = Pcs.objects.get(id=delPcRecord_pc)
    mypcs.delete()

    return HttpResponseRedirect(reverse('updatePlatz', args=[id]))


def delmonitor(RequestContext, id):
    mymonitors = Monitor.objects.all().values()

    template = loader.get_template('delmonitor.html')
    context = {
        'mymonitors': mymonitors,
        'id': id,
    }
    return HttpResponse(template.render(context, RequestContext))


def delMonitorRecord(request, id):
    delMonitorRecord = request.POST['monitor']

    mymonitor = Monitor.objects.get(id=delMonitorRecord)
    mymonitor.delete()

    return HttpResponseRedirect(reverse('updatePlatz', args=[id]))



def updatePlatzVerleih(request, id):
    myplaetze = Platz.objects.get(id=id)

    mypcs = Pcs.objects.filter().exclude(id=myplaetze.pc_id).values()
    mymonitors1 = Monitor.objects.filter().exclude(id=myplaetze.monitor1_id).values()
    mymonitors2 = Monitor.objects.filter().exclude(id=myplaetze.monitor2_id).values()

    template = loader.get_template('updateplatzverleih.html')
    context = {
        'myplaetze': myplaetze,
        'mypcs': mypcs,
        'mymonitors1': mymonitors1,
        'mymonitors2': mymonitors2,
    }
    return HttpResponse(template.render(context, request))
def updatePlatzVerleihRecord(request, id):
    updatePcRecord_room = int(request.POST['room'])
    updatePcRecord_pc = int(request.POST['pc'])
    updatePcRecord_monitor1 = int(request.POST['monitor1'])
    updatePcRecord_monitor2 = int(request.POST['monitor2'])
    updatePcRecord_bemaerkung = request.POST['bemaerkung']

    myplaetze = Platz.objects.get(id=id)
    myplaetze.room_id = updatePcRecord_room
    myplaetze.pc_id = updatePcRecord_pc
    myplaetze.monitor1_id = updatePcRecord_monitor1
    myplaetze.monitor2_id = updatePcRecord_monitor2
    myplaetze.bemaerkung = updatePcRecord_bemaerkung

    myplaetze.save()

    return HttpResponseRedirect(reverse('platzviewFilterVerleih', args=[updatePcRecord_room]))