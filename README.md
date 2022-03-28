# Sims 4 to Tower Unite converter
 This Blender script makes it easier to import Sims 4 models into Tower Unite, by automating the process of merging/renaming Sims 4 vertex groups to fit [Tower Unite's Blender Suite](https://forums.pixeltailgames.com/t/tower-unite-blender-tools-1-2-4/41541) armature.
 
 It relies on the .dae models exported by [TS4-SimRipper](https://github.com/thepancake1/TS4-SimRipper), so please use that! See the image below for which settings to use.
 
 Keep in mind that Tower Unite currently has a [30,000 vertex limit](https://towerunite.com/sdk/rules) on uploading player models. The vanilla and DLC options from Sims 4 usually work fine, but modded content tends to push it over the limit. Tower Unite may also add vertices when importing, for some reason.

## How to install
* Download the latest **[Sims4_to_TU_converter.zip](https://github.com/Lunarexxy/Sims4-to-TU-converter/releases/tag/latest)** file
* Open Blender 2.80 or later *(last tested on 3.1.0, but will likely work on later versions too)*
* Go to Edit -> Preferences -> Add-ons
* Press the Install button and select the downloaded .zip file
* Make sure the little box is checked, to the left of the addon name, to enable it
* Hover your cursor over the 3D viewport, and press N to pop out the sidebar
* If it succeeded, you should now have a "Sims 4" button in the sidebar. Click it to see what to do next.

## How to use the SimRipper tool

*(Requires Sims 4 to be installed on your machine, along with all the DLC and/or mods your Sim uses!)*

![Instructions for how to use the SimRipper tool](https://i.imgur.com/yXaI3mX.png)

*(While "Single mesh and texture" is recommended, the other two options will also work. They just tend to require some extra effort.)*

## How to do everything else

[KikiTheGeeky](https://kikithegeeky.carrd.co/) has written [this guide](https://docs.google.com/document/d/1QuYlJVm9N7VwhvK0ybf0UNh53gOLKEjAIN32H_VFBzE) showing how to put your Sims 4 model into Tower Unite using this tool! (Thank you!!)

I'm also planning on writing a more comprehensive guide to the process of rigging the Sims 4 models. It'll cover what I've learned so far, and how to fix common issues with the models. *(no promises i'll complete it because ADHD, but people keep being interested!)*

## Commissioning
No idea how to use Blender to fix up your Sim for Tower Unite? Or would you prefer to have someone more experienced go over it with you? I've imported several Sims by now, so I've got a decent grasp of the process!

Send me a DM on [my Twitter](https://twitter.com/Lunarexxy), and I'll do my best to get your Sim into Tower Unite!

(It's free, as long as I don't get overwhelmed with requests! I can even give you the final model, so you can retain ownership and put it on the workshop yourself.)

## Contributing
This is my first Blender add-on, so it might be a bit janky, but it seems to work!

Please report bugs and suggest improvements, if you have any 💖

## Big thanks to

*Lina*, for showing me the SimRipper tool, and being the first to ask if I could find out how import her Sim, which directly led to the creation of this script.

*Josh W*, for making a guide in 2018 on [how to import models into Tower Unite](https://www.youtube.com/watch?v=aYnYWDALONI) (I learned the essential steps from this)

*CmarNYC* and *thepancake1*, for creating and maintaining the [SimRipper](https://github.com/thepancake1/TS4-SimRipper) tool.

*Redoo*, *Skullasaurus*, *Laurie*, and others, for offering many different Sim models to learn from and practice on.

[*Kiki*](https://kikithegeeky.carrd.co/), for writing a [full guide](https://docs.google.com/document/d/1QuYlJVm9N7VwhvK0ybf0UNh53gOLKEjAIN32H_VFBzE) on how to take the ripped models, fix them up, and import them into Tower Unite.
