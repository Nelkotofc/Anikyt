from __init__ import *


class SettingsPage(QMainWindow):
    def __init__(self, manager):
        super(SettingsPage, self).__init__()

        self.manager = manager

        self.centralArea = QWidget()
        self.setCentralWidget(self.centralArea)

        self.options = { # Checked Var, Unchecked Var
            'Dark Mode': ["black", "white", 'DisplayColor'],
            'Grid Display': ["grid", "list", "DisplayModel"],
            'Adult Medias': [True, False],
            'English Titles': [False, True, "romaji"],
            'Large Icons': ["large", 'small', 'ModelSize']
        }

        self.loadSettings()

        self.manager.application(self)
        self.manager.defaultSwitchBar(self, self.centralArea)

    def getOptionName(self, option):
        return option.replace(" ", "") if len(self.options.get(option)) == 2 else self.options.get(option)[2]

    def nextValue(self, option):
        return self.options.get(option)[1] if self.manager.option(self.getOptionName(option)) == self.options.get(option)[0] else self.options.get(option)[0]

    def checkEvent(self):
        self.manager.setOption(self.getOptionName(self.sender().text()), self.nextValue(self.sender().text()))

    def getCheckBool(self, option):
        return True if self.manager.option(self.getOptionName(option)) == self.options.get(option)[
                0] else False
    def loadSettings(self):
        y = 0
        for option in self.options:
            checkBox = QCheckBox(option, self.centralArea)
            checkBox.setStyleSheet("font-size: 20px;")
            checkBox.setChecked(self.getCheckBool(option))
            checkBox.stateChanged.connect(self.checkEvent)
            checkBox.setGeometry(10, y, self.width(), 100)
            y += checkBox.height()

        loginBtn = QPushButton("Login", self.centralArea)
        loginBtn.setStyleSheet("font-size: 20px; font-weight: bold;")
        width = 300
        height = 50
        loginBtn.setGeometry(self.width()-width/2, self.height()-height/2, width, height)
        loginBtn.clicked.connect(self.manager.loginPageSwitch)



