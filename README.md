# Sims 4 to Tower Unite converter
This Blender script makes it easier to import Sims 4 models into Tower Unite, by automating the process of merging/renaming Sims 4 vertex groups to fit the Tower Unite armature. It saves you like 15-30 minutes of fiddly manual work.
 
It relies on the .dae models exported by the [TS4 SimRipper](https://github.com/CmarNYC-Tools/TS4SimRipper), so please use that! See the image below for which settings to use.

*(The TS4 SimRipper thread was originally [here](https://modthesims.info/d/635720/ts4-simripper-classic-rip-sims-from-savegames-v3-13-0-0-7-12-22.html), but its creator, CmarNYC, sadly passed away in October 2023, so updates are now made by community members.)*

For more info on creating custom characters for Tower Unite, visit [the official Tower Unite Workshop SDK](https://www.towerunite.com/guides/wk_creatingcharacters_v3.html).

## What does the script do?

It renames the Sims 4 vertex groups to Tower Unite vertex groups. Some of the vertex groups are merged, as Tower Unite doesn't have as many bones as Sims 4.

![image](https://github.com/Lunarexxy/Sims4-to-TU-converter/assets/8879206/7100fb6f-cace-401f-87e0-e80f82a9c02d)

## How to install the script
* Download the latest **[Sims4_to_TU_converter.zip](https://github.com/Lunarexxy/Sims4-to-TU-converter/releases)** file
* Open Blender 4.0 or later *(Anything 2.8x and later likely works too, but is unsupported.)*
* Go to Edit -> Preferences -> Add-ons
* Press the drop-down arrow in the top-right corner.
* Press the Install From Disk button and select the downloaded .zip file
* Make sure the add-on is enabled. If not, click the checkbox next to its name.
* Hover your cursor over the 3D viewport, and press N to pop out the sidebar
* If it succeeded, you should now have a "S4TU" button in the sidebar.
* Press that button to see the Sims 4 to Tower Unite tools, and follow their instructions.

## How to use the SimRipper tool

*(Requires Sims 4 to be installed on your machine, along with all the DLC and/or mods your Sim uses!)*

Create your Sim, save the game, download the latest version of [TS4 SimRipper](https://sims4studio.com/thread/34354/ts4-sim-ripper), then follow this guide:

![Instructions for how to use the SimRipper tool](https://i.imgur.com/yXaI3mX.png)

*("Single mesh and texture" is recommended. The other two options will also work, but may need some extra effort.)*

*(Setting Texture Size to HQ will double the texture resolution, but it'll make your model slower to load for others. It usually doesn't make a big visual difference.)*

## Before using the script - pose your model

Once you've used the Fix Vertex Groups button, your model will be much harder to pose to line up with the Tower Unite armature, as you're not supposed to pose the TU armature itself. Make sure you've already lined everything up first.

I've offered a basic guide to this below, but it won't go into full detail and may not be the perfect way to do it. You're expected to already know how to use Blender on your own.

You can skip it if you already know what you're doing, and just need the vertex groups renamed.

### Prerequisites:

You will need a copy of the official Workshop Rig .blend file, [found here.](https://www.towerunite.com/guides/wk_creatingcharacters_v3.html)

You can watch [this video guide on how to port models to Tower Unite, by Niko,](https://www.youtube.com/watch?v=YUCr28T8K-s) for a quick, visual explanation of the process. Some of it is outdated *(we no longer use the Tower Unite Blender Suite addon)* but most of it is still accurate.

You should also know,
 * "Mesh" refers to the 3D geometry part of your model. A model can have more than one of these.
 * "Armature" and "Rig" both mean the same thing, but I use "rig" below when talking about the rig that your Sims 4 model comes with, as it's usually named "rig", and "armature" when talking about Tower Unite's Workshop Rig, as it has to be named "Armature" to work when loaded into the game. I know, it's a little confusing.
 * "Model" means the model as a whole. Mesh(es), armature, and everything else your character uses, combined.

### How to pose the model:

First: 
 * Load the official Workshop Rig .blend scene in Blender
 * Delete the Davier mesh
 * Delete the Nametag mesh

Then, for the Sims 4 rig:
 * Import your Sims 4 model *(It might import very small!)*
 * Select the Sims 4 rig. *(Usually just named "rig")*
 * Scale it to roughly the same height as the Workshop Armature
 * Enter Pose Mode
 * Rotate the arms into a T-pose *(Usually 45 degrees on the Y-axis)*
 * Make any other changes that make sense for your model
 * Enter Object Mode
 * Hit Ctrl-A and apply the scale.

On each mesh in the model: *(usually you'll only have one)*
 * Select the mesh, and apply the scale on it as well.
 * Go into the mesh's modifier tab
 * Apply the Armature modifier. This locks in the T-pose.
 * Create a new Armature modifier, and link it to the official Armature.

Finally, delete the Sims 4 rig.

If all went well, your model should now be in the same pose as the official armature, and connected to it. The vertex group names on each mesh will still be wrong, which means it can't be animated yet, so follow the steps in the next section.

*(Also, it might not have any texture applied. You can go into the Material tab of each mesh to add an image texture pointing to the texture files, if so.)*

## How to use the script

 * Import your Sims 4 model into the Blender scene, if you haven't already.
 * Open the S4TU menu in the 3D viewport's sidebar.
 * Select the mesh *(not the rig/armature!)*
 * Press the Fix Vertex Groups button
 * If the model has multiple meshes, do this to each one.
 * Your model should now have vertex groups that work with Tower Unite.

![image](https://user-images.githubusercontent.com/8879206/191913164-3cdb8ffc-d38c-483c-a7a0-6f1e910e98dc.png)

If you want, you can also use the "Merge Fingers Into Hands" tool now. This will stop your model from having its fingers posed in-game. Tower Unite's finger animations are quite poor, so sometimes this looks better. It's not required, though.

After all this, you should be free to export the model to .dae, open Tower Unite, and import it in the in-game Workshop Editor.

## Common issues

If the SimRipper keeps crashing, it's often because Sims 4 had an update recently. Make sure to use the latest version of both the SimRipper and Sims 4.

Tower Unite has a [30,000 vertex limit](https://www.towerunite.com/guides/wk_rules.html#model-limits) on uploading player models. The vanilla and DLC options from Sims 4 usually work fine, but modded content sometimes pushes it over the limit. Tower Unite may also add vertices when importing, for various unknown reasons. If your Sim has too many vertices, it can't be imported into Tower Unite.

Fingers will pretty much always look bad. This is mainly an issue with Tower Unite's animations being poorly animated. There is a button for merging fingers into the hand, which will stop them from being animated at all. They'll simply follow the hand as-is.

Clothing, hair, jewelry and other details will also often look odd and wrinkly. The exact cause isn't known, but fixing it manually is pretty difficult.

## Contributing and usage
This is my first Blender add-on, so it might be a bit janky, but it seems to work!

Please report bugs and suggest improvements, if you have any! 💖

You're also 100% free to copy, modify, and re-use this script for your own purposes, under the GPL 3.0 license.

## Big thanks to

*Lina*, for showing me the SimRipper tool, and being the first to ask if I could find out how import her Sim, which directly led to the creation of this script.

*Josh W*, for making a guide in 2018 on [how to import models into Tower Unite](https://www.youtube.com/watch?v=aYnYWDALONI) *(I learned the essential steps from this)*

[*Niko*](https://www.youtube.com/c/limesupplier) for creating another [video guide](https://www.youtube.com/watch?v=YUCr28T8K-s) for Blender 2.8+ users, with additional helpful tips.

*CmarNYC*, *thepancake1*, and *andrew on Sims 4 Studio* for creating and maintaining the TS4 SimRipper tool.

*Redoo*, *Skullasaurus*, *Laurie*, and many others, for offering many different Sims 4 models to learn from and practice on.

*KawaiiEvil*, for writing a [text guide](https://docs.google.com/document/d/1QuYlJVm9N7VwhvK0ybf0UNh53gOLKEjAIN32H_VFBzE) on how to take the ripped models, fix them up, and import them into Tower Unite.
