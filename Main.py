# UI related imports
from PyQt5 import QtWidgets, uic

# functionality imports
import sys
import subprocess


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        # Initializing, using the superclass init method
        super().__init__()

        uic.loadUi('appGUI.ui', self)
        self.lineEdit.returnPressed.connect(self.executeCommand)
        self.working_dir = "."

        self.lineEdit.setStyleSheet("color: white; background-color: black")
        self.textBrowser.setStyleSheet("color: white; background-color: black")
        self.textBrowser.setText(
            "Welcome to Terminalio! \n on your command. \n >")

    def executeCommand(self):
        # Parsing input
        command = self.lineEdit.text()

        # Clearing after parsing
        self.lineEdit.setText('')

        if command == "exit":
            sys.exit(0)

        elif command == "clear":
            self.textBrowser.setText('> ')

        elif "cd " in command:
            values = command.split(" ")
            if values[1][0] == "/":
                self.working_dir = values[1]
            else:
                self.working_dir = self.working_dir + "/" + values[1]

            print(self.working_dir)

            self.textBrowser.setText(
                self.textBrowser.toPlainText() + "\n > " + command)

        else:
            try:
                result = subprocess.check_output(
                    command, shell=True, cwd=self.working_dir)
                self.textBrowser.setText(self.textBrowser.toPlainText(
                ) + "\n > " + command + " " + result.decode("utf-8"))
            except:
                self.textBrowser.setText(self.textBrowser.toPlainText(
                ) + "\n  " + "'" + command + "'" + " returned an error or wasn't recognized, please enter a valid command")

        self.textBrowser.verticalScrollBar().setValue(
            self.textBrowser.verticalScrollBar().maximum())


mainApp = QtWidgets.QApplication([])
mainWindow = Application()
mainWindow.show()
sys.exit(mainApp.exec())
