from CooolisGather.celery import app
from .tasks_handle.port_scan_handle import PortScanTask


@app.task(base=PortScanTask)
def hello_world():
    print('Hello World')

