# `MDSANIMA RenderTime`

The <img width="16" src="icons/logo_mdsanima_default_01-cyan_1x.png" />
Blender add-on estimates and calculate how long your animation will take
to render done based on the rendering time of the only one frame.

You will also find here useful rendering statistics as well as automations of
various time-consuming activities and manny more useful features and tools.

## Blender Add-on

The add-on is located in the `View3D > UI` area panel and show rendering time
statistic. Automatically calculating rendering time for frame range based on
your scene then shows date when rendering is done. The add-on also printing
rendering statistic in `System Console` inside *Blender* terminal.

Developed on [Python 3.10.4][python] and tested on [Blender 3.1.2][bl-3] and
[2.93 LTS][bl-2] version. The add-on also works on *older Blender versions* as
well but this is not recommended.

<div align="center">
  <img
    width="400" alt="mdsanima-render-time-v0.1.1"
    src="https://user-images.githubusercontent.com/3817871/168426652-d4d43bab-b619-40f1-82d4-67b758e968d4.jpg"
  />
</div>

## How to Install

Installing the
<img width="16" src="icons/logo_mdsanima_default_01-cyan_1x.png" />
**add-on** is very simple process, just follow this instruction steps:

- Go to [release][rt-release] page on this repository and download the
  **latest** add-on version.
- Open the [Blender 3.1.2][bl-3] in your system.
- Then open the `Preferences` and select `Add-ons` on the right side.
- Next click the `Install` button and select the add-on path on your hard drive
  where you previously downloaded the latest version.
- Select the `Community` support level button to view the add-on in the list
  below in the next step.
- On the search field type `MDSANIMA RenderTime` and then enable an add-on.

That's it, the add-on `MDSANIMA RenderTime` has been enabled. Now close the
`Preferences` window the add-on will appear in **3D Viewport** on the right
context panel section. If you don't see this section, just use the `N` key
shortcut in *3D Viewport* area to open the right panel where our add-on is
located.

Finally, we can meet together.

## How to Use

Just click on the `RENDER` button to see the statistics. The button renders one
frame of the animation and uses it to calculate how long your whole animation
will take to render done. To refresh statistic, just hover the cursor in to the
button `RENDER`, but don't click on it, then you will see the new date when the
rendering will complete.

You can also use the quick `F12` key shortcut to render a frame and then just
hover the cursor over the render button to see the new statistics.

## Development

Instruction for the *Blender and Python* add-ons or package development can
from with my other repository but instruction for automate release is the some
like here. Please check the [mdsanima-dev][pypi-mdsanima-dev] *Python* package
[documentation][docs-mdsanima-dev] site on GitHub Pages for more information
about it.

Only to do with *Blender and Python* add-ons development you must install the
[fake-bpy-module][fake-bpy] for the code completion in `Visual Studio Code`
just type in the terminal:

```shell
pip install fake-bpy-module-latest
```

## Follow Me

These are my social media account, be sure to check it. Thanks!

[![github-followers-mdsanima][badge-01]][mdsanima-gh]
[![twitter-follow-toudajew][badge-02]][toudajew-tw]
[![twitter-follow-str9led][badge-03]][str9leds-tw]
[![twitter-follow-mdsanima][badge-04]][mdsanima-tw]

[![subreddit-subscribers-mdsanima][badge-05]][mdsanima-re]
[![youtube-subscribers-mdsanima][badge-06]][mdsanima-yt]
[![youtube-views-mdsanima][badge-07]][mdsanima-yt]
[![twitch-status-mdsanima][badge-08]][mdsanima-tv]
[![discord-chat-mdsanima][badge-09]][mdsanima-dc]

## License

The *Blender* add-on [`MDSANIMA RenderTime`][rt-release] developed by
[Marcin Różewski][mdsanima-gh] is released under the terms of
[GPL License][gpl].

[python]: https://python.org/downloads/
[bl-3]: https://blender.org/download/releases/3-1/
[bl-2]: https://blender.org/download/releases/2-93/
[rt-release]: https://github.com/mdsanima-dev/mdsanima-render-time/releases/
[pypi-mdsanima-dev]: https://pypi.org/project/mdsanima-dev/
[docs-mdsanima-dev]: https://mdsanima-dev.github.io/mdsanima-dev/development/
[fake-bpy]: https://github.com/nutti/fake-bpy-module/
[gpl]: https://github.com/mdsanima-dev/mdsanima-render-time/blob/main/LICENSE/

[badge-01]: https://img.shields.io/github/followers/mdsanima?style=social
[badge-02]: https://img.shields.io/twitter/follow/toudajew?style=social
[badge-03]: https://img.shields.io/twitter/follow/str9led?style=social
[badge-04]: https://img.shields.io/twitter/follow/mdsanima?style=social
[badge-05]: https://img.shields.io/reddit/subreddit-subscribers/mdsanima?style=social
[badge-06]: https://img.shields.io/youtube/channel/subscribers/UCB5na2BRwrnwx00LCspbG5Q?style=social
[badge-07]: https://img.shields.io/youtube/channel/views/UCB5na2BRwrnwx00LCspbG5Q?style=social
[badge-08]: https://img.shields.io/twitch/status/mdsanima?style=social
[badge-09]: https://img.shields.io/discord/621477380359454742?style=social&logo=discord

[toudajew-tw]: https://twitter.com/intent/follow?toudajew&screen_name=toudajew
[str9leds-tw]: https://twitter.com/intent/follow?str9led&screen_name=str9led
[mdsanima-tw]: https://twitter.com/intent/follow?mdsanima&screen_name=mdsanima
[mdsanima-yt]: https://youtube.com/mdsanima?sub_confirmation=1
[mdsanima-re]: https://reddit.com/r/mdsanima/
[mdsanima-tv]: https://twitch.tv/mdsanima/
[mdsanima-gh]: https://github.com/mdsanima/
[mdsanima-dc]: https://discord.gg/c3m7pTF/
