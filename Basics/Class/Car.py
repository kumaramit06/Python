class Car :
    def __init__(self) -> None:
        self._brand= None
        self._model= None
        self._year = None
    
    def set_brand(self,brand: str)-> None:
        self._brand=brand
    
    def get_brand(self)->str:
        return self._brand
    
    def set_model(self,model: str)-> None:
        self._model=model
        
    def get_model(self)-> str:
        return self._model
    
    def set_year(self,year)-> None:
        self._year=year
    
    def get_year(self)->str:
        return self._year