class Computer:
    def __init__(self,
                 case="Coolermaster N300",
                 mainboard="MSI 970",
                 cpu="Intel Core i7-4770",
                 memory="Corsair 16GB",
                 hardDrive="Seagate 1TB",
                 videoCard="GeForce GTX 1070"):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hardDrive = hardDrive
        self.videoCard = videoCard

    def display(self):
        print(F"CASE --> {self.case}")
        print(F"MAIN BOARD --> {self.mainboard}")
        print(F"CPU --> {self.cpu}")
        print(F"MEMORY --> {self.memory}")
        print(F"HARD DRIVE --> {self.hardDrive}")
        print(F"VIDEO CARD --> {self.videoCard}")
