from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class PlayblastManagerUI(QWidget):
    def __init__(self):
        super().__init__()

        # Configure the window
        self.setWindowTitle("Playblast Manager")
        self.setGeometry(300, 300, 500, 250)

        # Initialize the form layout
        form_layout = QFormLayout()

        # First row
        first_row = QLabel("Name of playblast:")
        name_line_edit = QLineEdit()
        form_layout.addRow(first_row, name_line_edit)

        # Second row
        second_row = QLabel("Frame rate:")
        rate_line_edit = QLineEdit()
        form_layout.addRow(second_row, rate_line_edit)

        # Define the labels and corresponding QLineEdits
        settings_labels = [
            "Size:",
            "Frame range:",
        ]

        # Add QLabel and two QLineEdit widgets side by side for each label
        for label_name in settings_labels:
            label = QLabel(label_name)
            line_edit1 = QLineEdit()
            line_edit2 = QLineEdit()

            # Create a horizontal layout for the two QLineEdits
            hbox_layout = QHBoxLayout()
            hbox_layout.addWidget(line_edit1)
            hbox_layout.addWidget(line_edit2)

            # Add the label and the horizontal layout to the form layout
            form_layout.addRow(label, hbox_layout)

        # Second row
        file_row = QLabel("Export Directory:")
        directory_line_edit = QLineEdit()
        form_layout.addRow(file_row, directory_line_edit)

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
        playblast_button = QPushButton("Playblast")

        # Create a horizontal layout to center the button
        button_2_layout = QHBoxLayout()
        button_2_layout.addStretch()
        button_2_layout.addWidget(playblast_button)

        # Add the button layout to the form layout (so it appears just below the inputs)
        form_layout.addRow(button_2_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = PlayblastManager()
    window.show()
    app.exec()

