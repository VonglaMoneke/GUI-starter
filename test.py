import wx
import wx.adv
import pygame
import sqlite3
import time
import random
import zipfile
import os

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
        self.t3 = wx.TextCtrl(self, pos = (380, 270), size = (180, 35), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER) # the wx.TE_PROCESS_ENTER means 
        self.t3.SetFont(font_2)                                                                                     #that something will                               
        self.t4 = wx.TextCtrl(self, pos = (380, 310), size = (180, 35), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER) # happen when you press 
        self.t4.SetFont(font_2)                                                                                     #the enter button
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

class MainMenu(wx.Panel):           # this is the panel for the main menu

    def __init__(self, parent):

        wx.Panel.__init__(self, parent)    #this initialises the main menu panel
        txt = 'Main Menu'                 #this is the title
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD) #sets the font for the text
        
        wx.StaticText(self, -1, txt, (225, 60)).SetFont(font)
        txt1 = '''Game
Modes'''
        txt2 = 'Summon'                               #these are the text that will be on the buttons
        txt3 = 'Crafting'
        txt4 = '''Rules/
Help'''
        txt5 = 'Options'
        
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (160, 205), (140, 75))     #this sets the buttons and their positions on the pages 
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (490, 205), (140, 75))
        self.btn2.SetFont(font_2)
        self.btn3 = wx.Button(self, -1, txt3, (325, 265), (140, 75))
        self.btn3.SetFont(font_2)
        self.btn4 = wx.Button(self, -1, txt4, (160, 325), (140, 75))
        self.btn4.SetFont(font_2)
        self.btn5 = wx.Button(self, -1, txt5, (490, 325), (140, 75))
        self.btn5.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'LOG OUT', (50, 480)) # this is the log out button it is very similar to the return button
        

class Tech(wx.Panel):  # this is the page is the page that is inbetween the main menu and the intro page, when you log out
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
        self.btn2 = wx.Button(self, -1, txt3, (530, 465), (90, 50))      # this button should take you back to the main menu

class GameModes(wx.Panel):            
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Game Modes'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (200, 60)).SetFont(font)
        txt1 = '''Single
Player'''
        txt2 = '''Multi
Player'''
        font_2 = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (230, 205), (110, 225))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (390, 205), (110, 225))
        self.btn2.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

class SinglePlayer(wx.Panel):

    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Single Player'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        wx.StaticText(self, -1, txt, (200, 60)).SetFont(font)
        txt1 = '''Story
Mode'''
        txt2 = '''Player
vs
AI'''
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (230, 205), (110, 205))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (390, 205), (110, 205))
        self.btn2.SetFont(font_2)

        self.cb1 = wx.CheckBox(self, label = 'Easy',pos = (250,420), size = (80,60))   # this creates 3 checkboxes on the screen  
        self.cb2 = wx.CheckBox(self, label = 'Medium',pos = (340,420), size = (80,60)) #these are for the 3 difficulties  
        self.cb3 = wx.CheckBox(self, label = 'Hard',pos = (430,420), size = (80,60))

        self.cb1.Bind(wx.EVT_CHECKBOX,self.onChecked)      #these binds the checkboxes to different events
        self.cb2.Bind(wx.EVT_CHECKBOX,self.onChecked1)
        self.cb3.Bind(wx.EVT_CHECKBOX,self.onChecked2)

        font_3 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.cb1.SetFont(font_3)
        self.cb2.SetFont(font_3)
        self.cb3.SetFont(font_3)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

    def onChecked(self, event):    # all of these three functions are used to make sure that only one checkbox can be checked at one time
        cb = event.GetEventObject()     # this gets gets the checkbox in question
        q = cb.IsChecked()            # this function checks if the checkbox has been cheked
        if q == True:
            self.cb2.SetValue(False)   # this sets the other two checkboxes to be false so they aren't checked
            self.cb3.SetValue(False)
    def onChecked1(self, event):
        cb = event.GetEventObject()
        q = cb.IsChecked()
        if q == True:
            self.cb1.SetValue(False)
            self.cb3.SetValue(False)
    def onChecked2(self, event):
        cb = event.GetEventObject()
        q = cb.IsChecked()
        if q == True:
            self.cb2.SetValue(False)
            self.cb1.SetValue(False)

class MultiPlayer(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Multi Player'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (240, 60)).SetFont(font)
        txt1 = '''Player-2-Player'''
        txt2 = '''Leaderboard'''
        
        font_2 = wx.Font(19, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (245, 235), (270, 65))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (245, 325), (270, 65))
        self.btn2.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

class Player2Player(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Player 2 Player'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (190, 60)).SetFont(font)
        txt1 = '''Online'''
        txt2 = '''Friends'''
        
        font_2 = wx.Font(19, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (255, 235), (250, 65))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (255, 325), (250, 65))
        self.btn2.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

class Summon(wx.Panel):

    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Summon'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (235, 60)).SetFont(font)
        txt1 = '''Disc'''
        txt2 = '''Card'''
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (230, 245), (110, 75))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (390, 245), (110, 75))
        self.btn2.SetFont(font_2)

        self.cb1 = wx.CheckBox(self, label = 'Single',pos = (280,370), size = (80,60))  # adds the checkboxes to the page
        self.cb2 = wx.CheckBox(self, label = 'Multi',pos = (420,370), size = (80,60))

        self.cb1.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.cb2.Bind(wx.EVT_CHECKBOX,self.onChecked1)

        font_3 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.cb1.SetFont(font_3)
        self.cb2.SetFont(font_3)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

    def onChecked(self, event):      # only one check box at a time
        cb = event.GetEventObject()
        q = cb.IsChecked()
        if q == True:
            self.cb2.SetValue(False)    #sets the other checkbox to false
    def onChecked1(self, event):
        cb = event.GetEventObject()
        q = cb.IsChecked()
        if q == True:
            self.cb1.SetValue(False)

class Craft(wx.Panel):

    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Craft'
        
        font = wx.Font(46, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (285, 60)).SetFont(font)
        txt1 = '''Deck'''
        txt2 = '''Team'''
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (230, 245), (110, 75))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (390, 245), (110, 75))
        self.btn2.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))
        
class Options(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Options'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (260, 60)).SetFont(font)
        txt1 = '''Resolution'''
        txt2 = '''Sound'''
        txt3 = '''Colour Options'''
        
        font_2 = wx.Font(19, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (245, 195), (270, 65))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (245, 285), (270, 65))
        self.btn2.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt3, (245, 375), (270, 65))
        self.btn2.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

class RulesHelp(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent)
        txt = 'Rules/Help'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (245, 60)).SetFont(font)
        txt1 = '''Warnings'''
        txt2 = '''Extra
Info'''
        txt3 = 'Controls'
        txt4 = 'Achievements'
        txt5 = '''Resource
System'''
        txt6 = '''Rating
System'''
        font_2 = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (150, 205), (140, 75))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (315, 205), (140, 75))
        self.btn2.SetFont(font_2)
        self.btn3 = wx.Button(self, -1, txt3, (480, 205), (140, 75))
        self.btn3.SetFont(font_2)
        self.btn4 = wx.Button(self, -1, txt4, (150, 345), (140, 75))
        self.btn4.SetFont(font_2)
        self.btn5 = wx.Button(self, -1, txt5, (315, 345), (140, 75))
        self.btn5.SetFont(font_2)
        self.btn6 = wx.Button(self, -1, txt6, (480, 345), (140, 75))
        self.btn6.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))
        
class ExtraInfo(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Extra Info.'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (240, 60)).SetFont(font)
        txt1 = '''Hall
Of
Fame'''
        txt2 = '''Summon
History'''
        txt3 = '''Personal
Info'''
        font_2 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (230, 205), (110, 230))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (390, 205), (110, 90))
        self.btn2.SetFont(font_2)
        self.btn3 = wx.Button(self, -1, txt3, (390, 305), (110, 125))
        self.btn3.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

class PersonalInfo(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Personal Info'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (200, 60)).SetFont(font)
        txt1 = '''Records'''
        txt2 = '''User
ID'''
        txt3 = '''Time
Played'''
        font_2 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (230, 205), (110, 225))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (390, 205), (110, 90))
        self.btn2.SetFont(font_2)
        self.btn3 = wx.Button(self, -1, txt3, (390, 305), (110, 125))
        self.btn3.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))

class HallOfFame(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        txt = 'Hall Of Fame'
        
        font = wx.Font(42, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        wx.StaticText(self, -1, txt, (210, 60)).SetFont(font)
        txt1 = '''Stats'''
        txt2 = '''Character
Info'''
        txt3 = '''Ability
Card
Info'''
        font_2 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        
        self.btn1 = wx.Button(self, -1, txt1, (200, 195), (95, 250))
        self.btn1.SetFont(font_2)
        self.btn2 = wx.Button(self, -1, txt2, (325, 195), (115, 250))
        self.btn2.SetFont(font_2)
        self.btn3 = wx.Button(self, -1, txt3, (475, 195), (95, 250))
        self.btn3.SetFont(font_2)

        self.btn = wx.Button(self, -1, 'Return', (50, 480))



        
class Program(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'V.O.I.D', style= wx.MINIMIZE_BOX     # this makes that within the frame only the minimise button can be used
	| wx.SYSTEM_MENU | wx.CAPTION)

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        songs = []  # this is the list to hold all the songs used

        global intro
        intro = []
        global main_menu
        main_menu = []
        global matches
        matches = []
        global sign_up
        sign_up = []
        global craft
        craft = []
        global summon
        summon = []
        global story
        story = []

        global conn
        global c

        conn = sqlite3.connect('details.db')
        c = conn.cursor()

        def create_table():
            c.execute('CREATE TABLE IF NOT EXISTS account(Username TEXT, Password TEXT)')

        pygame.init()

        create_table()

        def direct():
            dialog = wx.DirDialog(None, "Choose a directory for MUSIC:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dialog.ShowModal() == wx.ID_OK:
                direct = dialog.GetPath()
            dialog.Destroy()
            os.chdir(direct)

            for files in os.listdir(direct):
                if files.endswith('.mp3'):

                    songs.append(files)

        direct()

        x = 0
        while x != 30:
            if x == 2 or x==4:
                main_menu.append(songs[x])
            elif x == 14:
                story.append(songs[x])
            elif x == 11:
                summon.append(songs[x])
            elif x == 15:
                intro.append(songs[x])
            elif x == 13:
                sign_up.append(songs[x])
                story.append(songs[x])
            elif x == 19:
                craft.append(songs[x])
            else:
                matches.append(songs[x])
            x = x+1

        myorder = [1,0]
        main_menu = [main_menu[i] for i in myorder]
        story = [story[i] for i in myorder]

        pygame.mixer.init()
        pygame.mixer.music.load(intro[0])
        pygame.mixer.music.play()

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
        self.panel_three.btn.Bind(wx.EVT_BUTTON, self.show_panel_two1)
        self.panel_three.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five1)
        self.panel_three.Hide()

        self.panel_four = Register(self)
        sizer.Add(self.panel_four, 1, wx.EXPAND)
        self.panel_four.btn.Bind(wx.EVT_BUTTON, self.show_panel_two1)
        self.panel_four.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five)
        self.panel_four.Hide()

        

        self.panel_six = Tech(self)
        sizer.Add(self.panel_six, 1, wx.EXPAND)
        self.panel_six.btn.Bind(wx.EVT_BUTTON, self.show_panel_one)
        self.panel_six.btn2.Bind(wx.EVT_BUTTON, self.show_panel_five2)
        self.panel_six.Hide()

        self.panel_five = MainMenu(self)
        sizer.Add(self.panel_five, 1, wx.EXPAND)
        self.panel_five.btn.Bind(wx.EVT_BUTTON, self.Message)
        self.panel_five.btn1.Bind(wx.EVT_BUTTON, self.show_panel_seven)
        self.panel_five.btn2.Bind(wx.EVT_BUTTON, self.show_panel_XI)
        self.panel_five.btn3.Bind(wx.EVT_BUTTON, self.show_panel_XII)
        self.panel_five.btn4.Bind(wx.EVT_BUTTON, self.show_panel_XIV)
        self.panel_five.btn5.Bind(wx.EVT_BUTTON, self.show_panel_XIII)
        self.panel_five.Hide()

        self.panel_seven = GameModes(self)
        sizer.Add(self.panel_seven, 1, wx.EXPAND)
        self.panel_seven.btn.Bind(wx.EVT_BUTTON, self.show_panel_five3)
        self.panel_seven.btn1.Bind(wx.EVT_BUTTON, self.show_panel_eight)
        self.panel_seven.btn2.Bind(wx.EVT_BUTTON, self.show_panel_nine)
        self.panel_seven.Hide()

        self.panel_eight = SinglePlayer(self)
        sizer.Add(self.panel_eight, 1, wx.EXPAND)
        self.panel_eight.btn.Bind(wx.EVT_BUTTON, self.show_panel_seven)
        self.panel_eight.Hide()

        self.panel_nine = MultiPlayer(self)
        sizer.Add(self.panel_nine, 1, wx.EXPAND)
        self.panel_nine.btn.Bind(wx.EVT_BUTTON, self.show_panel_seven)
        self.panel_nine.btn1.Bind(wx.EVT_BUTTON, self.show_panel_X)
        self.panel_nine.Hide()

        self.panel_X = Player2Player(self)
        sizer.Add(self.panel_X, 1, wx.EXPAND)
        self.panel_X.btn.Bind(wx.EVT_BUTTON, self.show_panel_nine)
        self.panel_X.Hide()

        self.panel_XI = Summon(self)
        sizer.Add(self.panel_XI, 1, wx.EXPAND)
        self.panel_XI.btn.Bind(wx.EVT_BUTTON, self.show_panel_five2)
        self.panel_XI.Hide()

        self.panel_XII = Craft(self)
        sizer.Add(self.panel_XII, 1, wx.EXPAND)
        self.panel_XII.btn.Bind(wx.EVT_BUTTON, self.show_panel_five2)
        self.panel_XII.Hide()

        self.panel_XIII = Options(self)
        sizer.Add(self.panel_XIII, 1, wx.EXPAND)
        self.panel_XIII.btn.Bind(wx.EVT_BUTTON, self.show_panel_five2)
        self.panel_XIII.Hide()

        self.panel_XIV = RulesHelp(self)
        sizer.Add(self.panel_XIV, 1, wx.EXPAND)
        self.panel_XIV.btn.Bind(wx.EVT_BUTTON, self.show_panel_five3)
        self.panel_XIV.btn2.Bind(wx.EVT_BUTTON, self.show_panel_XV)
        self.panel_XIV.Hide()

        self.panel_XV = ExtraInfo(self)
        sizer.Add(self.panel_XV, 1, wx.EXPAND)
        self.panel_XV.btn.Bind(wx.EVT_BUTTON, self.show_panel_XIV)
        self.panel_XV.btn1.Bind(wx.EVT_BUTTON, self.show_panel_XVII)
        self.panel_XV.btn3.Bind(wx.EVT_BUTTON, self.show_panel_XVI)
        self.panel_XV.Hide()

        self.panel_XVI = PersonalInfo(self)
        sizer.Add(self.panel_XVI, 1, wx.EXPAND)
        self.panel_XVI.btn.Bind(wx.EVT_BUTTON, self.show_panel_XV)
        self.panel_XVI.Hide()

        self.panel_XVII = HallOfFame(self)
        sizer.Add(self.panel_XVII, 1, wx.EXPAND)
        self.panel_XVII.btn.Bind(wx.EVT_BUTTON, self.show_panel_XV)
        self.panel_XVII.Hide()



        
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

        debug = wx.Menu()
        debug.Append(wx.ID_ANY, '&Main &Menu')
        debug.Bind(wx.EVT_MENU, self.show_panel_five2)
        menu.Append(debug, '&Debug')
        self.SetMenuBar(menu)
        

    def Clear(self,event):
        self.panel_four.t2.Clear()

    def Message(self, event):
        def show_panel_six(self, event):
            self.panel_six.Show()
            self.panel_two.Hide()
            self.panel_one.Hide()
            self.panel_three.Hide()
            self.panel_four.Hide()
            self.panel_five.Hide()
            self.panel_seven.Hide()
            self.panel_eight.Hide()
            self.panel_nine.Hide()
            self.panel_X.Hide()
            self.panel_XI.Hide()
            self.panel_XII.Hide()
            self.panel_XIII.Hide()
            self.panel_XIV.Hide()
            self.panel_XV.Hide()
            self.panel_XVI.Hide()
            self.panel_XVII.Hide()
            self.Layout()
        ans = wx.MessageDialog(self, 'Are You Sure You Want To Log Out?', 'Log Out',
                      wx.YES_NO | wx.ICON_EXCLAMATION)
        ret = ans.ShowModal()
        ans.Destroy()
        if ret == wx.ID_YES:
            self.show_panel_six(event)
        else:
            self.panel_five.Show()
            self.panel_two.Hide()
            self.panel_one.Hide()
            self.panel_three.Hide()
            self.panel_four.Hide()
            self.panel_six.Hide()
            self.panel_seven.Hide()
            self.panel_eight.Hide()
            self.panel_nine.Hide()
            self.panel_X.Hide()
            self.panel_XI.Hide()
            self.panel_XII.Hide()
            self.panel_XIII.Hide()
            self.panel_XIV.Hide()
            self.panel_XV.Hide()
            self.panel_XVI.Hide()
            self.panel_XVII.Hide()

    def show_panel_one(self, event):
        pygame.mixer.music.stop()
        self.panel_one.Show()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        pygame.mixer.init()
        pygame.mixer.music.load(intro[0])
        pygame.mixer.music.play()
        self.Layout()

    def show_panel_two(self, event):
        pygame.mixer.music.stop()
        self.panel_two.Show()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.panel_four.t2.Clear()
        self.panel_four.t3.Clear()
        self.panel_four.t4.Clear()
        self.panel_three.t2.Clear()
        self.panel_three.t3.Clear()
        pygame.mixer.init()
        pygame.mixer.music.load(sign_up[0])
        pygame.mixer.music.play()
        self.Layout()

    def show_panel_two1(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
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
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_four(self, event):
        self.panel_four.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_five(self, event):
        x = str(self.panel_four.t2.GetValue())
        mixed = any(letter.islower() for letter in x) and any(letter.isupper() for letter in x) and any(letter.isdigit() for letter in x)
        y = str(self.panel_four.t3.GetValue())
        mixed1 = any(letter.islower() for letter in y) and any(letter.isupper() for letter in y) and any(letter.isdigit() for letter in y)
        z = str(self.panel_four.t4.GetValue())

        if len(x) == 0 or len(y) == 0 or len(z) == 0:
            wx.MessageBox('Something Needs To Be Entered In These Fields', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        elif len(x) < 3 or len(y) < 5:
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
                    def new_user():
                        x = str(self.panel_four.t2.GetValue())
                        y = str(self.panel_four.t3.GetValue())

                        find_user = ('SELECT * FROM account WHERE Username = ?')
                        c.execute(find_user,[(x)])
                        if c.fetchall():
                            wx.MessageBox('Username Has Been Taken', 'Info',
                                          wx.OK | wx.ICON_EXCLAMATION)
                            self.panel_four.Show()
                            self.panel_two.Hide()
                            self.panel_one.Hide()
                            self.panel_three.Hide()
                            self.panel_five.Hide()
                            self.panel_six.Hide()
                            self.panel_seven.Hide()
                            self.panel_eight.Hide()
                            self.panel_nine.Hide()
                            self.panel_X.Hide()
                            self.panel_XI.Hide()
                            self.panel_XII.Hide()
                            self.panel_XIII.Hide()
                            self.panel_XIV.Hide()
                            self.panel_XV.Hide()
                            self.panel_XVI.Hide()
                            self.panel_XVII.Hide()
                            self.Layout()

                        else:
                            wx.MessageBox('Account Has Been Created', 'Success',
                                          wx.OK | wx.ICON_INFORMATION)
                            c.execute('INSERT INTO account (Username, Password) VALUES (?,?)',
                                      (x, y))
                            conn.commit()
                            pygame.mixer.music.stop()                    
                            self.panel_five.Show()
                            self.panel_two.Hide()
                            self.panel_one.Hide()
                            self.panel_three.Hide()
                            self.panel_four.Hide()
                            self.panel_six.Hide()
                            self.panel_seven.Hide()
                            self.panel_eight.Hide()
                            self.panel_nine.Hide()
                            self.panel_X.Hide()
                            self.panel_XI.Hide()
                            self.panel_XII.Hide()
                            self.panel_XIII.Hide()
                            self.panel_XIV.Hide()
                            self.panel_XV.Hide()
                            self.panel_XVI.Hide()
                            self.panel_XVII.Hide()
                            self.panel_four.t2.Clear()
                            self.panel_four.t3.Clear()
                            self.panel_four.t4.Clear()
                            self.panel_three.t2.Clear()
                            self.panel_three.t3.Clear()
                            pygame.mixer.init()
                            pygame.mixer.music.load(main_menu[0])
                            pygame.mixer.music.queue(main_menu[1])
                            pygame.mixer.music.play()
                            self.Layout()
                    new_user()
                    

    def show_panel_five1(self, event):
        x = str(self.panel_three.t2.GetValue())
        mixed = any(letter.islower() for letter in x) and (any(letter.isupper() for letter in x)) and (any(letter.isdigit() for letter in x))
        y = str(self.panel_three.t3.GetValue())
        mixed1 = any(letter.islower() for letter in y) and any(letter.isupper() for letter in y) and (any(letter.isdigit() for letter in y))

        if len(x) == 0 or len(y) == 0:
            wx.MessageBox('Something Needs To Be Entered In These Fields', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        elif len(x) < 5 or len(y) < 3:
            wx.MessageBox('Insufficient Login', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
        else:
            if mixed == False or mixed1 == False:
                wx.MessageBox('Insufficient Login', 'Info',
                          wx.OK | wx.ICON_EXCLAMATION)
            else:
                def login():
                    x = str(self.panel_three.t2.GetValue())
                    y = str(self.panel_three.t3.GetValue())

                    find_user = ('SELECT * FROM account WHERE Username = ? and Password = ?')
                    c.execute(find_user,[(y),(x)])
                    result = c.fetchall()
                    if result:
                        pygame.mixer.music.stop()
                        self.panel_five.Show()
                        self.panel_two.Hide()
                        self.panel_one.Hide()
                        self.panel_three.Hide()
                        self.panel_four.Hide()
                        self.panel_six.Hide()
                        self.panel_seven.Hide()
                        self.panel_eight.Hide()
                        self.panel_nine.Hide()
                        self.panel_X.Hide()
                        self.panel_XI.Hide()
                        self.panel_XII.Hide()
                        self.panel_XIII.Hide()
                        self.panel_XIV.Hide()
                        self.panel_XV.Hide()
                        self.panel_XVI.Hide()
                        self.panel_XVII.Hide()
                        self.panel_four.t2.Clear()
                        self.panel_four.t3.Clear()
                        self.panel_four.t4.Clear()
                        self.panel_three.t2.Clear()
                        self.panel_three.t3.Clear()
                        pygame.mixer.init()
                        pygame.mixer.music.load(main_menu[0])
                        pygame.mixer.music.queue(main_menu[1])
                        pygame.mixer.music.play()
                        self.Layout()
                    else:
                        wx.MessageBox('Username Not Found.', 'Login',
                                      wx.OK | wx.ICON_EXCLAMATION)
                        q = 1
                        while q == 5:
                            q = q+1
                            wx.MessageBox('Attempted Login Too Many Times', 'Error',
                                      wx.OK | wx.ICON_EXCLAMATION)
                            wx.MessageBox('CLOSING PROGRAM', 'Error',
                                      wx.OK | wx.ICON_EXCLAMATION)
                            pygame.mixer.music.stop()
                            self.Close()
                        else:
                            self.panel_three.Show()
                            self.panel_two.Hide()
                            self.panel_one.Hide()
                            self.panel_four.Hide()
                            self.panel_five.Hide()
                            self.panel_six.Hide()
                            self.panel_seven.Hide()
                            self.panel_eight.Hide()
                            self.panel_nine.Hide()
                            self.panel_X.Hide()
                            self.panel_XI.Hide()
                            self.panel_XII.Hide()
                            self.panel_XIII.Hide()
                            self.panel_XIV.Hide()
                            self.panel_XV.Hide()
                            self.panel_XVI.Hide()
                            self.panel_XVII.Hide()
                            self.Layout()

                login()
                
        
    def show_panel_five2(self, event):
        self.panel_five.Show()
        pygame.mixer.music.stop()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.panel_four.t2.Clear()
        self.panel_four.t3.Clear()
        self.panel_four.t4.Clear()
        self.panel_three.t2.Clear()
        self.panel_three.t3.Clear()
        pygame.mixer.init()
        pygame.mixer.music.load(main_menu[0])
        pygame.mixer.music.queue(main_menu[1])
        pygame.mixer.music.play()
        self.Layout()

    def show_panel_five3(self, event):
        self.panel_five.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
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
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_seven(self, event):
        self.panel_seven.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_eight(self, event):
        self.panel_eight.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_nine(self, event):
        self.panel_nine.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_X(self, event):
        self.panel_X.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_XI(self, event):
        pygame.mixer.music.stop()
        self.panel_XI.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        pygame.mixer.init()
        pygame.mixer.music.load(summon[0])
        pygame.mixer.music.play()
        self.Layout()

    def show_panel_XII(self, event):
        pygame.mixer.music.stop()
        self.panel_XII.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        pygame.mixer.init()
        pygame.mixer.music.load(craft[0])
        pygame.mixer.music.play()
        self.Layout()


    def show_panel_XIII(self, event):
        pygame.mixer.music.stop()
        self.panel_XIII.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        pygame.mixer.init()
        pygame.mixer.music.load(main_menu[1])
        pygame.mixer.music.play()
        self.Layout()

    def show_panel_XIV(self, event):
        self.panel_XIV.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_XV(self, event):
        pygame.mixer.music.stop()
        self.panel_XV.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XVI.Hide()
        self.panel_XVII.Hide()
        pygame.mixer.init()
        shuffle(story)
        pygame.mixer.music.load(story[0])
        pygame.mixer.music.load(story[1])
        pygame.mixer.music.play()
        self.Layout()

    def show_panel_XVI(self, event):
        self.panel_XVI.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVII.Hide()
        self.Layout()

    def show_panel_XVII(self, event):
        self.panel_XVII.Show()
        self.panel_two.Hide()
        self.panel_one.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.panel_seven.Hide()
        self.panel_eight.Hide()
        self.panel_nine.Hide()
        self.panel_X.Hide()
        self.panel_XI.Hide()
        self.panel_XII.Hide()
        self.panel_XIII.Hide()
        self.panel_XIV.Hide()
        self.panel_XV.Hide()
        self.panel_XVI.Hide()
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
        pygame.mixer.music.stop()
        self.Close()
        
if __name__ == "__main__":
    app = wx.App(False)    
    frame = Program()
    frame.Show()
    app.MainLoop()
