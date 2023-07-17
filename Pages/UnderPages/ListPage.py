from __init__ import *

class ListPage(QWidget):
    def __init__(self, mainWindow, manager):
        self.mainWindow = mainWindow
        self.manager = manager
        super(ListPage, self).__init__()

    def onload_image(self, QIB, image_width, image_height):
        QIB.setFixedSize(QSize(image_width, image_height))



    def create(self, media, layout):
        # Same code as before...
        row_layout = QHBoxLayout()
        image_button = QImageButton(media, media.coverImage["large"], divider=4, loaded=self.onload_image) # size=(None, 600 if self.manager.option("ModelSize") == "large" else 200)
        name_label = QLabel(media.getTitle(self.manager.option("romaji")))
        row_layout.addWidget(image_button)
        row_layout.addWidget(name_label)
        layout.addLayout(row_layout)

        # Create the second row with additional buttons and information
        row_layout = QHBoxLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        information_label = QLabel("Some more information")
        row_layout.addWidget(button1)
        row_layout.addWidget(button2)
        row_layout.addWidget(information_label)
        layout.addLayout(row_layout)


    def initUI(self, medias=None):

        medias: list[AniMedia]

        if medias is None:
            quit("There are no medias")

        main_layout = QHBoxLayout()

        # Create the layout for the buttons and information
        buttons_layout = QVBoxLayout()

        for media in list(medias):  # 5 is the number of animes
            self.create(media, buttons_layout)



        # Create the second row with additional buttons and information
        row_layout = QHBoxLayout()
        row_layout.addWidget(QLabel())
        buttons_layout.addLayout(row_layout)

        # Create the scroll area to enable vertical scrolling
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a container widget for the anime information
        anime_container = QWidget()
        anime_container_layout = QVBoxLayout()
        anime_container_layout.addLayout(buttons_layout)
        anime_container.setLayout(anime_container_layout)
        scroll_area.setWidget(anime_container)

        main_layout.addWidget(scroll_area)

        # Create the vertical slider for navigation (on the right)
        slider = QSlider(Qt.Vertical)
        slider.setRange(0, buttons_layout.count() - 1)
        slider.valueChanged.connect(self.onSliderValueChanged)
        main_layout.addWidget(slider)

        self.setLayout(main_layout)

    def onSliderValueChanged(self, value):
        # Show the corresponding row based on the slider value
        buttons_layout = self.layout().itemAt(0).widget().layout()
        for index in range(buttons_layout.count()):
            buttons_layout.itemAt(index).layout().setEnabled(index == value)
