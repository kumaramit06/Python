from Car import Car
class Sedan(Car):
    def __init__(self) -> None:
        super().__init__()
        self.open_truck="yes"
    
    def __get_open_truck(self)->str:
        print('Open truck')
        return self.open_truck;
    
    def open_trunk(self)->str:
       return self.__get_open_truck()
        
        
        
    