import wx
import wx.adv

class Starter(wx.Frame):

    def __init__(self, *args, **kw):
        super(Starter, self).__init__(*args, **kw, size=(600,600))

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        txt1 = '''Welcome To'''

        txt2 = '''V.O.I.D'''
        font = wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        heading = wx.StaticText(self, label = txt1, pos = (260, 75), size=(140, -1))
        font_1 = wx.Font(49, wx.DEFAULT, wx.SLANT, wx.BOLD)
        heading_1 = wx.StaticText(self, label = txt2, pos = (200, 90), size=(200, -1))

        heading.SetFont(font)
        heading_1.SetFont(font_1)

        txt3 = '''Press Any Button To Continue'''

        txt4 = '''Virtual Operation In Dissension'''

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()

        font_2 = wx.Font(19, wx.DEFAULT, wx.SLANT, wx.LIGHT)
        heading_2 = wx.StaticText(self, label = txt3, pos = (140, 295), size=(170, -1))
        font_3 = wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        heading_3 = wx.StaticText(self, label = txt4, pos = (392, 520), size=(140, -1))
        
        heading_2.SetFont(font_2)
        heading_3.SetFont(font_3)

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


        
        vbox = wx.BoxSizer(wx.VERTICAL)
   
  
        pnl.SetSizer(vbox)

        self.SetTitle('V.O.I.D')
        self.Centre()

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
        
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawLine(210, 165, 400, 165)
        dc1 = wx.PaintDC(self)
        dc1.DrawLine(210, 166, 400, 166)
        dc2 = wx.PaintDC(self)
        dc2.DrawLine(210, 167, 400, 167)
        dc3 = wx.PaintDC(self)
        dc3.DrawLine(210, 168, 400, 168)
        dc4 = wx.PaintDC(self)
        dc4.DrawLine(210, 169, 400, 169)
        dc5 = wx.PaintDC(self)
        dc5.DrawLine(210, 170, 400, 170)
        dc_1 = wx.PaintDC(self)
        dc_1.DrawLine(240, 180, 370, 180)
        dc_1_1 = wx.PaintDC(self)
        dc_1_1.DrawLine(240, 179, 370, 179)
        
        dc_2 = wx.PaintDC(self)
        dc_2.DrawLine(155, 290, 460, 290)
        dc_3 = wx.PaintDC(self)
        dc_3.DrawLine(155, 330, 460, 330)
        dc_2 = wx.PaintDC(self)
        dc_2.DrawLine(155, 289, 460, 289)
        dc_3 = wx.PaintDC(self)
        dc_3.DrawLine(155, 331, 460, 331)
        
        dc_4 = wx.PaintDC(self)
        dc_4.DrawLine(180, 275, 425, 275)
        dc_5 = wx.PaintDC(self)
        dc_5.DrawLine(180, 345, 425, 345)




def main():
    
    app = wx.App()
    ex = Starter(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
