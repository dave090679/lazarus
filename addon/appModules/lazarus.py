#appModules/lazarus.py
# Ein Teil von NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2023 NVDA Mitwirkende
# Diese Datei unterliegt der GNU General Public License.
# Weitere Informationen finden Sie in der Datei COPYING.
import textInfos
from NVDAObjects.IAccessible import IAccessible
import appModuleHandler
import controlTypes
import api
from scriptHandler import script
#import addonHandler
# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.
#addonHandler.initTranslation()
class lazarus_grid(IAccessible):
	def _get_name(self):
		info = self.parent.makeTextInfo(textInfos.POSITION_SELECTION)
		s = ""
		for t in info.getTextInChunks(textInfos.UNIT_LINE):
			s += t
		return s
class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.IAccessibleObject.accName[0] in ["PropertyGrid","EventGruid"]:
			clsList.insert(0, lazarus_grid)
