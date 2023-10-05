class Car():
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        self.status = 'STOPPED'
        self.speed = 0

    def start(self):
        if self.status == 'STOPPED':
            self.status = 'STARTED'
            self.speed = 10

    def stop(self):
        if self.status != 'STOPPED':
            self.status = 'STOPPED'
            self.speed = 0

    def speedup(self, speed):
        if self.status == 'STOPPED':
            self.start()
        self.speed += speed
        self.status = 'RUNNING'

    def slowdown(self, speed):
        if self.status != 'STOPPED':
            self.speed -= speed
            if self.speed <= 0:
                self.stop()

    def get_status(self):
        return f"Car is {self.status}, speed={self.speed}"

if __name__ == "__main__":
    c = Car('i20', 'Hyundai')
    print(c.get_status())

