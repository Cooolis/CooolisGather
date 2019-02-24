from celery import Task


class PortScanTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print("Done")
        return super(PortScanTask, self).on_success(retval, task_id, args, kwargs)


