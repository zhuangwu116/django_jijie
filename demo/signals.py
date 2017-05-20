from django.dispatch import Signal,receiver
signalAllen=Signal(providing_args=['allen'])
@receiver(signalAllen)
def signal_callback(sender,**kwargs):
    print(sender,kwargs)
    print('signal_callback called')
@receiver(signalAllen)
def signal_callback1(sender,**kwargs):
    print(sender,kwargs)
    print('signal_callback called1')