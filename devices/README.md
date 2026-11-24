# Device files

**Edit only the `.json` files here.** One per device, made with the device designer
(*Save device file*). The file name is the device's id, e.g. `vkb-gladiator-nxt-evo-l.json`.

- `art/` – the device pictures as separate image files (the device files carry their own copy).
- `built/` – **made automatically, don't edit.** After every push that changes a device file,
  GitHub rebuilds it: a `.js` copy of each device file (a page opened from disk can load `.js`
  but not `.json`) and `index.js`, the list behind the mapper's *Add device*. Pull afterwards
  so your copy has it too.

Each control has a type (button, 4-way hat, encoder, axis…), its icon, headings, leader lines,
and an `outs` entry per output. `n` is the default button number, axis (`x y z rx ry rz s1 s2`)
or POV direction (`hat1_up`). Positions are in sheet units; an Alpha stick is about 4377 units tall.
