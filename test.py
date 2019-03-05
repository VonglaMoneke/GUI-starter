import wx
import wx.adv

class Glowne(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        self.SetSize((600, 600))

        tekst = 'VOID'
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, tekst, (300, 10)).SetFont(font)

        self.btn = wx.Button(self, -1, "Here", (345, 300))


class Glowne1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        tekst = 'Sign Up'
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, tekst, (300, 10)).SetFont(font)

        self.btn = wx.Button(self, -1, "Register", (345, 100))
        self.btn1 = wx.Button(self, -1, "Login", (345, 120))


class Program(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Program')

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        self.panel_one = Glowne(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)
        self.panel_two = Glowne1(self)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.show_panel_one)
        self.panel_two.Hide()
        self.SetSize((800, 600))
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

    def show_panel_one(self, event):
        self.panel_one.Show()
        self.panel_two.Hide()
        self.Layout()

    def show_panel_two(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
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
