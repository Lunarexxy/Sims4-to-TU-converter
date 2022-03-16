# Sims 4 to Tower Unite converter
 This Blender script makes it easier to import Sims 4 models into Tower Unite, by automating the process of merging/renaming Sims 4 vertex groups to fit Tower Unite's armature in Blender. It relies on the .dae models exported by [TS4-SimsRipper](https://github.com/thepancake1/TS4-SimRipper), so please use that!
 
 The settings I use when exporting are *"Single mesh and texture"* and *"Clean DAE mesh"*. You can use the other mesh settings as well, but I found that having multiple meshes often just made things harder in the long run.
 
 *(i have no idea if .obj files would work too, never tried! Have fun being a pioneer if you want~)*
 
 Also keep in mind that Tower Unite currently has a [30,000 vertex limit](https://towerunite.com/sdk/rules) on player models. If your model has more vertices than this, many players might not be able to see it in-game! Very detailed things, like modded clothes and hair, might push you over the limit, but the vanilla and DLC choices are usually okay.

## How to install
* Download the **[Sims4_to_TU_converter.py](https://raw.githubusercontent.com/Lunarexxy/Sims4-to-TU-converter/main/Sims4_to_TU_converter.py)** file *(Right-click and Save As, anywhere on your machine)*
* Open Blender 2.80 or later *(last tested on 3.1.0)*
* Go to Edit -> Preferences -> Add-ons
* Press the Install button and select the downloaded file
* Make sure the little box is checked, to the left of the addon name, to enable it
* Hover your cursor over the 3D viewport, and press N to pop out the sidebar
* If it succeeded, you should now have a "Sims 4" button in the sidebar. Click it to see what to do next.

## How to use the SimRipper tool

![Instructions for how to use the SimRipper tool](https://i.imgur.com/yXaI3mX.png)

## How to do everything else
I'm planning on writing a full guide to the process of pulling Sims 4 models into Tower Unite, covering what I've learned so far, and writing it for people who have zero Blender experience. That way you can do it yourself, if you want. I'll add more info here if I finally get around to that.

*(no promises i'll complete it because ADHD, but people keep being interested)*

## Commissioning
No idea how to use Blender to fix up your Sim for Tower Unite? Or would you prefer to have someone more experienced go over it with you? I've imported several Sims by now, so I've got a decent grasp of the process!

Send me a DM on [my Twitter](https://twitter.com/Lunarexxy), and I'll do my best to get your Sim into Tower Unite!

(It's free, as long as I don't get overwhelmed with requests! I can even give you the final model, so you can retain ownership and put it on the workshop yourself.)

## Contributing
This is my first Blender add-on, so it might be a bit janky, but it seems to work!

Please report bugs and suggest improvements, if you have any 💖
