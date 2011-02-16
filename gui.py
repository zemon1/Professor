from Tkinter import *

class GUIFramework(Frame):
    """This is the GUI"""
    
    __slots__ = ("content")
    
    def __init__(self,master=None):
        """Initialize"""
        
        """Initialize the base class"""
        Frame.__init__(self,master)
        
        """Display the main window"""
        self.grid()
        
        """Create the Text"""
        self.createWidgets()
    
    def createWidgets(self):
        self.lbText = Label(self, text=self.content)
        self.lbText.grid(row=0, column=0)

                
if __name__ == "__main__":
    guiFrame = GUIFramework("con")
    guiFrame.mainloop()