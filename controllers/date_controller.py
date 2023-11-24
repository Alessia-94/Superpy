from repository.date_repository import Time_repository #classe riempita statica

class Date_controller:
    time_repository = Time_repository()
    
    def get_current_date(self):
        self.time_repository.get_current_time()