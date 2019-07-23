import os
import sys

_dir = os.path.dirname(__file__)
sys.path.append(_dir)

os.environ["QT_PREFERRED_BINDING"] = "PySide"  # Unix/OSX
try:
    from Qt import QtCore, QtGui, QtWidgets
except:
    import traceback
    trackback.print_exc()

from QtPythonConsole.console import ConsoleDialog


def _build_connection():
    import SyPy
    connection = SyPy.SyLevel()
    if connection.OpenExisting():
        print("Connection opened")
        return connection
    return


def main():
    app = QtWidgets.QApplication.instance()
    start = False
    if not app:
        start = True
        app = QtWidgets.QApplication([])

    # Build existing connection object
    connection = _build_connection()

    # Add a nice helper comment at the top of the file.
    _comment_line = "# " + ("=" * 60) + "\n"
    additional_text = _comment_line
    if not connection:
        additional_text += "# Could not initiate an automatic hlev SyPy connection\n"
    else:
        additional_text += "# A SyPy hlev connection object is initialized as \"connection\"\n"
    additional_text += _comment_line

    dialog = ConsoleDialog(_locals={"connection": connection})
    dialog.resize(1200, 600)
    dialog.show()

    # Replace the helper text if existing
    _text = dialog.console_widget.input_console.toPlainText()
    if _text.startswith(_comment_line):
        lines = _text.split("\n")
        lines = additional_text.split("\n") + lines[3:]
        dialog.console_widget.input_console.setCode("\n".join(lines))

    else:
        dialog.console_widget.input_console.setCode(additional_text + _text)

    # If we created the app, we need to start it
    if start:
        app.exec_()


if __name__ == "__main__":
    main()
