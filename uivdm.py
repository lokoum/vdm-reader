#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from lib.vdm import *


class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		self.choix = 1
		self.last_size = 200
		self.vdm = vdm()
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.output = wx.StaticText(self, -1, "")
		self.xchoix = wx.ListBox(self, -1, choices=["Histoire du jour", "Histoire Aleatoire"])
		self.enter = wx.Button(self, -1, "Nouvelle VDM")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_LISTBOX, self.achoix, self.xchoix)
		self.Bind(wx.EVT_BUTTON, self.nouvelleVDM, self.enter)

	def __set_properties(self):
		self.SetTitle("VDM [BETA]")
		self.xchoix.SetSelection(0)

	def __do_layout(self):
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_1 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_2 = wx.GridSizer(1, 2, 0, 0)
		grid_sizer_1.Add(self.output, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
		grid_sizer_2.Add(self.xchoix, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
		grid_sizer_2.Add(self.enter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
		grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()

	def achoix(self, event):
		if self.choix:
			self.choix -= 1
		else:
			self.choix += 1
		event.Skip()

	def nouvelleVDM(self, event):
		try:
			if self.choix:
				x = self.vdm.new_story()
				if x != '':
					self.output.SetLabel(x)
				else:
					self.vdm = vdm()
			else:
				self.output.SetLabel(self.vdm.random_story())
		except:
			self.output.SetLabel("Erreur")
		self.last_size += 1
		self.SetSize((400, self.last_size))
		event.Skip()



if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
