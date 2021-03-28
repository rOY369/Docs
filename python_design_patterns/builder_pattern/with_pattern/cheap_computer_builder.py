from abstract_builder import AbstractBuilder


class CheapComputerBuilder(AbstractBuilder):
    def get_case(self):
        self._computer.case = "IN WIN BP655"

    def build_mainboard(self):
        self._computer.mainboard = "ASRock AM1H-ITX"
        self._computer.cpu = "AMD Athlon 5150"
        self._computer.memory = "Kingston ValueRAM 4GB"

    def install_mainboard(self):
        print("MAIN BOARD INSTALLED")

    def install_hard_drive(self):
        self._computer.hardDrive = "Seagate 500 GB"

    def install_video_card(self):
        self._computer.videoCard = "On Board"
