PreSonus-Atom-FL-Studio-Script
```
FL Studio midi script for the PreSonus Atom Pad controller
Made by YukoFurry
Script Version 1.0 by YukoFurry
Fl-Studio Version 20.8.4 Build 2576 (Should be compatible from 20.7 to newest)


Note: This script is personalized for my use, however many button functions are predefined anyway 
(like play/record) so I of course coded them for their destined purpose. 
I am by far no professional coder and even less a python geek, so please don't expect any godlike 
code. I bought the PreSonus Atom with the expectancy it would work natively with FL-Studio which 
it didn't. To make it work I was thrown into python scripting so here we are.
If you know FL-Studio midi scripting and want to help or generally have suggestions for button use 
feel free to contact me.

For information on where to put the file please see Image-Lines guide on midi scripts under 
"Script Locations and File Names":
https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm

-----Functions-----

--Navigation Keys--
Up: Move up (Arrow up key)
Down: Move down (Arrow down key)
Left: Move left (Arrow left key)
Right: Move right (Arrow right key)
Select: TAB (Switches between opened windows)
Zoom: Zooms in/out by a defined amount (Change variable value of "zoom_value" to change the amount)

--Transport Keys--
Click: Toggles the Metronome
Count In: Toggles Countdown before recording
Record: Toggles recording
Save: CTRL + S (Saves the file)
Play: Toggles Play/Pause
Loop: Toggles loop recording
Stop: Stops playback
Undo: CTRL + Z (Undo button)

--Song Keys--
Setup: Toggles mute on Channels 20-30
Set Loop: Toggles playback mode between pattern mode and song mode

--Event Keys--
Editor: none
Nudge: Toggles between "none" and next snap mode in the snap pannel
Quantize: none (Planned quick Quantize CTRL + Q, however code didn't work)

--Inst--
Show/Hide: Toggles showing/hiding piano roll window for selected pattern in the channel rack
Preset+/-: none
Focus: none
Bank: no function/midi output possible

--Mode--
Full Level: none
Note Repeat: none
Shift: no function/midi output possible
```
