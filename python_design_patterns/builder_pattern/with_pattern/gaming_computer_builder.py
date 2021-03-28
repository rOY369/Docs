from abstract_builder import AbstractBuilder


class GamingComputerBuilder(AbstractBuilder):
    def get_case(self):
        self._computer.case = "Coolermaster N300"

    def build_mainboard(self):
        self._computer.mainboard = "MSI 970"
        self._computer.cpu = "Intel Core i7-4770"
        self._computer.memory = "Corsair 16GB"

    def install_mainboard(self):
        print("MAIN BOARD INSTALLED")

    def install_hard_drive(self):
        self._computer.hardDrive = "Seagate 1TB"

    def install_video_card(self):
        self._computer.videoCard = "GeForce GTX 1070"
