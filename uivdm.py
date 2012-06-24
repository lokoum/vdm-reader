#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx#YOU MUST DOWNLOAD WXPYTHON @ http://wxpython.org/download.php
import urllib
from lib.vdm import * 


class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		self.last_size = 280
		self.vdm = vdm()
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.output = wx.StaticText(self, -1, "")
		self.NouvelleHistoire = wx.Button(self, -1, "Nouvelle Histoire")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self.nouvelle_histoire, self.NouvelleHistoire)

	def __set_properties(self):
		self.SetTitle("VDM [BETA]")
		self.output.SetMinSize((400, 140))
		self.output.SetFocus()

	def __do_layout(self):
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_1 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_1.Add(self.output, 0, wx.ADJUST_MINSIZE, 0)
		grid_sizer_1.Add(self.NouvelleHistoire, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
		sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()

	def nouvelle_histoire(self, event):
		try:
			story = self.vdm.new_story()
			if story == '':
				self.output.SetLabel(self.vdm.random_story())
				self.last_size -= 2
			else:
				self.output.SetLabel(story)
			self.last_size += 1
			self.SetSize((400, self.last_size))
		except IOError:
			self.output.SetLabel("Erreur de connection")
		event.Skip()

if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
