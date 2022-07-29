#name=PreSonus Atom

#Script Version 1.0 by YukoFurry
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

#-----Start of Loop-----

def OnControlChange(event):

#---Navigatin---
#---Up---
	if event.data1 == up_key and event.data2 == 127:
		if ui.getFocused(2) == 1:
			patterns.deselectAll()
			patterns.selectPattern(patterns.patternNumber() - 1)
		else:
			ui.up()
		event.handled = True

#---Down---
	if event.data1 == down_key and event.data2 == 127:
		if ui.getFocused(2) == 1:
			patterns.deselectAll()
			patterns.selectPattern(patterns.patternNumber() + 1)
		else:
			ui.down()
		event.handled = True

#---Left---
	if event.data1 == left_key and event.data2 == 127:
		ui.left()
		event.handled = True

#---Right---
	if event.data1 == right_key and event.data2 == 127:
		ui.right()
		event.handled = True

#---Select---
	if event.data1 == select_key and event.data2 == 127:
		ui.nextWindow()
		event.handled = True
	if event.data1 == select_key and event.data2 == 0:
		ui.setHintMsg(ui.getFocusedFormCaption())
		event.handled = True

#---Zoom---
	if event.data1 == zoom_key and event.data2 == 127:
		ui.horZoom(zoom_value)
		ui.verZoom(zoom_value)
		event.handled = True
	if event.data1 == zoom_key and event.data2 == 0:
		ui.horZoom(-zoom_value)
		ui.verZoom(-zoom_value)
		event.handled = True

#---Transport---
#---Click---
	if event.data1 == click_key and event.data2 == 127 and ui.isMetronomeEnabled() == False:
		transport.globalTransport(midi.FPT_Metronome, 1)
		event.handled = True
	if event.data1 == click_key and event.data2 == 0 and ui.isMetronomeEnabled() == True:
		transport.globalTransport(midi.FPT_Metronome, 1)
		event.handled = True

#---Count In---
	if event.data1 == count_in_key and event.data2 == 127:
		transport.globalTransport(midi.FPT_CountDown, 1)
		event.handled = True

#---Record---
	if event.data1 == record_key and event.data2 == 127 and transport.isRecording() == False:
		transport.record()
		event.handled = True
	if event.data1 == record_key and event.data2 == 0 and transport.isRecording() == True:
		transport.record()
		event.handled = True

#---Save---
	if event.data1 == save_key and event.data2 == 127:
		transport.globalTransport(midi.FPT_Save, 1)
		event.handled = True

#---Play---
	if event.data1 == play_key and event.data2 == 127 and transport.isPlaying() == False:
		transport.start()
		event.handled = True
	if event.data1 == play_key and event.data2 == 0 and transport.isPlaying() == True:
		transport.start()
		event.handled = True

#---Loop---
	if event.data1 == loop_key and event.data2 == 127 and ui.isLoopRecEnabled() == False:
		transport.globalTransport(midi.FPT_LoopRecord, 1)
		event.handled = True
	if event.data1 == loop_key and event.data2 == 0 and ui.isLoopRecEnabled() == True:
		transport.globalTransport(midi.FPT_LoopRecord, 1)
		event.handled = True

#---Stop---	
	if event.data1 == stop_key:
		transport.stop()
		event.handled = True

#---Undo---
	if event.data1 == undo_key and event.data2 == 127:
		general.undo()
		event.handled = True

#---Event---
#---Editor---
	if event.data1 == editor_key and event.data2 == 127:
		openEventEditor(1)
		event.handled = True
	if event.data1 == editor_key and event.data2 == 0:
		openEventEditor(0)
		event.handled = True

		

#---Nudge---
	if event.data1 == nudge_key and event.data2 == 127:
		ui.snapOnOff()
		ui.snapMode(1)
		event.handled = True
	if event.data1 == nudge_key and event.data2 == 0:
		ui.snapOnOff()
		event.handled = True

#---Quantize---
	if event.data1 == quantize_key:
		event.handled = True


#---Song---
#---Setup---
	if event.data1 == setup_key and event.data2 == 127 and mixer.getTrackVolume(20) > 0:
		mixer.setTrackVolume(20, 0)
		mixer.setTrackVolume(21, 0)
		mixer.setTrackVolume(22, 0)
		mixer.setTrackVolume(23, 0)
		mixer.setTrackVolume(24, 0)
		mixer.setTrackVolume(25, 0)
		mixer.setTrackVolume(26, 0)
		mixer.setTrackVolume(27, 0)
		mixer.setTrackVolume(28, 0)
		mixer.setTrackVolume(29, 0)
		mixer.setTrackVolume(30, 0)
		event.handled = True

	if event.data1 == setup_key and event.data2 == 0 and mixer.getTrackVolume(20) == 0:
		mixer.setTrackVolume(20, 0.8)
		mixer.setTrackVolume(21, 0.8)
		mixer.setTrackVolume(22, 0.8)
		mixer.setTrackVolume(23, 0.8)
		mixer.setTrackVolume(24, 0.8)
		mixer.setTrackVolume(25, 0.8)
		mixer.setTrackVolume(26, 0.8)
		mixer.setTrackVolume(27, 0.8)
		mixer.setTrackVolume(28, 0.8)
		mixer.setTrackVolume(29, 0.8)
		mixer.setTrackVolume(30, 0.8)
		event.handled = True

#---Set Loop---
	if event.data1 == set_loop_key and event.data2 == 127 and transport.getLoopMode() == 0:
		transport.setLoopMode()
		event.handled = True
	if event.data1 == set_loop_key and event.data2 == 0 and transport.getLoopMode() == 1:
		transport.setLoopMode()
		event.handled = True

#---Inst---
#---Show/Hide---

	if event.data1 == show_hide_key and event.data2 == 127:
		if ui.getVisible(3) == 0:
			ui.showWindow(3)
		else:
			ui.hideWindow(3)
		event.handled = True

#---Focus---
	if event.data1 == focus_key and event.data2 == 127:
		channels.showEditor(1)
		channels.focusEditor(1)
		event.handled = True
	if event.data1 == focus_key and event.data2 == 0:
		channels.showEditor(0)
		event.handled = True