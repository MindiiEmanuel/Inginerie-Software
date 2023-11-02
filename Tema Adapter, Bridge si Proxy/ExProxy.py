# Clasa Subiect

class Subject:
    def request(self):
        pass


# Clasa RealSubject

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Trimitere cerere.")


# Clasa Proxy

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Verificare acces înainte de trimitere cerere.")
        return True

    def log_access(self):
        print("Proxy: Jurnalizare acces la cerere.")


# Utilizarea Proxy

def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    # Trimitere cerere prin proxy
    proxy.request()


if __name__ == '__main__':
    main()
