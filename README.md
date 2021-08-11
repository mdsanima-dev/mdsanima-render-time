# mdsanima-render-time

Blender Add-on for estimated total rendering time for all frames in your animation.

## Blender Add-on `MDSANIMA RenderTime`

Automatically calculating rendering time for all frames based on your scenes,
and shows date when rendering is done. Add-on also printing rendering stats
in `System Console` in **Blender**.

Tested with [Blender 2.93.2](https://www.blender.org/download/releases/2-93/)
but probably works on **older versions** as well and with **Blender 3.0.0 Alpha** too.

<img width="256" alt="mdsanima-render-time-blender-addon_button" src="https://user-images.githubusercontent.com/3817871/128876799-13caec70-b7f0-49c5-9d7e-333838b5601f.png">

## How to Install

Installing the **Add-on** is very simple.

* Go to [Releases](httops://github.com/mdsanima-dev/mdsanima-render-time/releases/)
page on this repository and download **Latest Release** version.

* Open **Blender 2.93.2** in your system.

* Go to `Preferences` and select `Add-ons` on the right side.

* Then click the **Install** button and select the path where you downloaded the `Add-on`.

* You must select **Community** support level to view the `Add-on`.

* Then in the search type `MDSANIMA RenderTime` and enable the `Add-on`.

That's it, close the `Preferences` window. The add-on will appear in **3D View** > **UI**.

## How to Use

Just click on the **Render** button to see the statistics. The button renders one
frame of the animation and uses it to calculate when the renderign is complete.
To refresh, just go to the button **Render**, but don't click on it, then you
will see the new date when the rendering is done.

You can also use the quick `F12` key to render a frame and then just hover over
the render button to see the statistics.

## Development

Add a `standard-version` npm pacage to automatically create `CHANGELOG.md`
and tracking version. This option allow to generate automatically changelog
file for the project and tracking version on the `Add-on` based on commit
messages.

For some reason thats features is only for the development not allow and accecs
for the **Blender Add-on** `MDSANIMA RenderTime`.

Make release run in the console:

```bash
standard-version release
```

For checking if everything is ok:

```bash
standard-version release-test
```

## Connect With Me

Hi there, I'm Marcin Różewski aka [MDSANIMA](https://mdsanima.com).
These are my social media, check it out please. Thanks.

![GitHub followers](https://img.shields.io/github/followers/mdsanima?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/toudajew?style=flat-square)
![Twitter Follow](https://img.shields.io/twitter/follow/str9led?style=flat-square)
![Twitter Follow](https://img.shields.io/twitter/follow/mdsanima?style=flat-square)
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCB5na2BRwrnwx00LCspbG5Q?style=social)
![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCB5na2BRwrnwx00LCspbG5Q?style=social)

License
-------
Blender Add-on `MDSANIMA RenderTime` is released under the terms of [GPL License](https://github.com/mdsanima-dev/mdsanima-render-time/blob/master/LICENSE)
