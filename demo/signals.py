from django.dispatch import Signal
signalAllen=Signal(providing_args=['allen'])
def signal_callback(sender,**kwargs):
    print(sender,kwargs)
    print('signal_callback called')
def signal_callback1(sender,**kwargs):
    print(sender,kwargs)
    print('signal_callback called1')
signalAllen.connect(signal_callback)
signalAllen.connect(signal_callback1)