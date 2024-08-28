from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QFileDialog
from core.capture import PlayblastManager
from shiboken6 import wrapInstance
from maya import OpenMayaUI
import maya.cmds as cmds
import maya.app.general.createImageFormats as createImageFormats

def get_maya_window():
    """Get pointed to Maya's main window to use as parent

    Returns:
        QWidget: QWidget representing Maya's main window
    """
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)


class PlayblastManagerUI(QMainWindow):

    def __init__(self, parent=get_maya_window()):
        super().__init__(parent=parent)
        # Configure the window
        self.setWindowTitle("Playblast Manager")
        self.setGeometry(300, 300, 500, 250)
        self.main_widget = PlayblastManagerWidget()
        self.setCentralWidget(self.main_widget)


class PlayblastManagerWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent = parent)

        # Initialize the form layout
        form_layout = QFormLayout()

        # First row
        first_row = QLabel("Name of playblast:")
        self.name_line_edit = QLineEdit()
        form_layout.addRow(first_row, self.name_line_edit)

        # Second row
        second_row = QLabel("Frame rate:")
        self.rate_line_edit = QLineEdit()
        form_layout.addRow(second_row, self.rate_line_edit)

        third_row = QLabel("Size:")
        self.width_line_edit = QLineEdit()
        self.height_line_edit = QLineEdit()

        # Create a horizontal layout for the two QLineEdits
        size_hbox_layout = QHBoxLayout()
        size_hbox_layout.addWidget(self.width_line_edit)
        size_hbox_layout.addWidget(self.height_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(third_row, size_hbox_layout)


        fourth_row = QLabel("Frame range:")
        self.start_line_edit = QLineEdit()
        self.end_line_edit = QLineEdit()

        # Create a horizontal layout for the two QLineEdits
        range_hbox_layout = QHBoxLayout()
        range_hbox_layout.addWidget(self.start_line_edit)
        range_hbox_layout.addWidget(self.end_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(fourth_row, range_hbox_layout)

        # Second row
        file_row = QLabel("Export Directory:")
        self.directory_line_edit = QLineEdit()
        form_layout.addRow(file_row, self.directory_line_edit)

        # Create the "Browse" button
        self.browse_button = QPushButton("Browse")

        # Create a horizontal layout to center the button
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.browse_button)

        # Add the button layout to the form layout (so it appears just below the inputs)
        form_layout.addRow(button_layout)

        # Set the layout for the widget
        self.setLayout(form_layout)

        # Define the labels and corresponding Artist
        artist_row = QLabel("Artist Name:")
        self.artist_line_edit = QLineEdit()

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.artist_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(artist_row, hbox_layout)

        # Define the labels and corresponding Department
        department_row = QLabel("Department:")
        self.department_line_edit = QLineEdit()

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.department_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(department_row, hbox_layout)

        # Define the labels and corresponding company
        company_row = QLabel("Company Name:")
        self.company_line_edit = QLineEdit()

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.company_line_edit)

        # Add the label and the horizontal layout to the form layout
        form_layout.addRow(company_row, hbox_layout)


        # Create the "Playblast" button
        self.playblast_button = QPushButton("Playblast")

        # Create a horizontal layout to center the button
        button_2_layout = QHBoxLayout()
        button_2_layout.addStretch()
        button_2_layout.addWidget(self.playblast_button)

        # Add the button layout to the form layout (so it appears just below the inputs)
        form_layout.addRow(button_2_layout)

        # Signals
        self.playblast_button.clicked.connect(self.do_playblast)
        self.browse_button.clicked.connect(self.browse_file)

    def browse_file(self):
        # Define file filters
        multipleFilters = "Movie Files (*.mov *.mp4 *.avi *.mkv);;All Files (*.*)"

        # Open the save file dialog
        file_path = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2,
                                     startingDirectory=self.directory_line_edit.text(), fm=0)

        if file_path:
            # file_path is a list, so take the first selected file
            file_path = file_path[0]

            # Extract directory path from the file path
            directory_path = '/'.join(file_path.split('/')[:-1])

            # Set the directory path in the line edit
            self.directory_line_edit.setText(directory_path)

            # Extract and display the file name and final path
            file_name = file_path.split('/')[-1]
            print(f"Selected File Name: {file_name}")
            print(f"Selected Directory Path: {directory_path}")


    def do_playblast(self):
        playblast_mgr = PlayblastManager()

        file_name = self.name_line_edit.text()
        dir_name = self.directory_line_edit.text()
        width = self.width_line_edit.text()
        height = self.height_line_edit.text()
        frame_rate = self.rate_line_edit.text()
        start_frame = self.start_line_edit.text()
        end_frame = self.end_line_edit.text()
        artist_name = self.artist_line_edit.text()
        department_name = self.department_line_edit.text()
        company_name = self.company_line_edit.text()

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

        try:
            playblast_mgr.do_playblast(dir_name, file_name, int(width), int(height), int(frame_rate), int(start_frame), int(end_frame), artist_name, department_name, company_name)
        except(ValueError):
            cmds.inViewMessage(amg='<hl>please provide all the information</hl>.', pos='topCenter', fade=True)



if __name__ == "__main__":
    app = QApplication([])
    window = PlayblastManagerUI()
    window.show()
    app.exec()
