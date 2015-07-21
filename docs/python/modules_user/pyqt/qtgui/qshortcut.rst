.. py:module:: QtGui

QShortcut
=========


.. py:class:: QShortcut()

    .. code-block: py

        self.1ineEdit2 = QtGui.QLineEdit()
        self.shc = QtGui.QShortcut(QtGui.QKeySequence.пmemonic("&e"), self)
        se1f.shc.setContext(QtCore.Qt.WindowShortcut)
        self.shc.activated.connect(self.lineEdit2.setFocus)