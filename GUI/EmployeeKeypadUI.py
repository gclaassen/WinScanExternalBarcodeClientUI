import tkinter as tk
import tkinter.font as font

class EmployeeCodes:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.textEntryWidget = tk.Entry(self.frame)
        self.frame.pack()
        self.font = font.Font(size=30)

        self.backspaceIcon = '<'
        self.cancelIcon = 'C'

        self.EmployeeIdKeys = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            [self.backspaceIcon, '0', self.cancelIcon],
        ]

        self.EmployeeIdCode = ''

        self.employeesWindow()

    def keyPadPressed(self, value):
        if value == self.backspaceIcon:
            self.EmployeeIdCode = self.EmployeeIdCode[:-1]
            self.textEntryWidget.delete('0', 'end')
            self.textEntryWidget.insert('end', self.EmployeeIdCode)

        elif value == self.cancelIcon:
            # clear `pin`
            self.EmployeeIdCode = ''
            # clear `entry`
            self.textEntryWidget.delete('0', 'end')

        else:
            self.EmployeeIdCode += value
            self.textEntryWidget.insert('end', value)

    def acceptButtonPressed(self):
        # clear `entry`
        self.textEntryWidget.delete('0', 'end')
        # clear global
        self.EmployeeIdCode = ''
        NotImplementedError


    def employeesWindow(self):
        btnColor = 'gray'

        # self.textEntryWidget.config(state="readonly")
        self.textEntryWidget.grid(row=0, column=0, columnspan=3, ipady=50)
        self.textEntryWidget['font'] = self.font


        # create buttons using `keys`
        for y, row in enumerate(self.EmployeeIdKeys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)`
                # instead of direct `code(key)`
                if key == self.backspaceIcon:
                    btnColor = 'goldenrod1'
                elif key == self.cancelIcon:
                    btnColor = 'red'
                else:
                    btnColor = 'gray'

                keyPadButton = tk.Button(self.frame, text=key, bg=btnColor, command=lambda val=key:self.keyPadPressed(val))
                keyPadButton.grid(row=y, column=x, ipadx=50, ipady=50)
                keyPadButton['font'] = self.font

        acceptButton = tk.Button(self.frame, text='YES', bg='green', command=lambda: self.acceptButtonPressed())
        acceptButton.grid(row=y+1, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)
        acceptButton['font'] = self.font

        self.frame.grid_columnconfigure(4, minsize=100)
