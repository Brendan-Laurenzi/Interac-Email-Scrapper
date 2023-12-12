from PyQt6.QtCore import QRunnable, QObject, pyqtSignal, QSettings
import time
import scrape
import database

class WorkerSignals(QObject):
    progress = pyqtSignal(int, int)
    finished = pyqtSignal(int)
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)

class UpdateWorker(QRunnable):

    def __init__(self, condition=None):
        super(UpdateWorker, self).__init__()
        self.condition = condition
        self.emailUser = None
        self.emailPass = None
        self.db = database.Database()
        self.signals = WorkerSignals()

        self.settings = QSettings('NoOrg', 'EMTManager')
        try:
            self.emailUser = self.settings.value('email username')
            self.emailPass = self.settings.value('email password')
            self.email = scrape.emtEmail(self.emailUser, self.emailPass)
        except:
            print("Email Initialize Error")
            pass #Change this

    def run(self):
        self.db.connect()
        self.email.connect()
        beforeEntryCount = len(self.db.fetch_all('received_emts'))

        emailCount = self.email.get_email_count(self.condition)
        for i in range(emailCount):
            # Retreive ['name', 'amt', 'memo', 'date', 'refID'] from Interac Confirmation Email
            emailData = self.email.fetch_email_content(i)
            self.signals.progress.emit(i+1, emailCount)
            # Continue to next email if -1 (Email did not match Interac E-Transfer Format)
            if (emailData == -1): continue
            self.db.insert_record("received_emts", ['name', 'amt', 'memo', 'date', 'refID'], emailData)

        # Calculate how many new entries were added
        afterEntryCount = len(self.db.fetch_all('received_emts'))
        newEntryCount = afterEntryCount - beforeEntryCount

        self.email.disconnect()
        self.db.disconnect()
        self.signals.finished.emit(newEntryCount)


class ListenWorker(QRunnable):

    def __init__(self):
        super(ListenWorker, self).__init__()
        self.shouldStop = False
        self.emailUser = None
        self.emailPass = None
        self.signals = WorkerSignals()

        self.settings = QSettings('NoOrg', 'EMTManager')
        try:
            self.emailUser = self.settings.value('email username')
            self.emailPass = self.settings.value('email password')
            self.email = scrape.emtEmail(self.emailUser, self.emailPass)
        except:
            print("Email Initialize Error")
            pass #Change this


    def stop(self):
        print("ListenWorker received 'STOP' Signal")
        self.email.stop_email_idle()
        self.shouldStop = True

    def run(self):
        self.email.connect()
        while not self.shouldStop:
            result = self.email.check_for_new_emails()
            if self.shouldStop or result == -1: break
            self.signals.result.emit(result)
        self.email.disconnect()
        print("Listen Thread Complete")


class TimeWorker(QRunnable):

    def __init__(self):
        super(TimeWorker, self).__init__()
        self.shouldStop = False
        self.signals = WorkerSignals()

    def stop(self):
        print("TimeWorker received 'STOP' Signal")
        self.shouldStop = True

    def run(self):
        while not self.shouldStop:
            current_time = time.strftime("%I:%M %p", time.localtime())
            if self.shouldStop: break
            self.signals.result.emit(current_time)
            time.sleep(1)
        print("Time Thread Complete")