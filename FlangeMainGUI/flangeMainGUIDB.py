# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='Raised Face Weld Neck Flange', kernelModule='mainScript', kernelFunction='mainScript', includeApplyBtn=False, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgComboBox(name='ComboBox_1', p='DialogBox', text='Flange Class:', keyword='flangeClass', default='150', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_1', text='150')
RsgListItem(p='ComboBox_1', text='300')
RsgListItem(p='ComboBox_1', text='400')
RsgListItem(p='ComboBox_1', text='600')
RsgListItem(p='ComboBox_1', text='900')
RsgListItem(p='ComboBox_1', text='1500')
RsgListItem(p='ComboBox_1', text='2500')
RsgComboBox(name='ComboBox_2', p='DialogBox', text='NPS:', keyword='flangeSize', default='2', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_2', text='2')
RsgListItem(p='ComboBox_2', text='2.5')
RsgListItem(p='ComboBox_2', text='3')
RsgListItem(p='ComboBox_2', text='3.5')
RsgListItem(p='ComboBox_2', text='4')
RsgListItem(p='ComboBox_2', text='5')
RsgListItem(p='ComboBox_2', text='6')
RsgListItem(p='ComboBox_2', text='8')
RsgListItem(p='ComboBox_2', text='10')
RsgListItem(p='ComboBox_2', text='12')
RsgListItem(p='ComboBox_2', text='14')
RsgListItem(p='ComboBox_2', text='16')
RsgListItem(p='ComboBox_2', text='18')
RsgListItem(p='ComboBox_2', text='20')
RsgListItem(p='ComboBox_2', text='22')
RsgListItem(p='ComboBox_2', text='24')
RsgTextField(p='DialogBox', fieldType='Float', ncols=12, labelText='Pipe Schedule:', keyword='pipeSchedule', default='')
RsgTextField(p='DialogBox', fieldType='Float', ncols=12, labelText='Gasket Thickness:', keyword='gasketThickness', default='')
dialogBox.show()