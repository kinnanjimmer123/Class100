class Car: 
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model

    def start(self):
        print("started")

    def stop(self):
        print('stopped')

    def accelarate(self):
        print("accelarating")
 
    def headlights(self):
        print("lights on")

audi = Car("a6","red","audi",100)
print(audi.start())