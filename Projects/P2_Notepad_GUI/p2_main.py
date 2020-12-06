import tkinter
import os
import time
import os.path
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisStatsMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Untitled - Notepad")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)
        # To save current file as
        self.__thisFileMenu.add_command(label="Save as",
                                        command=self.__saveFileAs)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)
        # To give a feature of find
        self.__thisEditMenu.add_command(label="Find",
                                        command=self.__find)
        # To give a feature of find and replace
        self.__thisEditMenu.add_command(label="Find and Replace",
                                        command=self.__findAndReplace)

        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # To give a feature of Word Count
        self.__thisStatsMenu.add_command(label="Word Count",
                                        command=self.__wordCount)

        # To give a feature of Char Count
        self.__thisStatsMenu.add_command(label="Char Count",
                                         command=self.__charCount)

        # To give a feature of Created Time
        self.__thisStatsMenu.add_command(label="Created Time",
                                         command=self.__CreatedTime)

        # To give a feature of Modified Time
        self.__thisStatsMenu.add_command(label="Modified Time",
                                         command=self.__modifiedTime)

        # To give a feature of Stats
        self.__thisMenuBar.add_cascade(label="Stats",
                                       menu=self.__thisStatsMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    # exit()

    def __showAbout(self):
        showinfo("Notepad", "This Notepad is Created by Abhishek And Rishabh")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFileAs(self):
        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __find(self):
        #from tkinter import *
        strn = self.__thisTextArea.get(1.0, END)
        # to create a window
        __root = Tk()


        # root window is the parent window
        fram = Frame(__root)

        # Creating Label, Entry Box, Button
        # and packing them adding label to
        # search box
        Label(fram, text=' ').pack(side=LEFT)

        # adding of single line text box
        edit = Entry(fram)

        # positioning of text box
        edit.pack(side=LEFT, fill=BOTH, expand=1)

        # setting focus
        edit.focus_set()

        # adding of search button
        Find = Button(fram, text='Find')
        Find.pack(side=LEFT)

        # Label(fram, text="Replace With ").pack(side=LEFT)

        # edit2 = Entry(fram)
        # edit2.pack(side=LEFT, fill=BOTH, expand=1)
        # edit2.focus_set()

        # replace = Button(fram, text='FindNReplace')
        # replace.pack(side=LEFT)

        fram.pack(side=TOP)

        # text box in root window
        text = Text(__root)

        # text input area at index 1 in text window
        text.insert('1.0', strn)
        text.pack(side=BOTTOM)

        # function to search string in text
        def find():
            # remove tag 'found' from index 1 to END
            text.tag_remove('found', '1.0', END)

            # returns to widget currently in focus
            s = edit.get()

            if (s):
                idx = '1.0'
                while 1:
                    # searches for desried string from index 1
                    idx = text.search(s, idx, nocase=1,
                                      stopindex=END)

                    if not idx: break
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(s))

                    # overwrite 'Found' at idx
                    text.tag_add('found', idx, lastidx)
                    idx = lastidx

                    # mark located string as red

                text.tag_config('found', foreground='red')
            edit.focus_set()

        # def findNreplace():
        #     # remove tag 'found' from index 1 to END
        #     text.tag_remove('found', '1.0', END)
        #
        #     # returns to widget currently in focus
        #     s = edit.get()
        #     r = edit2.get()
        #
        #     if (s and r):
        #         idx = '1.0'
        #         while 1:
        #             # searches for desried string from index 1
        #             idx = text.search(s, idx, nocase=1,
        #                               stopindex=END)
        #             print(idx)
        #             if not idx: break
        #
        #             # last index sum of current index and
        #             # length of text
        #             lastidx = '% s+% dc' % (idx, len(s))
        #
        #             text.delete(idx, lastidx)
        #             text.insert(idx, r)
        #
        #             lastidx = '% s+% dc' % (idx, len(r))
        #
        #             # overwrite 'Found' at idx
        #             text.tag_add('found', idx, lastidx)
        #             idx = lastidx
        #
        #             # mark located string as red
        #         text.tag_config('found', foreground='green', background='yellow')
        #     edit.focus_set()

        Find.config(command=find)
        # replace.config(command=findNreplace)

        # mainloop function calls the endless
        # loop of the window, so the window will
        # wait for any user interaction till we
        # close it
        #root.mainloop()

    def __findAndReplace(self):
        #from tkinter import *
        strn = self.__thisTextArea.get(1.0, END)
        # to create a window
        root = Tk()

        # root window is the parent window
        fram = Frame(root)

        # Creating Label, Entry Box, Button
        # and packing them adding label to
        # search box
        Label(fram, text='Find').pack(side=LEFT)

        # adding of single line text box
        edit = Entry(fram)

        # positioning of text box
        edit.pack(side=LEFT, fill=BOTH, expand=1)

        # setting focus
        edit.focus_set()

        # adding of search button
        Find = Button(fram, text='Find')
        Find.pack(side=LEFT)

        Label(fram, text="Replace With ").pack(side=LEFT)

        edit2 = Entry(fram)
        edit2.pack(side=LEFT, fill=BOTH, expand=1)
        edit2.focus_set()

        replace = Button(fram, text='FindNReplace')
        replace.pack(side=LEFT)

        fram.pack(side=TOP)

        # text box in root window
        text = Text(root)

        # text input area at index 1 in text window
        text.insert('1.0', strn)
        text.pack(side=BOTTOM)

        # function to search string in text
        def find():
            # remove tag 'found' from index 1 to END
            text.tag_remove('found', '1.0', END)

            # returns to widget currently in focus
            s = edit.get()

            if (s):
                idx = '1.0'
                while 1:
                    # searches for desried string from index 1
                    idx = text.search(s, idx, nocase=1,
                                      stopindex=END)

                    if not idx: break
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(s))

                    # overwrite 'Found' at idx
                    text.tag_add('found', idx, lastidx)
                    idx = lastidx

                    # mark located string as red

                text.tag_config('found', foreground='red')
            edit.focus_set()

        def findNreplace():
            # remove tag 'found' from index 1 to END
            text.tag_remove('found', '1.0', END)

            # returns to widget currently in focus
            s = edit.get()
            r = edit2.get()

            if (s and r):
                idx = '1.0'
                while 1:
                    # searches for desried string from index 1
                    idx = text.search(s, idx, nocase=1,
                                      stopindex=END)
                    print(idx)
                    if not idx: break

                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(s))

                    text.delete(idx, lastidx)
                    text.insert(idx, r)

                    lastidx = '% s+% dc' % (idx, len(r))

                    # overwrite 'Found' at idx
                    text.tag_add('found', idx, lastidx)
                    idx = lastidx

                    # mark located string as red
                text.tag_config('found', foreground='green', background='yellow')
            edit.focus_set()

        Find.config(command=find)
        replace.config(command=findNreplace)

        # mainloop function calls the endless
        # loop of the window, so the window will
        # wait for any user interaction till we
        # close it
        #root.mainloop()



    def __wordCount(self):
        strn=self.__thisTextArea.get(1.0,END)
        res=0
        res = len(strn.split())
        showinfo("Total words:         is/are ",res)
        # print(res)


    def __charCount(self):
        strn = self.__thisTextArea.get(1.0, END)
        res = 0
        for w in strn:
            if w=="\n" or w==" ":
                continue
            else:
                res+=1
        showinfo("Total Chars:         is/are ", res)

    def __CreatedTime(self):
        t = time.ctime(os.path.getctime(os.path.basename(self.__file)))
        ct_time = tkinter.Label(ct_frame, text=t)
        showinfo("Created Time:         is ", ct_time)

    def __modifiedTime(self):
        pass


    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.__root.mainloop()

    # Run main application


notepad = Notepad(width=600, height=400)
notepad.run()