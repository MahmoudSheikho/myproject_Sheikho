from django.urls import path
from itinventory import views


urlpatterns = [
    path('', views.index, name='itinventory'),
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
    path('platz/', views.platzview, name='platz'),
    path('platzviewFilter/<int:id>', views.platzviewFliter, name='platzviewFilter'),
    path('platzviewFilterGesamt/', views.platzviewFilterGesamt, name='platzviewFilterGesamt'),
    path('platzviewFilterVerleih/<int:id>', views.platzviewFilterVerleih, name='platzviewFilterVerleih'),
    path('addplatz/', views.addplatz, name='addplatz'),
    path('addPlatzRaum/<int:id>', views.addPlatzRaum, name='addPlatzRaum'),
    path('addplatz/addplatzRecord/', views.addplatzRecord, name='addplatzRecord'),
    path('delplatz/<int:id>/<int:id_room>/', views.delplatz, name='delplatz'),

    path('updatePlatz/<int:id>', views.updatePlatz, name='updatePlatz'),
    path('updatePlatz/updatePlatzRecord/<int:id>',views.updatePlatzRecord, name='updatePlatzRecord'),

    #update PC Data
    path('updatePC/<int:id>', views.updatePC, name='updatePC'),
    path('updatePC/updatePCRecord/<int:id_pc>', views.updatePCRecord, name='updatePCRecord'),

    path('updatePlatzPC/<int:id>', views.updatePlatzPC, name='updatePlatzPC'),
    path('updatePlatzPC/updatePlatzPCRecord/<int:id>',views.updatePlatzPCRecord, name='updatePlatzPCRecord'),

    path('updatePlatzVerleih/<int:id>', views.updatePlatzVerleih, name='updatePlatzVerleih'),
    path('updatePlatzVerleih/updatePlatzVerleihRecord/<int:id>',views.updatePlatzVerleihRecord, name='updatePlatzVerleihRecord'),

    
    path('updatePlatzMonitor1/<int:id>', views.updatePlatzMonitor1, name='updatePlatzMonitor1'),
    path('updatePlatzMonitor1/updatePlatzMonitor1Record/<int:id>',views.updatePlatzMonitor1Record, name='updatePlatzMonitor1Record'),
    path('updatePlatzMonitor2/<int:id>', views.updatePlatzMonitor2, name='updatePlatzMonitor2'),
    path('updatePlatzMonitor2/updatePlatzMonitor2Record/<int:id>',views.updatePlatzMonitor2Record, name='updatePlatzMonitor2Record'),

    path('raum/', views.raumview, name='raum'),
    path('addraum/', views.addraum, name='addraum'),
    path('addraumRecord/', views.addraumRecord, name='addraumRecord'),
    path('delraum/<int:id>', views.delraum, name='delraum'),
    path('pc/', views.pcview, name='pc'),
    path('pcviewFilter/<int:id>', views.pcviewFilter, name='pcviewFilter'),
    path('addpc/', views.addpc, name='addpc'),
    path('addpc/addpcRecord/', views.addpcRecord, name='addpcRecord'),
    path('updatePc/<int:id>/<int:id_room>', views.updatePc, name='updatePc'),
    path('updatePc/updatePcRecord/<int:id_pc>/<int:id_room>',views.updatePcRecord, name='updatePcRecord'),
    path('delPc/<int:id>', views.delPc, name='delPc'),
    path('delPc/delPcRecord/<int:id>', views.delPcRecord, name='delPcRecord'),
    # del PC Record directly
    path('delPCRecord/<int:id>', views.delPCRecord, name='delPCRecord'),


    # Monitors
    path('monitors/', views.monitors, name='monitors'),
    path('monitor/', views.monitorview, name='monitor'),

    path('addMONITOR/', views.addMONITOR, name='addMONITOR'),
    path('addmonitor/addMONITORRecord/',views.addMONITORRecord, name='addMONITORRecord'),

    path('updateMONITOR/<int:id>', views.updateMONITOR, name='updateMONITOR'),
    path('updateMONITOR/updateMONITORRecord/<int:id>',views.updateMONITORRecord, name='updateMONITORRecord'),

    path('addmonitor/<int:id>', views.addmonitor, name='addmonitor'),

    path('addmonitor/addMonitorRecord/<int:id>',views.addMonitorRecord, name='addMonitorRecord'),
    path('monitorviewFilter/<int:id>',views.monitorviewFilter, name='monitorviewFilter'),

    path('updateMonitor/<int:id>/<int:id_room>/', views.updateMonitor, name='updateMonitor'),
    path('updateMonitor/updateMonitorRecord/<int:id>/<int:id_room>/',views.updateMonitorRecord, name='updateMonitorRecord'),
    path('delmonitor/<int:id>', views.delmonitor, name='delmonitor'),
    path('delMONITORRecord/<int:id>', views.delMONITORRecord, name='delMONITORRecord'),
    
    path('delmonitor/delMonitorRecord/<int:id>',views.delMonitorRecord, name='delMonitorRecord'),


    #pc Management
    path('pcs/', views.pcs, name='pcs'),

    # change Mouse/keyboard
    path('changeMouse/<int:id_platz>', views.changeMouse, name='changeMouse'),
    path('changeKeyboard/<int:id_platz>', views.changeKeyboard, name='changeKeyboard'),
]
