import wx
import wx.adv

class Front(wx.Panel):            #each page in the interface is a seperate class for easier implementation

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)     #this initialise the panel so that it can be used and interacted with

        self.SetSize((600, 600))           # this sets the size of the panel

        tekst = 'VOID'
        txt = 'Welcome To'
        txt2 = 'Press The Button To Continue'
        txt3 = 'Virtual Operation In Dissension' 
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)    #these are the font settings for the words that will appear on screen
        wx.StaticText(self, -1, txt, (340, 75)).SetFont(font)
        font_2 = wx.Font(49, wx.DEFAULT, wx.SLANT, wx.BOLD)
        wx.StaticText(self, -1, tekst, (300, 90)).SetFont(font_2)
        font_3 = wx.Font(19, wx.DEFAULT, wx.SLANT, wx.LIGHT)
        wx.StaticText(self, -1, txt2, (210, 295)).SetFont(font_3)
        font_4 = wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt3, (582, 520)).SetFont(font_4)

        self.btn = wx.Button(self, -1, 'Here', (341, 370))      #this is the button that will appear on the first page
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)        #this is to add a function to the page so that items can be painted on to the page
    
    def OnPaint(self, e):
        dc1 = wx.PaintDC(self)                      # these all are the lines that will be shown on the front screen
        dc1.DrawLine(300, 166, 460, 166)
        dc2 = wx.PaintDC(self)
        dc2.DrawLine(300, 167, 460, 167)
        dc3 = wx.PaintDC(self)
        dc3.DrawLine(300, 168, 460, 168)
        dc4 = wx.PaintDC(self)
        dc4.DrawLine(300, 169, 460, 169)
        dc5 = wx.PaintDC(self)
        dc5.DrawLine(300, 170, 460, 170)
        dc_1 = wx.PaintDC(self)
        dc_1.DrawLine(325, 180, 440, 180)
        dc_1_1 = wx.PaintDC(self)
        dc_1_1.DrawLine(325, 179, 440, 179)
        
        dc_2 = wx.PaintDC(self)
        dc_2.DrawLine(205, 290, 550, 290)
        dc_3 = wx.PaintDC(self)
        dc_3.DrawLine(205, 330, 550, 330)
        dc_2 = wx.PaintDC(self)
        dc_2.DrawLine(205, 289, 550, 289)
        dc_3 = wx.PaintDC(self)
        dc_3.DrawLine(205, 331, 550, 331)
        
        dc_4 = wx.PaintDC(self)
        dc_4.DrawLine(220, 275, 535, 275)
        dc_5 = wx.PaintDC(self)
        dc_5.DrawLine(220, 345, 535, 345)
        


class Sign(wx.Panel): # this is the page for signing up

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        test = 'Sign Up'
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, test, (280, 60)).SetFont(font)


        self.btn = wx.Button(self, -1, 'Register', (345, 300), (120, 50))    #these are the buttons that will take you to the login & register pages
        self.btn1 = wx.Button(self, -1, 'Login', (345, 360), (120, 50))
        self.btn2 = wx.Button(self, -1, 'Return', (50, 480)) # this button will take you back to the previous page

class Login(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        vbox = wx.BoxSizer(wx.VERTICAL) 
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        txt = 'Login'                              #this is the text that will be used as the title for the page
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt, (295, 60)).SetFont(font)          # the static font allows the text to be added to the page as just a piece of text that does nothing
        

        font_1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        wx.StaticText(self, -1, 'Enter Username:', (195, 220), (120, 80)).SetFont(font_1)
        wx.StaticText(self, -1, 'Enter Password:', (200, 270), (120, 80)).SetFont(font_1)
        
		
        self.t3 = wx.TextCtrl(self, pos = (380, 220), size = (180, 35))    # this adds the etry boxes where the user can input their details
        self.t3.SetFont(font_2)
        self.t2 = wx.TextCtrl(self, pos = (380, 270), size = (180, 35), style=wx.TE_PASSWORD) #the style=wx.TE_PASSWORD means that whatever is entered
        self.t2.SetFont(font_2)                                                               #will have the properties of a password so it will be starred out
        self.t2.SetMaxLength(18)                                             # these set the max length for the username and password
        self.t3.SetMaxLength(12)
		
        
        self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)            #these set the events to when the max has been reached
        self.t3.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        

        self.btn = wx.Button(self, -1, 'Return', (50, 480))                                # return button
        self.btn2 = wx.Button(self, -1, 'Continue', (440, 380), (120, 50))       #continue button
        self.btn2.SetFont(font_2)

    def OnMaxLen(self,event):
        wx.MessageBox('Max Length Reached', 'Info',                    #this is a dialog box that pops up when the maximum length has been met.
            wx.OK | wx.ICON_EXCLAMATION)

class Register(wx.Panel):                              # this is the panel for the register screen

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)              # this initailises the panel so theat it can be intercated with and seen by the user 

        vbox = wx.BoxSizer(wx.VERTICAL) 
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        txt = 'Register'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt, (295, 60)).SetFont(font)
        

        font_1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        wx.StaticText(self, -1, 'Enter Username:', (195, 220), (120, 80)).SetFont(font_1)
        wx.StaticText(self, -1, 'Enter Password:', (200, 270), (120, 80)).SetFont(font_1)
        wx.StaticText(self, -1, 'Re-Enter Password:', (162, 310), (120, 80)).SetFont(font_1)
        
		
         
        
        self.t2 = wx.TextCtrl(self, pos = (380, 220), size = (180, 35), style=wx.TE_PROCESS_ENTER)
        self.t2.SetFont(font_2)
        self.t3 = wx.TextCtrl(self, pos = (380, 270), size = (180, 35), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER) # the wx.TE_PROCESS_ENTER means that something will
        self.t3.SetFont(font_2)                                                                                     # happen when you press the enter button
        self.t4 = wx.TextCtrl(self, pos = (380, 310), size = (180, 35), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.t4.SetFont(font_2)
        self.t2.SetMaxLength(12)
        self.t3.SetMaxLength(18)
        self.t4.SetMaxLength(18)
        
		
        
        self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        self.t3.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        self.t4.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)

        self.t2.Bind(wx.EVT_TEXT_ENTER,self.Enter)          # this binds the enter button press to an event
        self.t3.Bind(wx.EVT_TEXT_ENTER,self.Enter)           
        self.t4.Bind(wx.EVT_TEXT_ENTER,self.Enter)
        

        self.btn = wx.Button(self, -1, 'Return', (50, 480))
        self.btn2 = wx.Button(self, -1, 'Continue', (440, 380), (120, 50))
        self.btn2.SetFont(font_2)
        self.btn2.Bind(wx.EVT_BUTTON,self.Enter)        # I binded the continue button to do the same thing as when you press the enter button

    def Enter(self, event):
        x = str(self.t2.GetValue())         # this gets whatever has been entered and makes it a string
        y = str(self.t3.GetValue())
        z = str(self.t4.GetValue())
        if len(x) < 2 or len(y) < 5:          # as it string now the length can be checked, this is the way to validate the username and the password
            wx.MessageBox('Too Short', 'Info',                  # brings up a dialog box to say that whatever was entered is too short.
                          wx.OK | wx.ICON_EXCLAMATION)
        else:
            if y != z:                               # this is for the 2 passwords to see if they match each other
                wx.MessageBox('Passwords Do Not Match', 'Info',        # brings up a dialog box to say that the 2 passwords don't match
                          wx.OK | wx.ICON_EXCLAMATION)
            else:
                pass

    def OnMaxLen(self,event):
        
        wx.MessageBox('Max Length Reached', 'Info',
            wx.OK | wx.ICON_EXCLAMATION)


class Program(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'V.O.I.D')

        sizer = wx.BoxSizer()
        self.SetSize((600,600))
        self.SetSizer(sizer)
        self.Centre()
        menu = wx.MenuBar()

        about = wx.Menu()
        about.Append(wx.ID_ANY, '&Info')
        about.Bind(wx.EVT_MENU, self.OnAbout)
        menu.Append(about, '&Help')
        self.SetMenuBar(menu)
        
        file = wx.Menu()
        item = file.Append(wx.ID_EXIT, 'Quit Game')
        menu.Append(file, '&Exit')
        self.SetMenuBar(menu)
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        self.panel_one = Front(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)
        
        self.panel_two = Sign(self)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn2.Bind(wx.EVT_BUTTON, self.show_panel_one)
##        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.show_panel_four)
        self.panel_two.btn1.Bind(wx.EVT_BUTTON, self.show_panel_three)
        self.panel_two.Hide()

        self.panel_three = Login(self)
        sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.panel_three.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)
##        self.panel_three.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five1)
        self.panel_three.Hide()
        
        self.SetSize((800, 600))
        

    def show_panel_one(self, event):
        self.panel_one.Show()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.Layout()

    def show_panel_two(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.Layout()
    def show_panel_three(self, event):
        self.panel_three.Show()
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.Layout()
        
    def OnAbout(self, e):

        text = '''                             This is the VOID (Virtual Operation In Dissension);
This essentially is a plaform for where players can choose charcters from a vast amount of
Pop culture series such as anime or video games where they will fight against each other,
                                       Where it couldn't be possible other wise.
                                                        Thanks For Playing.
'''
        licence = '''VOID is a free to play game; so it is for the people instead of the profit.
          This is a product that can be redistributed anywhere although,
        It cannot be modified with a Public Licence.
'''

        info = wx.adv.AboutDialogInfo()

        #info.SetIcon(wx.Icon('logo.png', wx.BITMAP_TYPE_PNG))
        info.SetName('V.O.I.D')
        info.SetVersion('1.0.1')
        info.SetDescription(text)
        info.SetCopyright('(C) 2019 Chris Moneke')
        info.SetWebSite('https://www.cyberVOID.co.uk')
        info.SetLicence(licence)
        info.AddDeveloper('Chris Moneke')
        info.AddDocWriter(''' These are the Stakeholders that have been involved with this game:
Emmanuel , Octavia, Nappy, Light, Ken
''')
        info.AddArtist('''Chris Moneke with thanks from:
https://www.piskelapp.com''')

        wx.adv.AboutBox(info)

    def OnQuit(self,e):
        self.Close()
        
if __name__ == "__main__":
    app = wx.App(False)
    frame = Program()
    frame.Show()
    app.MainLoop()

#
