from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QFileDialog, QComboBox
import maya.cmds as cmds
from PySide6.QtGui import QValidator, QIcon
from PySide6.QtCore import QSize
from core.capture import PlayblastManager
from shiboken6 import wrapInstance
from maya import OpenMayaUI
import maya.cmds as cmds
from os.path import join, dirname, isdir
import maya.app.general.createImageFormats as createImageFormats

# Define repository path via environment variable
icon_path = dirname(dirname(__file__))
ICON = join(icon_path, "ui", "folder.png")

def get_maya_window():
    """Get pointed to Maya's main window to use as parent

    Returns:
        QWidget: QWidget representing Maya's main window
    """
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)

class IntegerValidator(QValidator):
    def validate(self, input_text, pos):
        if input_text == "":
            return QValidator.Intermediate
        try:
            int(input_text)
            return QValidator.Acceptable
        except ValueError:
            return QValidator.Invalid


class PlayblastManagerUI(QMainWindow):

    def __init__(self, parent=get_maya_window(), debug = False):
        """
        This function creates the main window of the UI
        Args:
             parent (QWidget): Parent widget for the window. Default to Maya window.
            debug (bool): Initialize in debug mode. If True, the temporary folder will not be deleted.
        """
        super().__init__(parent=parent)
        # Configure the window
        self.setWindowTitle("Playblast Manager")
        self.setGeometry(300, 300, 500, 250)
        self.main_widget = PlayblastManagerWidget( debug = debug)
        self.setCentralWidget(self.main_widget)


class PlayblastManagerWidget(QWidget):

    def __init__(self, parent=None, debug = False):
        """
        This function populates the UI created by the PlayblastManagerUI class
        Args:
            parent (None): just indicates that the function does not inherits from any other function
            debug (bool): placed to see the temporary folder of all the assets or don't see it
        """
        super().__init__(parent = parent)
        self.debug = debug
        self.playblast_mgr = PlayblastManager(debug = debug)

        self.default_width = "1280"
        self.default_height = "720"
        # Initialize the form layout
        form_layout = QFormLayout()

        # First row
        first_row = QLabel("Name of playblast:")
        self.name_line_edit = QLineEdit()
        form_layout.addRow(first_row, self.name_line_edit)

        # Second row
        file_row = QLabel("Export Directory:")
        self.directory_line_edit = QLineEdit()
        self.browse_button = QPushButton("Browse")

        self.browse_button.setMinimumSize(100, 24)

        # Set an icon for the button
        self.browse_button.setIcon(QIcon(ICON))
        self.browse_button.setIconSize(QSize(20, 20))

        # Create a horizontal layout to center the button
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.directory_line_edit)
        button_layout.addWidget(self.browse_button)

        # Add the button layout to the form layout (so it appears just below the inputs)
        form_layout.addRow(file_row, button_layout)

        # Set the layout for the widget
        self.setLayout(form_layout)

        # rate_row
        rate_row = QLabel("Frame rate:")
        self.rate_combo_box = QComboBox()
        rates = ["24", "23.976", "25", "29.97", "30", "40", "60"]
        for i in rates:
            self.rate_combo_box.addItem(i)
        form_layout.addRow(rate_row, self.rate_combo_box)

        third_row = QLabel("Size:")
        self.width_line_edit = QLineEdit(self.default_width)
        self.height_line_edit = QLineEdit(self.default_height)
        self.width_line_edit.setValidator(IntegerValidator())
        self.height_line_edit.setValidator(IntegerValidator())

        # Create a horizontal layout for the two QLineEdits
        size_hbox_layout = QHBoxLayout()
        size_hbox_layout.addWidget(self.width_line_edit)
        size_hbox_layout.addWidget(self.height_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(third_row, size_hbox_layout)

        fourth_row = QLabel("Frame range:")

        self.start_line_edit = QLineEdit(self.get_start_frame())
        self.end_line_edit = QLineEdit(self.get_end_frame())
        self.start_line_edit.setValidator(IntegerValidator())
        self.end_line_edit.setValidator(IntegerValidator())

        # Create a horizontal layout for the two QLineEdits
        range_hbox_layout = QHBoxLayout()
        range_hbox_layout.addWidget(self.start_line_edit)
        range_hbox_layout.addWidget(self.end_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(fourth_row, range_hbox_layout)

        # Define the labels and corresponding Artist
        artist_row = QLabel("Artist Name:")
        self.artist_line_edit = QLineEdit()
        self.artist_line_edit.setPlaceholderText("Optional...")

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.artist_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(artist_row, hbox_layout)

        # Define the labels and corresponding Department
        department_row = QLabel("Department:")
        self.department_line_edit = QLineEdit()
        self.department_line_edit.setPlaceholderText("Optional...")

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.department_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(department_row, hbox_layout)

        # Define the labels and corresponding company
        company_row = QLabel("Company Name:")
        self.company_line_edit = QLineEdit()
        self.company_line_edit.setPlaceholderText("Optional...")

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.company_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(company_row, hbox_layout)

        #Create "clean up" button
        self.reset_button = QPushButton("Reset")
        self.reset_button.setToolTip("Reset to default values")

        # Create the "Playblast" button
        self.playblast_button = QPushButton("Playblast")

        # Create a horizontal layout to center the button
        button_2_layout = QHBoxLayout()
        button_2_layout.addStretch()
        button_2_layout.addWidget(self.reset_button)
        button_2_layout.addWidget(self.playblast_button)


        # Add the button layout to the form layout (so it appears just below the inputs)
        form_layout.addRow(button_2_layout)

        # Signals
        self.playblast_button.clicked.connect(self.do_playblast)
        self.browse_button.clicked.connect(self.browse_file)
        self.reset_button.clicked.connect(self.do_reset)

    def get_start_frame(self):
        start = int(cmds.playbackOptions(q=True, min=True))
        start = str(start)
        return start

    def get_end_frame(self):
        end = int(cmds.playbackOptions(q=True, max=True))
        end = str(end)
        return end

    def browse_file(self):
        """
        This function is called when the browse button is clicked and allows the user
        to input the folder where he/she wants to store the video
        """
        # Define file filters
        multipleFilters = "Movie Files (*.mov *.mp4 *.avi *.mkv);;All Files (*.*)"

        # Open the save file dialog
        file_path = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2,
                                     startingDirectory=self.directory_line_edit.text(), fm=3)

        if file_path:
            # file_path is a list, so take the first selected file
            file_path = file_path[0]

            # Set the directory path in the line edit
            self.directory_line_edit.setText(file_path)

            # Extract and display the file name and final path
            print(f"Selected Directory Path: {file_path}")

    def do_reset(self):
        """
        This function resets the fields of the ui
        """

        self.name_line_edit.setText("")
        self.directory_line_edit.setText("")
        self.width_line_edit.setText(self.default_width)
        self.height_line_edit.setText(self.default_height)
        self.start_line_edit.setText(self.get_start_frame())
        self.end_line_edit.setText(self.get_end_frame())
        self.artist_line_edit.setText("")
        self.department_line_edit.setText("")
        self.company_line_edit.setText("")




    def do_playblast(self):
        """
        This function is the most important, is the one that calls on playblast_mgr that calls PlayblastManager class
        to do the final playblast

        """

        file_name = self.name_line_edit.text()
        dir_name = self.directory_line_edit.text()
        width = self.width_line_edit.text()
        height = self.height_line_edit.text()
        frame_rate = self.rate_combo_box.currentText()
        start_frame = self.start_line_edit.text()
        end_frame = self.end_line_edit.text()
        artist_name = self.artist_line_edit.text()
        department_name = self.department_line_edit.text()
        company_name = self.company_line_edit.text()

        if self.debug is True:
            print(f"file_name {file_name}")
            print(f"dir_name {dir_name}")
            print(f"width {width}")
            print(f"height {height}")
            print(f"frame_rate {frame_rate}")
            print(f"start_frame {start_frame}")
            print(f"end_frame {end_frame}")
            print(f"artist_name {artist_name}")
            print(f"department_name {department_name}")
            print(f"company_name {company_name}")

        if file_name != "" and isdir(dir_name):

            try:
                self.playblast_mgr.do_playblast(dir_name, file_name, int(width), int(height), int(frame_rate), int(start_frame), int(end_frame), artist_name, department_name, company_name)
            except(ValueError):
                cmds.inViewMessage(amg='<hl>please provide all the information</hl>.', pos='topCenter', fade=True)
        else:
            cmds.inViewMessage(amg='<hl>please provide a valid name or folder for the playblast</hl>.', pos='topCenter', fade=True)


if __name__ == "__main__":
    app = QApplication([])
    window = PlayblastManagerUI()
    window.show()
    app.exec()
