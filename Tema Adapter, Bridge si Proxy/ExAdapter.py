# Adaptee
class EuropeanSocketInterface:
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target
class USASocketInterface:
    def voltage(self):
        return 120

    def live(self):
        return 1

    def neutral(self):
        return -1


# Adapter
class EuropeanToUSASocketAdapter(USASocketInterface):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def voltage(self):
        return 120

    def live(self):
        return self.adaptee.live()

    def neutral(self):
        return self.adaptee.neutral()


# Client
def main():
    socket = USASocketInterface()
    print("USA Socket Interface:")
    print(f"Voltage: {socket.voltage()}V, Live: {socket.live()}, Neutral: {socket.neutral()}")

    print("\nAdapting European Socket Interface to USA:")
    european_socket = EuropeanSocketInterface()
    adapter = EuropeanToUSASocketAdapter(european_socket)
    print(f"Voltage: {adapter.voltage()}V, Live: {adapter.live()}, Neutral: {adapter.neutral()}")


if __name__ == '__main__':
    main()
