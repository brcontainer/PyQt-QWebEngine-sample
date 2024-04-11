# -*- coding: utf-8 -*-

from PyQt6.QtWebEngineWidgets import QWebEngineView

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStatusBar,
    QGridLayout,
    QWidget
)

from PyQt6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QUrl
)


class MainWindow(object):
    def setupUi(self, main):
        main.setObjectName("MainWindow")
        main.resize(800, 600)

        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        webView = QWebEngineView(self.centralwidget)
        webView.setUrl(QUrl("https://github.com/brcontainer/"))
        webView.setObjectName("webView")

        self.gridLayout.addWidget(webView, 0, 0, 1, 1)

        main.setCentralWidget(self.centralwidget)

        statusbar = QStatusBar(main)
        statusbar.setObjectName("statusbar")

        main.setStatusBar(statusbar)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)


    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    win = QMainWindow()

    ui = MainWindow()
    ui.setupUi(win)

    win.show()

    sys.exit(app.exec())
