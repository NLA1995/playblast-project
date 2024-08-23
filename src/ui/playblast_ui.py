from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from core.capture import PlayblastManager
from shiboken6 import wrapInstance
from maya import OpenMayaUI


def get_maya_window():
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)


class PlayblastManagerUI(QWidget):

    def __init__(self, parent=get_maya_window()):
        super().__init__(parent = parent)

        # Configure the window
        self.setWindowTitle("Playblast Manager")
        self.setGeometry(300, 300, 500, 250)

        # Initialize the form layout
        form_layout = QFormLayout()

        # First row
        first_row = QLabel("Name of playblast:")
        self.name_line_edit = QLineEdit()
        form_layout.addRow(first_row, self.name_line_edit)

        # Second row
        second_row = QLabel("Frame rate:")
        rate_line_edit = QLineEdit()
        form_layout.addRow(second_row, rate_line_edit)



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
        browse_button = QPushButton("Browse")

        # Create a horizontal layout to center the button
        button_layout = QHBoxLayout()
        button_layout.addWidget(browse_button)

        # Add the button layout to the form layout (so it appears just below the inputs)
        form_layout.addRow(button_layout)

        # Set the layout for the widget
        self.setLayout(form_layout)

        # Define the labels and corresponding QLineEdits
        review_labels = [
            "Artist Name:",
            "Department:",
            "Company Name:",
        ]

        # Add QLabel and two QLineEdit widgets side by side for each label
        for label_name_2 in review_labels:
            label_2 = QLabel(label_name_2)
            line_edit3 = QLineEdit()

            # Create a horizontal layout for the two QLineEdits
            hbox_layout = QHBoxLayout()
            hbox_layout.addWidget(line_edit3)

            # Add the label and the horizontal layout to the form layout
            form_layout.addRow(label_2, hbox_layout)

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


    def do_playblast(self):
        playblast_mgr = PlayblastManager()

        file_name = self.name_line_edit.text()
        dir_name = self.directory_line_edit.text()
        width = self.width_line_edit.text()
        height = self.height_line_edit.text()
        start_frame = self.start_line_edit.text()
        end_frame = self.end_line_edit.text()

        print(f"file_name {file_name}")
        print(f"dir_name {dir_name}")
        print(f"width {width}")
        print(f"height {height}")
        print(f"start_frame {start_frame}")
        print(f"end_frame {end_frame}")

        playblast_mgr.do_playblast(dir_name, file_name, int(width), int(height), int(start_frame), int(end_frame))

if __name__ == "__main__":
    app = QApplication([])
    window = PlayblastManagerUI()
    window.show()
    app.exec()
