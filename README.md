# JoyVerse

A free, unofficial control-map editor for joysticks and control panels in **Star Citizen**.

Lay out your sticks and control panels, name what every button does, check it against your
Star Citizen keybindings, export a profile back to the game, and print a sheet to keep beside your rig.

**Open it online:** https://matmann.github.io/JoyVerse/ – nothing to install, always the latest
version and devices.

**Or use it offline:** download the zip from [Releases](https://github.com/matmann/JoyVerse/releases),
unzip it and open the `.html` file in Brave, Chrome or Edge. Everything is in that one file. When
you're online it also picks up new and updated devices from here.

> Unofficial fan tool. Not affiliated with or endorsed by Cloud Imperium Games, VIRPIL Controls or VKB.
> Star Citizen® is a trademark of Cloud Imperium Rights LLC. Device names, pictures and logos
> belong to their owners.

## Supported devices

- VIRPIL VPC Constellation Alpha (left and right)
- VIRPIL VPC Control Panel #1, #2 and #3
- VKB Gladiator NXT EVO (left and right)
- VKB Gladiator NXT EVO OMNI (left and right)

Each device is a file in the `devices` folder (see [`devices/README.md`](devices/README.md)).
New devices start with the maker's default button numbers.

## Getting started

The first time you open it, a short walkthrough sets up your devices and pages.
Each side panel (Button assignment, Devices, Actions, Game check) has a **?** tour.

- **Your map saves in your browser.** Use **Map file → Save map file** to keep a copy or move it to
  another PC, and **Open map file** to load it back.
- **Game check** compares your map with a keybinding export from Star Citizen
  (*Options → Keybindings → Advanced Controls Customization → Save / Export*) and builds a new
  profile to import. The file you load is never changed.
- **Joystick Gremlin / Gobloon + vJoy** users can load their profile in the walkthrough
  to match devices to joystick numbers.

## Keeping the action list current

The list of Star Citizen actions is kept in [`actions.csv`](actions.csv) and updated after each patch.
In the mapper, **Actions → Check for updates** fetches the latest; your own edits stay on top.

## What's in this repository

| | |
|---|---|
| `index.html` | the mapper – the page GitHub Pages serves |
| `JoyVerse-offline.html` | the same mapper with the devices inside – the one file in the release zip |
| `actions.csv` | every Star Citizen action the mapper knows |
| `devices/*.json` | one file per device |
| `devices/art/` | the device pictures as separate image files |
| `devices/built/` | made automatically from the device files – don't edit |
| `release/` | the release zip's readme and notes; edit `release.json` and push to publish a release |
| `tools/`, `.github/` | the script and GitHub jobs that rebuild `devices/built/` and publish releases |
| `TODO.md` | what's planned |

## Feedback

Found a problem or want a device added? Open an issue.

## Licence

All rights reserved – free for personal use. See [LICENSE.txt](LICENSE.txt).
