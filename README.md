# Sims 4 to Tower Unite converter
 This Blender script makes it easier to import Sims 4 models into Tower Unite, by automating the process of merging/renaming Sims 4 vertex groups to fit [Tower Unite's Blender Suite](https://forums.pixeltailgames.com/t/tower-unite-blender-tools-1-2-4/41541) armature. *(Saving you like 15-30 minutes of fiddly manual work)*

 Note that the Tower Unite Blender Suite addon is not compatible with Blender 4.0 or higher.
 
 It relies on the .dae models exported by the [TS4 SimRipper](https://modthesims.info/d/635720/ts4-simripper-classic-rip-sims-from-savegames-v3-13-0-0-7-12-22.html), so please use that! See the image below for which settings to use.

## How to install the script
* Download the latest **[Sims4_to_TU_converter.zip](https://github.com/Lunarexxy/Sims4-to-TU-converter/releases)** file
* Open Blender 2.80 or later *(last tested on 4.0, but will likely work on later versions too)*
* Go to Edit -> Preferences -> Add-ons
* Press the Install button and select the downloaded .zip file
* Make sure the little box is checked, to the left of the addon name, to enable it
* Hover your cursor over the 3D viewport, and press N to pop out the sidebar
* If it succeeded, you should now have a "Sims 4" button in the sidebar.

## How to use the SimRipper tool

*(Requires Sims 4 to be installed on your machine, along with all the DLC and/or mods your Sim uses!)*

Create your Sim, save the game, download [TS4 SimRipper](https://modthesims.info/d/635720/ts4-simripper-classic-rip-sims-from-savegames-v3-13-0-0-7-12-22.html), then follow this guide:

![Instructions for how to use the SimRipper tool](https://i.imgur.com/yXaI3mX.png)

*(While "Single mesh and texture" is recommended, the other two options will also work. They just tend to require some extra effort.)*

*(You can also set Texture Size to HQ if you want, it'll double the texture sizes, but it'll obviously make your model slower to load for others. It also doesn't usually make a big visual difference.)*

## How to make the model compatible with Tower Unite

A comprehensive video guide on how to port models to Tower Unite can be found [here](https://www.youtube.com/watch?v=YUCr28T8K-s). I recommend watching it first, as you'll need to learn these steps anyway. Part of the video covers how to manually rename and merge vertex groups to fit Tower Unite's requirements. This is the step that my script automates.

With the script, you simply select the model's mesh by clicking it, open the Sims 4 menu in the sidebar, and press the "Fix Vertex Groups" button. It will merge the extra vertex groups together and rename them to work with Tower Unite's armature. If the model is made up of multiple meshes, you'll need to do this to each one.

![image](https://user-images.githubusercontent.com/8879206/191913164-3cdb8ffc-d38c-483c-a7a0-6f1e910e98dc.png)

[*KawaiiEvil*](https://kawaiievilvt.carrd.co/) has also written [this text guide](https://docs.google.com/document/d/1QuYlJVm9N7VwhvK0ybf0UNh53gOLKEjAIN32H_VFBzE) showing how to put your Sims 4 model into Tower Unite using this tool! (Thank you!!)

### Common issues

Tower Unite has a [30,000 vertex limit](https://towerunite.com/sdk/rules) on uploading player models. The vanilla and DLC options from Sims 4 usually work fine, but modded content sometimes pushes it over the limit. Tower Unite may also add vertices when importing, for various technical reasons.

Fingers will pretty much always look bad. This is mainly an issue with Tower Unite's animations being broken. In the future, I'd like to add a button for removing all the finger weights and instead weighting them to the hands. This would make the fingers entirely static in all poses, but at least they'd look normal.

## Contributing and usage
This is my first Blender add-on, so it might be a bit janky, but it seems to work!

Please report bugs and suggest improvements, if you have any! 💖

You're also 100% free to copy, modify, and re-use this script for your own purposes, under the GPL 3.0 license.

## Big thanks to

*Lina*, for showing me the SimRipper tool, and being the first to ask if I could find out how import her Sim, which directly led to the creation of this script.

*Josh W*, for making a guide in 2018 on [how to import models into Tower Unite](https://www.youtube.com/watch?v=aYnYWDALONI) (I learned the essential steps from this)

[*Niko*](https://www.youtube.com/c/limesupplier) for creating another [video guide](https://www.youtube.com/watch?v=YUCr28T8K-s) for Blender 2.8+ users, with additional helpful tips.

*CmarNYC* and *thepancake1*, for creating and maintaining the [TS4 SimRipper Classic](https://modthesims.info/d/635720/ts4-simripper-classic-rip-sims-from-savegames-v3-13-0-0-7-12-22.html) and [TS4 SimRipper](https://github.com/thepancake1/TS4-SimRipper) tools, respectively.

*Redoo*, *Skullasaurus*, *Laurie*, and others, for offering many different Sim models to learn from and practice on.

[*KawaiiEvil*](https://kawaiievilvt.carrd.co/), for writing a [text guide](https://docs.google.com/document/d/1QuYlJVm9N7VwhvK0ybf0UNh53gOLKEjAIN32H_VFBzE) on how to take the ripped models, fix them up, and import them into Tower Unite.
