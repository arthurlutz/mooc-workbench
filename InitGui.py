# coding: utf-8
################################################
#
#  InitGui.py
#
#  Copyright 2018 Jonathan Wiedemann <contact at freecad-france dot com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
################################################

import os, moocwb_locator
import FreeCAD,  FreeCADGui

moocWBpath = os.path.dirname(moocwb_locator.__file__)
moocWBpath_medias = os.path.join(moocWBpath, 'medias')
moocWB_icons_path = os.path.join( moocWBpath_medias, 'icons')
moocWB_images_path = os.path.join( moocWBpath_medias, 'images')
moocWB_images_path = os.path.join( moocWBpath_medias, 'videos')
moocWB_images_path = os.path.join( moocWBpath_medias, 'gifs')

global main_moocWB_Icon
main_moocWB_Icon = os.path.join( moocWB_icons_path , 'fun-mooc.svg')

class MoocWorkbench ( Workbench ):

    global main_moocWB_Icon

    MenuText = "MOOC"
    ToolTip = "Learn FreeCAD"
    Icon = main_moocWB_Icon

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        import MoocPlayerChooser,  MoocGrader
        self.appendToolbar('MOOC',['Mooc_Player','Mooc_Grader'])
        self.appendMenu('MOOC',['Mooc_Player','Mooc_Grader'])
        #FreeCADGui.addIconPath(":/icons")
        print('Loading MOOC module... done\n')

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(MoocWorkbench())
