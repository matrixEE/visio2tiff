import sys
import os
import win32com.client
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PySide6 import QtCore
from mainUI_ui import Ui_mainWindow
from diag_ui import Ui_Dialog
# import debugpy,time
class ok_Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super().__init__(parent)
        self.setupUi(self)

    def show_dialog(self):
        self.exec() 

class mainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super().__init__(parent)
        self.setupUi(self)

    @QtCore.Slot()
    def on_pushButton_open_visio_clicked(self):#打开Visio文件槽函数
        filters = "Visio files (*.vsd *.vsdx)"
        visio_file_name,filetype=QFileDialog.getOpenFileName(self,u'Open the visio file','',filters)
        if visio_file_name:
            directory = QFileDialog.getExistingDirectory(self, u"Select the save directory", os.path.dirname(visio_file_name))
            if directory:
                dpiSelect=int(self.comboBox.currentText())
                visio_file_name=os.path.abspath(os.path.normpath(visio_file_name))#解决中文路径报错问题

                # 设置进度条为忙碌模式
                self.progressBar_visio.setRange(0, 0)          
                # 启动线程
                self.workerVisio = VisioConversionWorker(visio_file_name, dpiSelect, directory)
                self.workerVisio.set_range.connect(self.set_progressvisio_range)  # 连接设置范围的信号
                self.workerVisio.progress.connect(self.update_progressvisio)  # 连接更新进度条信号
                self.workerVisio.finished.connect(self.conversionvisio_finished) #连接重置进度条信号
                self.workerVisio.start()

    @QtCore.Slot(int)#装饰器
    def update_progressvisio(self, value):
        self.progressBar_visio.setValue(value)

    @QtCore.Slot(int, int)#装饰器
    def set_progressvisio_range(self, min_value, max_value):
        self.progressBar_visio.setRange(min_value, max_value)

    @QtCore.Slot()#装饰器
    def conversionvisio_finished(self):
        # 结束后重置进度条
        self.progressBar_visio.setRange(0, 100)
        self.progressBar_visio.setValue(0)
        # 显示成功对话框
        okDialog = ok_Dialog()
        okDialog.show_dialog()


    @QtCore.Slot()#装饰器
    def on_pushButton_open_word_clicked(self):#打开Word文件槽函数
        filters = "Word files (*.doc *.docx)"
        word_file_name,filetype=QFileDialog.getOpenFileName(self,u'Open the word file','',filters)
        if word_file_name:
            directory = QFileDialog.getExistingDirectory(self, u"Select the save directory", os.path.dirname(word_file_name))
            if directory:
                dpiSelect=int(self.comboBox.currentText())
                word_file_name=os.path.abspath(os.path.normpath(word_file_name))#解决中文路径报错问题

                # 设置进度条为忙碌模式
                self.progressBar_word.setRange(0, 0)          
                # 启动线程
                self.workerWord = WordConversionWorker(word_file_name, dpiSelect, directory)
                self.workerWord.set_range.connect(self.set_progressword_range)  # 连接设置范围的信号
                self.workerWord.progress.connect(self.update_progressword)  # 连接更新进度条信号
                self.workerWord.finished.connect(self.conversionword_finished) #连接重置进度条信号
                self.workerWord.start()

    @QtCore.Slot(int)#装饰器
    def update_progressword(self, value):
        self.progressBar_word.setValue(value)

    @QtCore.Slot(int, int)#装饰器
    def set_progressword_range(self, min_value, max_value):
        self.progressBar_word.setRange(min_value, max_value)

    @QtCore.Slot()#装饰器
    def conversionword_finished(self):
        # 结束后重置进度条
        self.progressBar_word.setRange(0, 100)
        self.progressBar_word.setValue(0)
        # 显示成功对话框
        okDialog = ok_Dialog()
        okDialog.show_dialog()


class VisioConversionWorker(QtCore.QThread):
    set_range = QtCore.Signal(int, int)  # 用于设置进度条范围的信号
    progress = QtCore.Signal(int)  # 用于进度更新的信号

    def __init__(self, visio_file_name, dpiSelect, directory):
        super().__init__()
        self.visio_file_name = visio_file_name
        self.dpiSelect = dpiSelect
        self.directory = directory
    
    def run(self):
        self.visio_convert_tif(self.visio_file_name, self.dpiSelect, self.directory)


    def visio_convert_tif(self,visio_file,dpi,currentPath):
        if not os.path.exists('outTifTemp'):
            os.mkdir('outTifTemp')
        # 创建  Visio 应用对象
        visio_app = win32com.client.Dispatch("Visio.Application")
        visio_app.Visible = True

        # 打开 Visio 文档
        vdoc = visio_app.Documents.Open(visio_file)
        jTiff=0
        # 遍历所有嵌入的对象
        pageNum=0
        for i, vpage in enumerate(vdoc.Pages ):
            pageNum=pageNum+1

        jTiff=0
        self.set_range.emit(0, 100)#发送设置进度条范围
        for i, vpage in enumerate(vdoc.Pages ):
            jTiff=jTiff+1
            vapp = vdoc.Application
            vapp.Application.Settings.RasterExportDataCompression=5
            activePage=vapp.ActivePage
            output_path=currentPath+'\\out_fig_'+str(jTiff)+'.tif'
            vapp.Application.Settings.SetRasterExportResolution(3,dpi,dpi,0)
            vapp.Application.Settings.SetRasterExportSize(2)
            output_path=os.path.abspath(os.path.normpath(output_path))#解决中文路径报错问题
            vpage.Export(output_path)
            progress_value=int(jTiff/pageNum*100)
            self.progress.emit(progress_value)
        vdoc.Close()
        visio_app.Quit()

class WordConversionWorker(QtCore.QThread):
    set_range = QtCore.Signal(int, int)  # 用于设置进度条范围的信号
    progress = QtCore.Signal(int)  # 用于进度更新的信号

    def __init__(self, word_file_name, dpiSelect, directory):
        super().__init__()
        self.word_file_name = word_file_name
        self.dpiSelect = dpiSelect
        self.directory = directory
    
    def run(self):
        # debugpy.debug_this_thread()
        self.word_visio_convert_tif(self.word_file_name, self.dpiSelect, self.directory)

    def word_visio_convert_tif(self,word_file,dpi,currentPath):

        # 创建 Word 和 Visio 应用对象
        word_app = win32com.client.Dispatch("Word.Application")
        visio_app = win32com.client.Dispatch("Visio.Application")

        word_app.Visible = False
        visio_app.Visible = False

        # 打开 Word 文档
        doc = word_app.Documents.Open(word_file)
        jTiff=0
        # 遍历所有嵌入的对象

        pageNum=0
        for i, shape in enumerate(doc.InlineShapes):
            if shape.Type == 1:  # 确保是嵌入的 OLE 对象
                if 'Visio' in shape.OLEFormat.ProgID: # 确保是Visio对象
                    pageNum=pageNum+1
        self.set_range.emit(0, 100)#发送设置进度条范围
        for i, shape in enumerate(doc.InlineShapes):
            if shape.Type == 1:  # 确保是嵌入的 OLE 对象
                if 'Visio' in shape.OLEFormat.ProgID: # 确保是Visio对象
                    jTiff=jTiff+1
                    original_width = shape.Width
                    original_height = shape.Height
                    shape.OLEFormat.DoVerb(1)
                    ole = shape.OLEFormat
                    vdoc = ole.object
                    vapp = vdoc.Application
                    vapp.Application.Settings.RasterExportDataCompression=5
                    activePage=vapp.ActivePage
                    output_path=currentPath+'\\outTifTemp\\out_fig_'+str(jTiff)+'.tif'
                    os.makedirs(currentPath+'\\outTifTemp', exist_ok=True)
                    vapp.Application.Settings.SetRasterExportResolution(3,dpi,dpi,0)
                    vapp.Application.Settings.SetRasterExportSize(2)
                    output_path=os.path.abspath(os.path.normpath(output_path))#解决中文路径报错问题
                    activePage.Export(output_path)
                    vapp.Quit()
                    # 替换 Visio 对象为 TIF 图片
                    new_shape=shape.Range.InlineShapes.AddPicture(FileName=output_path, LinkToFile=False, SaveWithDocument=True)
                    # # 设置新插入图片的宽度和高度
                    scaleNum1=original_height/new_shape.Height
                    scaleNum2=original_width/new_shape.Width
                    scaleNum=min(scaleNum1,scaleNum2)
                    new_shape.Width = new_shape.Width*scaleNum
                    new_shape.Height = new_shape.Height*scaleNum
                    progress_value=int(jTiff/pageNum*90)
                    self.progress.emit(progress_value)
        # 保存并关闭文档
        # 遍历所有嵌入的对象
        jTiff=0
        for i, shape in enumerate(doc.InlineShapes):
            if shape.Type == 1:  # 确保是嵌入的 OLE 对象
                if 'Visio' in shape.OLEFormat.ProgID: # 确保是Visio对象
                    jTiff=jTiff+1
                    shape.Delete()
                    progress_value=int(90+jTiff/pageNum*10)
                    self.progress.emit(progress_value)#发射更新进度条信号
        splitted_name = os.path.splitext(os.path.basename(word_file))
        no_suffix_name = splitted_name[0]
        if splitted_name[1]=='.docx':
            savePath=currentPath+'\\'+no_suffix_name+'(tif).docx'
            savePath=os.path.abspath(os.path.normpath(savePath))#解决中文路径报错问题
            doc.SaveAs(savePath,FileFormat=12)  # 替换为修改后的 Word 文件路径
        else:
            savePath=currentPath+'\\'+no_suffix_name+'(tif).doc'
            savePath=os.path.abspath(os.path.normpath(savePath))#解决中文路径报错问题
            doc.SaveAs(savePath,FileFormat=0)  # 替换为修改后的 Word 文件路径
        doc.Close()
        word_app.Quit()
        visio_app.Quit()




if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    thisWindow = mainWindow()
    thisWindow.show()
    sys.exit(app.exec())
