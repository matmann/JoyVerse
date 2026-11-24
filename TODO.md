# JoyVerse – to do

Updated 23 Nov 2026.

## Where things stand
- The mapper reads its actions only from `actions.csv`: 661 joystick-bindable actions for Star Citizen 4.10.3, all with descriptions.
- A copy of that file is built into the mapper, so it works offline. At start-up it checks GitHub for a newer list (only works once the repo is public).
- The action-list builder (in the private Mapper-tools repository) makes `actions.csv` from `defaultProfile.xml` (converted with unforge), `global.ini` and controls exports.

## Done 22 Nov
- VKB A1 hat: device files can hold two ways to wire one control, named "… (POV)" and "… (axis)". The game file picks which shows (hat1_ → POV, rx/ry → axis); Devices has a switch.
- Reset is one list: Actions / Layout / Devices and pages / Everything.
- Moving things on the map works like the designer: icon/heading moves its group, labels move alone, line dots, snapping, Ctrl+Z. Alt+drag a picture moves just that picture of a device, with its controls.
- Dark sheet (header tick box **Dark**): #444444 with the grey Star Citizen logo, light text and lines, light versions of the maker logos; PNG export uses it.
- Designer: a red **Move picture + its controls** tab on each picture (with Move pictures ticked).
- Designer: Control types… makes your own types and icons; they're saved inside the device files that use them.

## Next
- **Device designer page** – first version done (device designer, in the private Mapper-tools repository). Alpha R and L are seeded from the PSD layout with VIRPIL default numbers. Still to do: the mapper reading device files, and a check that the left Alpha's numbering is right (hat directions, scroll wheel 23/24). Original plan: (for the maintainer, like the action-list builder). Load a device PNG and set its real size so all devices share one scale. Drag control icons on, then size, rotate and snap them. Set each control's type and default numbers:
  - button 1; 2-way toggle 2; 3-position toggle 2 (middle is off)
  - 4-way hat 4 (+1 push); 8-way hat 8 (+1); encoder 2 (+1 push)
  - axis (stick X/Y/twist, throttle, rotary, slider, lever) 1 axis, plus a button if it has a detent
  - headings, groups and leader lines with dots
  - exports a device file (JSON)
- **Device files on GitHub** in a `devices` folder, loaded by the mapper like `actions.csv` (decided: upload a finished device and it's live, no rebuild). Convert the current Alpha, CP1–3, VMAX and CM4 layouts to device files.
- **SVG icon set** redrawn from the PNG icons (emergency toggle, 4-way hat, rotary with push, and the rest). Sharp at any zoom, and colours can change.
- **VKB support.** Device names as VKB shows them in the game export, and VKB default numbering. First device: Gladiator NXT EVO (decided). Needs a straight-on picture and VKB's default button numbers.
- ~~**Name.**~~ Done: JoyVerse (was VPC Mapper).
- **Dark mode.** Two parts: the editor (panels, menus, header) with a toggle or following Windows; and the map sheet, which needs a dark background, light icons/lines/text and maybe darker device art. Colours from Mat: dark background `#444444` with the grey (dark) Star Citizen logo, light background `#f5f5f5` with the white logo, so each logo shows as a subtle tone-on-tone watermark (logo PNGs saved, 3548×4336, transparent). More colour files to come. Logo use must follow CIG's Fankit terms, and the unofficial notice stays.
- **Stay HTML for now.** It could be wrapped later as a small Windows app (Tauri) to read game files directly, detect devices / device order, and auto-update.
- **Only bind across modes where the game does.** The mapper shouldn't copy a button to same-named actions in other modes based on the user's own cross-assignments, only where the game itself puts an action in more than one mode. This drops the four bindings the new list would add: EVA Boost, ground-vehicle Boost, EVA Freelook and on-foot Drop.
- **Sort actions by mode (flight / vehicle / EVA / on foot).** Let the user choose which modes they want on joysticks and panels, and stop actions from the other modes being assigned.
- **Allow in view mode - select ingame modes (scanning, salvage, mining, guns, etc..)**  let view mode hide actions not assigned to that mode for quicker reference
- **Keyboard controls.** Add a new button that toggles a view showing the keyboard bindings next to each action.
- **How-to for shifted (modifier) buttons.** Cover VIRPIL's shift tool, or Joystick Gremlin doing the same job.
- **HidHide / vJoy / Joystick Gremlin walkthrough.** A basic setup guide, probably as a separate page.
- **More devices.** Regroup VMAX and CM4 the way CP3 is done, then MongoosT-50CM3 and others.
- **Help me for Actions builder**  Add a TLDR  help me version of how to unpack and convert with the commnds needed for command prompt for unp4k and unforge.
- **Art work**  Need to reconfigure and unify

## Earlier, still open
- App icon: needs the actual `.ico` or `.png`.
- Confirm guesses: Panel #1 flip switches 17–20 orientation; Alpha Prime triggers 2/3 and 4/5 and brake lever 32; left Alpha scroll wheel 23/24 order.
- Make the repo public and turn on GitHub Pages when ready. **First** scrub the old history: `builder/` (the designer and action builder) and `images/` (VIRPIL artwork, SC logos) are still in past commits – ask before rewriting history.
