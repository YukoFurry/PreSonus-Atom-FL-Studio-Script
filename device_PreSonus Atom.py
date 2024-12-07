#name=PreSonus Atom
#supportedDevices=PreSonus ATOM

# Changes: Added supportedDeviceList, switched mute channels 20-30 from Setup to Preset +/-, nudge now switches snap mode selection, switched showing piano roll from Show/Hide to Editor,

#Script Version 1.2 by YukoFurry
#Fl-Studio Version 20.8.4 Build 2576

#-----Imports-----
import playlist
import channels
import mixer
import patterns
import arrangement
import ui
import transport
import device
import plugins
import general
import launchMapPages 
import midi

#-----Define variables-----

#---Generic Variables---
zoom_value = 10
muteTrackStart = 20
muteTrackEnd = 30

#---Navigation keys---
up_key = 87
down_key = 89
left_key = 90
right_key = 102
select_key = 103
zoom_key = 104

#---Transportation keys---
click_key = 105
count_in_key = 106
record_key = 107
save_key = 108
play_key = 109
loop_key = 110
stop_key = 111
undo_key = 112

#---Song keys---
setup_key = 86
set_loop_key = 85

#---Event keys---
editor_key = 31
nudge_key = 30
quantize_key = 23

#---Inst keys---
show_hide_key = 29
focus_key = 28
preset_key = 27
bank_key = 26

#---Mode keys---
full_level_key = 25
note_repeat_key = 24

#---Rotary Encorders---
encoder_one = 14
encoder_two = 15
encoder_three = 16
encoder_four = 17



#-----Start of Script-----

def OnControlChange(event):

#---Navigation---
#---Up---
	if event.data1 == up_key:
		if event.data2 == 127:
			if ui.getFocusedPluginName():
				counter = 0
				truthCheck = False
				while truthCheck == False:
					if plugins.isValid(counter) == False:
						counter+=1
					elif ui.getFocusedPluginName() not in plugins.getPluginName(counter):
						counter+=1
					else:
						truthCheck = True
				plugins.prevPreset(counter)
			elif ui.getFocused(2) == 1:
				patterns.deselectAll()
				patterns.selectPattern(patterns.patternNumber() - 1)
			else:
				ui.up()
		event.handled = True

#---Down---
	if event.data1 == down_key:
		if event.data2 == 127:
			if ui.getFocusedPluginName():
				counter = 0
				truthCheck = False
				while truthCheck == False:
					if plugins.isValid(counter) == False:
						counter+=1
					elif ui.getFocusedPluginName() not in plugins.getPluginName(counter):
						counter+=1
					else:
						truthCheck = True
				plugins.nextPreset(counter)
			elif ui.getFocused(2) == 1:
				patterns.deselectAll()
				patterns.selectPattern(patterns.patternNumber() + 1)
			else:
				ui.down()
		event.handled = True

#---Left---
	if event.data1 == left_key:
		if event.data2 == 127:
			ui.left()
		event.handled = True

#---Right---
	if event.data1 == right_key:
		if event.data2 == 127:
			ui.right()
		event.handled = True

#---Select---
	if event.data1 == select_key:
		if event.data2 == 127:
			ui.nextWindow()
		elif event.data2 == 0:
			ui.setHintMsg(ui.getFocusedFormCaption())
		event.handled = True

#---Zoom---
	if event.data1 == zoom_key:
		if event.data2 == 127:
			ui.horZoom(zoom_value)
			ui.verZoom(zoom_value)
		elif event.data2 == 0:
			ui.horZoom(-zoom_value)
			ui.verZoom(-zoom_value)
		event.handled = True

#---Transport---
#---Click---
	if event.data1 == click_key:
		if event.data2 == 127 and ui.isMetronomeEnabled() == False:
			transport.globalTransport(midi.FPT_Metronome, 1)
		elif event.data2 == 0 and ui.isMetronomeEnabled() == True:
			transport.globalTransport(midi.FPT_Metronome, 1)
		event.handled = True

#---Count In---
	if event.data1 == count_in_key:
		if event.data2 == 127:
			transport.globalTransport(midi.FPT_CountDown, 1)
		event.handled = True

#---Record---
	if event.data1 == record_key:
		if event.data2 == 127 and transport.isRecording() == False:
			transport.record()
		elif event.data2 == 0 and transport.isRecording() == True:
			transport.record()
		event.handled = True

#---Save---
	if event.data1 == save_key:
		transport.globalTransport(midi.FPT_Save, 1)
		event.handled = True

#---Play---
	if event.data1 == play_key:
		if event.data2 == 127 and transport.isPlaying() == False:
			transport.start()
		elif event.data2 == 0 and transport.isPlaying() == True:
			transport.start()
		event.handled = True

#---Loop---
	if event.data1 == loop_key:
		if event.data2 == 127 and ui.isLoopRecEnabled() == False:
			transport.globalTransport(midi.FPT_LoopRecord, 1)
		elif event.data2 == 0 and ui.isLoopRecEnabled() == True:
			transport.globalTransport(midi.FPT_LoopRecord, 1)
		event.handled = True

#---Stop---	
	if event.data1 == stop_key:
		transport.stop()
		event.handled = True

#---Undo---
	if event.data1 == undo_key:
		if event.data2 == 127:
			general.undo()
		event.handled = True

#---Event---
#---Editor---
	if event.data1 == editor_key:
		if event.data2 == 127:
			if ui.getFocused(1) == 1:
				channels.showEditor(channels.selectedChannel())
			elif ui.getFocused(0) == 1:
				event.handled = True
			elif ui.getVisible(3) == 0:
				ui.showWindow(3)
		elif event.data2 == 0:
			if ui.getFocused(5) == 1:
				channels.showEditor(channels.selectedChannel(), 0)
			elif ui.getVisible(3) == 1:
				ui.hideWindow(3)
		event.handled = True

#---Nudge---
	if event.data1 == nudge_key:
		if event.data2 == 127:
			ui.snapMode(1)
		elif event.data2 == 0:
			ui.snapMode(1)
		event.handled = True

#---Quantize---

#---Song---
#---Setup---
	if event.data1 == setup_key:
		if event.data2 == 127:
			ui.setFocused(4)
			ui.showWindow(4)
			ui.showWindow(0)
			ui.showWindow(1)
			ui.showWindow(2)
		event.handled = True


#---Set Loop---
	if event.data1 == set_loop_key:
		if event.data2 == 127 and transport.getLoopMode() == 0:
			transport.setLoopMode()
		elif event.data2 == 0 and transport.getLoopMode() == 1:
			transport.setLoopMode()
		event.handled = True

#---Inst---
#---Show/Hide---

	if event.data1 == show_hide_key:
		if event.data2 == 127:
			if ui.isInPopupMenu() == True:
				ui.closeActivePopupMenu
			elif ui.getFocused(4) == 1:
				ui.hideWindow(4)
			ui.escape()
		event.handled = True

#---Preset +/-

	if event.data1 == preset_key:
		if event.data2 == 127:
			counter = muteTrackStart
			for counter in range(muteTrackStart, muteTrackEnd + 1):
				mixer.setTrackVolume(counter, 0)
		elif event.data2 == 0:
			counter = muteTrackStart
			for counter in range(muteTrackStart, muteTrackEnd + 1):
				mixer.setTrackVolume(counter, 0.8)
		event.handled = True

#---Focus---
	if event.data1 == focus_key:
		ui.setFocused(4)
		event.handled = True

#---Mode---
#---Full Level---
	if event.data1 == full_level_key:
		if ui.getFocused(4) == True:
			ui.enter()
		event.handled = True

#---Note Repeat---

#---Rotary Encoders---