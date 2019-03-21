import wx
import wx.adv
import pygame
import sqlite3
import time
import random
import zipfile

class Front(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        self.SetSize((600, 600))

        tekst = 'VOID'
        txt = 'Welcome To'
        txt2 = 'Press The Button To Continue'
        txt3 = 'Virtual Operation In Dissension' 
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, txt, (340, 75)).SetFont(font)
        font_2 = wx.Font(49, wx.DEFAULT, wx.SLANT, wx.BOLD)
        wx.StaticText(self, -1, tekst, (300, 90)).SetFont(font_2)
        font_3 = wx.Font(19, wx.DEFAULT, wx.SLANT, wx.LIGHT)
        wx.StaticText(self, -1, txt2, (210, 295)).SetFont(font_3)
        font_4 = wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt3, (582, 520)).SetFont(font_4)

        self.btn = wx.Button(self, -1, 'Here', (341, 370))
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    
    def OnPaint(self, e):
        dc1 = wx.PaintDC(self)
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
        


class Sign(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        tekst = 'Sign Up'
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, tekst, (280, 60)).SetFont(font)


        self.btn = wx.Button(self, -1, 'Register', (345, 300), (120, 50))
        self.btn1 = wx.Button(self, -1, 'Login', (345, 360), (120, 50))
        self.btn2 = wx.Button(self, -1, 'Return', (50, 480))

class Login(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        vbox = wx.BoxSizer(wx.VERTICAL) 
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        txt = 'Login'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt, (295, 60)).SetFont(font)
        

        font_1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        wx.StaticText(self, -1, 'Enter Username:', (195, 220), (120, 80)).SetFont(font_1)
        wx.StaticText(self, -1, 'Enter Password:', (200, 270), (120, 80)).SetFont(font_1)
        
		
         
        self.t2 = wx.TextCtrl(self, pos = (380, 270), size = (180, 35), style=wx.TE_PASSWORD)
        self.t2.SetFont(font_2)
        self.t3 = wx.TextCtrl(self, pos = (380, 220), size = (180, 35))
        self.t3.SetFont(font_2)
        self.t2.SetMaxLength(12)
        self.t3.SetMaxLength(15)
		
        
        self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        self.t3.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        

        self.btn = wx.Button(self, -1, 'Return', (50, 480))
        self.btn2 = wx.Button(self, -1, 'Continue', (440, 380), (120, 50))
        self.btn2.SetFont(font_2)

    def OnMaxLen(self,event):
        print ('Maximum length reached')

class Register(wx.Panel):



    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        vbox = wx.BoxSizer(wx.VERTICAL) 
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        add = False
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
        self.t3 = wx.TextCtrl(self, pos = (380, 270), size = (180, 35), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.t3.SetFont(font_2)
        self.t4 = wx.TextCtrl(self, pos = (380, 310), size = (180, 35), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.t4.SetFont(font_2)
        self.t2.SetMaxLength(15)
        self.t3.SetMaxLength(12)
        self.t4.SetMaxLength(12)
        
		
        
        self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        self.t3.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        self.t4.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)

        self.t2.Bind(wx.EVT_TEXT_ENTER,self.Enter)
        self.t3.Bind(wx.EVT_TEXT_ENTER,self.Enter)
        self.t4.Bind(wx.EVT_TEXT_ENTER,self.Enter)
        

        self.btn = wx.Button(self, -1, 'Return', (50, 480))
        self.btn2 = wx.Button(self, -1, 'Continue', (440, 380), (120, 50))
        self.btn2.SetFont(font_2)
        self.btn2.Bind(wx.EVT_BUTTON,self.Enter)

    def Enter(self, event):
        x = str(self.t2.GetValue())
        y = str(self.t3.GetValue())
        z = str(self.t4.GetValue())
        if len(x) < 2 or len(y) < 5:
            wx.MessageBox('Too Short', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        else:
            if y != z:
                wx.MessageBox('Passwords Do Not Match', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
            else:
                pass

    def OnMaxLen(self,event):
        
        wx.MessageBox('Max Length Reached', 'Info',
            wx.OK | wx.ICON_INFORMATION)

        
        


class MainMenu(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent)
        txt = 'Main Menu'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (225, 60)).SetFont(font)
        txt2 = '''Game
Modes'''
        txt3 = 'Summon'
        txt4 = 'Options'
        txt1 = 'Crafting'
        txt5 = '''Rules/
Help'''
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt2, (210, 205), (120, 65))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt3, (430, 205), (120, 65))
        self.btn2.SetFont(font_2)
        self.btn3 = wx.Button(self, -1, txt1, (320, 295), (120, 65))
        self.btn3.SetFont(font_2)
        self.btn4 = wx.Button(self, -1, txt5, (210, 385), (120, 65))
        self.btn4.SetFont(font_2)
        self.btn5 = wx.Button(self, -1, txt4, (430, 385), (120, 65))
        self.btn5.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'LOG OUT', (50, 480))
        

class Tech(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        txt = 'Thanks For Playing'
        txt1 = 'さようなら'
        txt2 = 'Sayōnara'
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt, (175, 120)).SetFont(font)
        font_1 = wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, txt1, (325, 340)).SetFont(font_1)
        font_2 = wx.Font(23, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, txt2, (325, 380)).SetFont(font_2)
        
        txt3 = ''' Main Menu
Return'''
        self.btn = wx.Button(self, -1, 'LOG OUT', (335, 480))
        self.btn2 = wx.Button(self, -1, txt3, (530, 465), (90, 50))
    
class Program(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'V.O.I.D')

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        self.panel_one = Front(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)
        
        self.panel_two = Sign(self)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn2.Bind(wx.EVT_BUTTON, self.show_panel_one)
        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.show_panel_four)
        self.panel_two.btn1.Bind(wx.EVT_BUTTON, self.show_panel_three)
        self.panel_two.Hide()
        
        self.panel_three = Login(self)
        sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.panel_three.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)
        self.panel_three.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five1)
        self.panel_three.Hide()

        self.panel_four = Register(self)
        sizer.Add(self.panel_four, 1, wx.EXPAND)
        self.panel_four.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)
        self.panel_four.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five)
        self.panel_four.Hide()

        self.panel_five = MainMenu(self)
        sizer.Add(self.panel_five, 1, wx.EXPAND)
        a=0
    
        self.panel_five.btn.Bind(wx.EVT_BUTTON, self.Message)
        self.panel_five.Hide()

        self.panel_six = Tech(self)
        sizer.Add(self.panel_six, 1, wx.EXPAND)
        self.panel_six.btn.Bind(wx.EVT_BUTTON, self.show_panel_one)
        self.panel_six.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five2)
        self.panel_six.Hide()

        
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

    def Clear(self,event):
        self.panel_four.t2.Clear()

    def Message(self, event):
        ans = wx.MessageDialog(self, 'Are You Sure You Want To Log Out?', 'Log Out',
                      wx.YES_NO | wx.ICON_EXCLAMATION)
        ret = ans.ShowModal()
        ans.Destroy()
        if ret == wx.ID_YES:
            self.panel_five.Show()
            self.panel_two.Hide()
            self.panel_one.Hide()
            self.panel_three.Hide()
            self.panel_four.Hide()
            self.panel_six.Hide()
            self.panel_five.btn.Bind(wx.EVT_BUTTON, self.show_panel_six)
        else:
            self.panel_five.Show()
            self.panel_two.Hide()
            self.panel_one.Hide()
            self.panel_three.Hide()
            self.panel_four.Hide()
            self.panel_six.Hide()

    def show_panel_one(self, event):
        self.panel_one.Show()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()

    def show_panel_two(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_four.t2.Clear()
        self.panel_four.t3.Clear()
        self.panel_four.t4.Clear()
        self.panel_three.t2.Clear()
        self.panel_three.t3.Clear()
        self.Layout()

    def show_panel_three(self, event):
        self.panel_three.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()

    def show_panel_four(self, event):
        self.panel_four.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()

    def show_panel_five(self, event):
        x = str(self.panel_four.t2.GetValue())
        mixed = any(letter.islower() for letter in x) and any(letter.isupper() for letter in x) and x.isalnum()
        y = str(self.panel_four.t3.GetValue())
        mixed1 = any(letter.islower() for letter in y) and any(letter.isupper() for letter in y) and y.isalnum()
        z = str(self.panel_four.t4.GetValue())

        if len(x) == 0 or len(y) == 0 or len(z) == 0:
            wx.MessageBox('Something Needs To Be Entered In These Fields', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        elif len(x) < 2 or len(y) < 5:
            wx.MessageBox('Too Short', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        else:
            if not mixed or not mixed1:
                wx.MessageBox('Insufficient Login', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
            else:
                if y != z:
                    wx.MessageBox('Passwords Do Not Match', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
                else:
                    self.panel_five.Show()
                    self.panel_two.Hide()
                    self.panel_one.Hide()
                    self.panel_three.Hide()
                    self.panel_four.Hide()
                    self.panel_six.Hide()
                    self.panel_four.t2.Clear()
                    self.panel_four.t3.Clear()
                    self.panel_four.t4.Clear()
                    self.panel_three.t2.Clear()
                    self.panel_three.t3.Clear()
                    self.Layout()

    def show_panel_five1(self, event):
        x = str(self.panel_three.t2.GetValue())
        mixed = any(letter.islower() for letter in x) and any(letter.isupper() for letter in x) and x.isalnum()
        y = str(self.panel_three.t3.GetValue())
        mixed1 = any(letter.islower() for letter in y) and any(letter.isupper() for letter in y) and y.isalnum()
        #z = str(self.panel_four.t4.GetValue())

        if len(x) == 0 or len(y) == 0 or len(z) == 0:
            wx.MessageBox('Something Needs To Be Entered In These Fields', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        elif len(x) < 2 or len(y) < 5:
            wx.MessageBox('Insufficient Login', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        else:
            if not mixed or not mixed1:
                wx.MessageBox('Insufficient Login', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
            else:
               # if y != z:
               #     wx.MessageBox('Passwords Do Not Match', 'Info',
               #               wx.OK | wx.ICON_EXCLAMATION)
               # else:
                self.panel_five.Show()
                self.panel_two.Hide()
                self.panel_one.Hide()
                self.panel_three.Hide()
                self.panel_four.Hide()
                self.panel_six.Hide()
                self.panel_four.t2.Clear()
                self.panel_four.t3.Clear()
                self.panel_four.t4.Clear()
                self.panel_three.t2.Clear()
                self.panel_three.t3.Clear()
                self.Layout()
        
    def show_panel_five2(self, event):
        self.panel_five.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_six.Hide()
        self.panel_four.t2.Clear()
        self.panel_four.t3.Clear()
        self.panel_four.t4.Clear()
        self.panel_three.t2.Clear()
        self.panel_three.t3.Clear()
        self.Layout()
        
    def show_panel_six(self, event):
        self.panel_six.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
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
