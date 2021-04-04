import tkinter
import os
import platform
from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    app_file_path = ''
    app_icon_path = ''
    op_sys = platform.system()

    def btn_path_clicked(self):
        try:
            home_dir = os.path.expanduser('~')

            dialog = QtWidgets.QFileDialog()
            file = dialog.getOpenFileName(
                dialog,
                'SELECIONAR ARQUIVO',
                home_dir,
                'Arquivo python (*.py)'
            )

            self.txtPath.setText(file[0].replace(home_dir, ''))
            self.app_file_path = file[0]

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

    def btn_icon_clicked(self):
        try:
            home_dir = os.path.expanduser('~')

            dialog = QtWidgets.QFileDialog()
            file = dialog.getOpenFileName(
                dialog,
                'SELECIONAR ÍCONE',
                home_dir,
                'Arquivo de ícone (*.ico)'
            )

            icon = QtGui.QPixmap(file[0])
            self.iconBox.setPixmap(icon)
            self.app_icon_path = file[0]

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

    def btn_create_clicked(self):
        if not self.app_file_path.endswith('.py'):
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror(
                'ERRO',
                'O arquivo selecionado não é válido\nselecione outro e tente novamente'
            )
            tkinter.Tk().destroy()
        else:
            if self.op_sys == 'Windows' and self.app_icon_path == '':
                root = tkinter.Tk()
                root.withdraw()
                choice = messagebox.askyesno(
                    'CRIAR EXECUTÁVEL',
                    'Deseja criar um executável sem ícone customizado?'
                )
                tkinter.Tk().destroy()

                if choice == True:
                    self.create_app()

            else:
                self.create_app()

    def create_app(self):
        try:
            from plyer import notification

            notification.notify(
                title = 'CRIANDO EXECUTÁVEL',
                message = 'O executável está sendo construído, você será notificado ao término da operação',
                timeout = 10
            )

            output_dir = ''
            path = self.app_file_path.split('/')

            i = 0
            while i < len(path) - 1:
                output_dir += f'{path[i]}/'
                i += 1

            if self.op_sys == 'Windows':
                if self.app_icon_path != '':
                    os.system(f'pyinstaller -F -w -n executavel --specpath {output_dir} --distpath {output_dir}\\dist\\ --workpath {output_dir}\\build\\ -i {self.app_icon_path} {self.app_file_path}')

                    if os.path.exists(f'{output_dir}\\dist\\executavel.exe'):
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showinfo('COMPLETO', 'EXECUTÁVEL CRIADO COM SUCESSO')
                        tkinter.Tk().destroy()
                    else:
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showerror('ERRO', 'NÃO FOI POSSÍVEL CRIAR O EXECUTÁVEL')
                        tkinter.Tk().destroy()

                else:
                    os.system(f'pyinstaller -F -w -n executavel --specpath {output_dir} --distpath {output_dir}\\dist\\ --workpath {output_dir}\\build\\ {self.app_file_path}')

                    if os.path.exists(f'{output_dir}\\dist\\executavel.exe'):
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showinfo('COMPLETO', 'EXECUTÁVEL CRIADO COM SUCESSO')
                        tkinter.Tk().destroy()
                    else:
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showerror('ERRO', 'NÃO FOI POSSÍVEL CRIAR O EXECUTÁVEL')
                        tkinter.Tk().destroy()
            else:
                os.system(f'pyinstaller -F -w -n executavel --specpath {output_dir} --distpath {output_dir}/dist/ --workpath {output_dir}/build/ {self.app_file_path}')

                if os.path.exists(f'{output_dir}/dist/executavel'):
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showinfo('COMPLETO', 'EXECUTÁVEL CRIADO COM SUCESSO')
                    tkinter.Tk().destroy()
                else:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror('ERRO', 'NÃO FOI POSSÍVEL CRIAR O EXECUTÁVEL')
                    tkinter.Tk().destroy()
                        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 185)
        MainWindow.setMinimumSize(QtCore.QSize(650, 185))
        MainWindow.setMaximumSize(QtCore.QSize(750, 185))
        MainWindow.setWindowTitle("CRIADOR DE EXECUTÁVEIS")
        icon = QtGui.QIcon.fromTheme("applications-development")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnIcon = QtWidgets.QPushButton(self.centralwidget)
        self.btnIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnIcon.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Clique aqui para adicionar um ícone para o executável.</span></p><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; text-decoration: underline;\">Disponível apenas para Windows.</span></p></body></html>")
        self.btnIcon.setText("ESCOLHER ÍCONE")
        self.btnIcon.setObjectName("btnIcon")
        self.gridLayout.addWidget(self.btnIcon, 3, 2, 1, 1)
        self.iconBox = QtWidgets.QLabel(self.centralwidget)
        self.iconBox.setEnabled(True)
        self.iconBox.setMinimumSize(QtCore.QSize(128, 128))
        self.iconBox.setMaximumSize(QtCore.QSize(128, 128))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.iconBox.setFont(font)
        self.iconBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.iconBox.setToolTip("")
        self.iconBox.setFrameShape(QtWidgets.QFrame.Box)
        self.iconBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.iconBox.setLineWidth(2)
        self.iconBox.setText("ÍCONE")
        self.iconBox.setTextFormat(QtCore.Qt.PlainText)
        self.iconBox.setScaledContents(True)
        self.iconBox.setAlignment(QtCore.Qt.AlignCenter)
        self.iconBox.setObjectName("iconBox")
        self.gridLayout.addWidget(self.iconBox, 0, 2, 3, 1)
        self.txtPath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPath.setEnabled(True)
        self.txtPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtPath.setToolTip("<html><head/><body><p>use o botão ao lado para selecionar o caminho do arquivo &quot;.py&quot;</p></body></html>")
        self.txtPath.setInputMask("")
        self.txtPath.setText("")
        self.txtPath.setDragEnabled(False)
        self.txtPath.setReadOnly(True)
        self.txtPath.setPlaceholderText("Selecione o arquivo \".py\" com o botão acima")
        self.txtPath.setObjectName("txtPath")
        self.gridLayout.addWidget(self.txtPath, 2, 0, 1, 1)
        self.btnCreate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCreate.setFont(font)
        self.btnCreate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCreate.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:400;\">Clique aqui para criar um executável nativo para o seu sistema operacional</span></p></body></html>")
        self.btnCreate.setText("CRIAR EXECUTÁVEL")
        icon = QtGui.QIcon.fromTheme("text-x-script")
        self.btnCreate.setIcon(icon)
        self.btnCreate.setObjectName("btnCreate")
        self.gridLayout.addWidget(self.btnCreate, 3, 0, 1, 1)
        self.btnPath = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(False)
        self.btnPath.setFont(font)
        self.btnPath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPath.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Clique aqui para selecionar um arquivo</span></p></body></html>")
        self.btnPath.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPath.setText("ESCOLHER ARQUIVO")
        icon = QtGui.QIcon.fromTheme("text-x-python")
        self.btnPath.setIcon(icon)
        self.btnPath.setObjectName("btnPath")
        self.gridLayout.addWidget(self.btnPath, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("CRIADOR DE EXECUTÁVEIS PARA PYTHON")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnPath, self.btnIcon)
        MainWindow.setTabOrder(self.btnIcon, self.btnCreate)

        self.btnPath.clicked.connect(self.btn_path_clicked)
        self.btnIcon.clicked.connect(self.btn_icon_clicked)
        self.btnCreate.clicked.connect(self.btn_create_clicked)
        
        if self.op_sys == 'Linux':
            self.iconBox.setEnabled(False)
            self.iconBox.setText('Ícones indisponíveis\npara Linux')
            self.btnIcon.setEnabled(False)

if __name__ == "__main__":
    import sys
    import os

    os.system('python -m pip install plyer pyinstaller pyqt5')

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
