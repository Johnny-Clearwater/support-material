---
title: "Two nozzles, two cadences"
issue: 1
date: 2026-11-21
summary: "An OrcaSlicer fork that gives each nozzle its own layer height, five quick finds from a screen-reader slicer to a litter-picking rover, and Klipper for the Core One."
draft: true
---

Support Material is a biweekly roundup of open-source 3D printing projects built by individuals who never advertised them. Every project here was created, released or updated in the two weeks before this issue, and none of them turned up in our coverage check of the big 3D printing outlets.

## Deep cut: two nozzles, two layer heights, one print

**[Cadence Slicer](https://github.com/HMITCHR/CadenceSlicer)** by [HMITCHR](https://github.com/HMITCHR) is an OrcaSlicer fork for multi-nozzle printers. It doesn't just run two nozzle sizes in one print. It runs each one at its *own* layer height. Version 1.2.0 shipped on November 10, rebased onto OrcaSlicer 2.5.0.

**Why that matters.** Stock OrcaSlicer 2.5.0 now lets the two nozzles on an H2D or X2D be different sizes. But both still march up the part at the same layer height, so a 0.8 mm nozzle is stuck printing thin layers. Cadence lets the coarse nozzle lay down thick layers while the fine nozzle keeps the surfaces crisp.

**The trick.** The coarse nozzle prints at a whole-number multiple, N, of the fine layer height. The two layer stacks line up every N fine layers, and that's the only place the nozzles swap, with a purge and re-prime on the prime tower. A time check keeps a part on the fine nozzle when a swap would cost more than it saves. On standard Bambu hotends N can go up to 14.

**Two ways to split a print**

- **Feature Split:** walls and top/bottom skins on the fine nozzle, sparse infill on the coarse one.
- **Body Split:** whole parts, or regions you paint, go to one nozzle or the other. Interlocking beams join them.

**The maker's numbers** (slicer estimates)

| Model | Cadence | Single nozzle |
| --- | --- | --- |
| Argonath (0.2 + 0.8 mm, N = 7) | 13 h 1 min | 1 d 4 h 12 min at 0.08 mm |
| Minas Tirith (N = 5) | 11 h 57 min | 18 h 38 min |
| Text sign, Body Split | ~47 min | 1 h 40 min |

**What it won't do.** The README is upfront about the limits. There's no speedup on single-nozzle printers, and small prints can end up slower. It refuses PLA paired with PETG, adaptive layer height, spiral vase and Arachne walls. Body Split can't do rafts. Builds exist for macOS (Apple silicon) and Windows only, with no Linux build. Bambu cloud printing is out, so use LAN mode or the SD card. The installers are unsigned.

**At a glance**

| Item | Detail |
| --- | --- |
| Base | OrcaSlicer 2.5.0 fork |
| Hardware | Print-tested on the Bambu H2D only. H2D Pro, H2C, X2D, Prusa XL and Snapmaker J1/U1 are enabled but untested; v1.2 adds Snapmaker U1 profiles |
| Nozzles | Any pair of 0.2 / 0.4 / 0.6 / 0.8 mm, Standard or High Flow |
| Status | v1.2.0, released Nov 10, 2026; seven releases since v1.0 on Oct 2 |
| Cost | Free |
| License | AGPL-3.0, inherited from OrcaSlicer |

**Editor's note.** If you own a Prusa XL, you're the person the maker needs most: it's enabled but nobody has printed on one yet. Test reports go in the repo's issues.

## Quick finds

Five small projects from individual makers, all active in the last two weeks.

- **[AccessSlice](https://github.com/Accessible3D-Edis/AccessSlice)** by [Edis Adilovic](https://github.com/Accessible3D-Edis). A Windows app that lets blind and low-vision makers prepare, slice, send and monitor prints with a screen reader. It doesn't replace your slicer. A 3MF project is a zip of plain text, so AccessSlice turns every setting into a labelled field, slices with the real engine (Bambu Studio, PrusaSlicer, OrcaSlicer, Creality Print 7 or Anycubic Slicer Next), and reads the result back as text, including a layer-by-layer description. It checks moves before sending and won't start until you confirm the plate is empty. 728 automated tests; three releases between Nov 9 and Nov 14. GPL-3.0.
- **[ender3-hotend-twin](https://github.com/batu63562/ender3-hotend-twin)** by [batu63562](https://github.com/batu63562). A physics model of an Ender 3 hotend running Klipper that spots faults from heater power alone, with no extra sensors. The idea: while the PID holds temperature steady, the heater works like a calorimeter, so any "missing power" means something changed. It catches a filament run-out in about 20 seconds, and on the maker's own test logs it caught 24 of 31 labelled faults with about one false alarm every seven print hours. The maker is clear it's validated on one printer, with PETG and TPU only, and it is *not* a replacement for thermal-runaway protection. Commits through Nov 12; docs mostly in Turkish. GPL-3.0.
- **[MOSS](https://github.com/metrox-eth/moss)** by [metr0x](https://github.com/metrox-eth). A mostly 3D-printed litter-picking rover with printed TPU tracks, an ESP32-S3 base, an arm derived from the SO-101 with a gripper widened to 90 mm, and a depth camera in the nose. The base costs about $460, and full builds run about $600 to $1,390 depending on the compute you pick. It's honest about where it stands: it drives and does pick-and-drop moves, but fully autonomous litter picking hasn't been shown yet. Daily commits through Nov 15. Code is Apache-2.0; MOSS's own hardware designs are CC BY-NC-SA 4.0 from Nov 1, 2026 (earlier copies were CERN-OHL-S-2.0), so no commercial builds.
  *Safety note:* MOSS uses a custom 3S4P lithium pack, and the maker posted an "Important Safety Update" on Nov 9. Read the battery guide in the repo before building, and follow the maker's advice to put the rover on blocks for its first run.
- **[SpinSlicer](https://github.com/redbluecarrot/SpinSlicer)** by [redbluecarrot](https://github.com/redbluecarrot). A desktop slicer for Computed Axial Lithography, the "print a whole object at once inside a spinning vial of resin" method. It computes the projector frames, simulates the cured result to show regions that over- or under-cure, and plays the exposure. The engine is pure NumPy and SciPy with no GPU, and it models refraction, attenuation and Fresnel losses; a 128-voxel grid takes about 10 seconds on two cores. v0.8.0 (Nov 8) added one-button printing to a networked printer. MIT.
  *Safety note:* CAL means photopolymer resin and intense projector light, and the README doesn't cover handling either. Use the resin maker's safety data sheet, gloves, ventilation and eye protection.
- **[gridfinity-solidcraft](https://github.com/tharje/gridfinity-solidcraft)** by [Tharje Kinn](https://github.com/tharje). A plugin for the open-source SolidCraft CAD app that generates Gridfinity bins and baseplates. Drawer baseplates are split to your bed size and lock together with press-fit dovetails. Settings like height and label text stay editable afterward without rerunning the plugin, and label text comes out as a separate body so you can print it in another colour. The whole thing was created between Nov 13 and Nov 15. The maker says it's "not yet printed: please report how it fits." MIT.

## Tooling corner

Three firmware and software tools, all with releases in the window. The first one is for Prusa owners.

- **[coreone-firmware](https://github.com/packerlschupfer/coreone-firmware)** by [packerlschupfer](https://github.com/packerlschupfer). A Klipper port for the Prusa Core One and Core One+ that runs on the stock xBuddy board with no hardware changes, and installs alongside Prusa's bootloader so you can go back to stock. It drives the printer's second board (enclosure fans, chamber sensor, LEDs) as a second Klipper MCU, uses the load cell for Z probing and clog detection, and keeps input shaping on the printer itself. That last choice is backed by the maker's own tests: shaping on the host caused 56× more starvation events on a Pi 4. Releases on Nov 14 and 15; the latest is a safety fix. Experimental, and not affiliated with Prusa. 4 stars. GPL-3.0.
- **[Kiln OS](https://github.com/djvalic/kiln-os)** by [Wes (djvalic)](https://github.com/djvalic). Open replacement firmware for the Flashforge Adventurer 5X: mainline Klipper, Moonraker, Fluidd and a touch UI on its own Linux build. The smart part is recovery. It uses the printer's two eMMC slots as a main system and a recovery OS, so a failed boot lands you in recovery instead of a brick. The installer also copies Flashforge's drivers from *your* printer, so none of Flashforge's files are in the repo. Eight releases between Nov 10 and Nov 13. The maker runs it on one printer and says "expect rough edges." GPL-3.0-or-later.
- **[Sutura](https://github.com/Krateian/Sutura)** by [Krateian](https://github.com/Krateian). Offline mesh repair for STL, OBJ and 3MF on Linux and macOS, with a Rust geometry core. Its 19 ranked repair methods have surgical names (Tamponade, Graft, Splint) behind one Repair button. It leaves clean models alone, always writes a copy, and tries to keep 3MF paint and supports. v0.9.9 (Nov 12) added a "Fidelity" score showing how far the repair moved your surface. License: PolyForm Noncommercial 1.0.0 (earlier versions were Apache-2.0), so check before using it commercially.

## From the bench

*Occasional section. Ethan prints something featured here on a Prusa MK3S and reports honestly on how it went.*

Shortlist for this issue: **[gridfinity-solidcraft](https://github.com/tharje/gridfinity-solidcraft)**. Its maker hasn't printed it yet and is asking for fit reports, so a bench test would be useful to them as well as to readers.

> *\[Ethan's bench notes go here: print settings, what fought back, and whether it was worth the filament.\]*

## Sign-off

That's issue #1. Know a passion project that deserves more than 30 stars? Reply and tell us. Self-promotion is welcome if you built it.

**House rules.** Every pick links to the maker's own page and is credited by name. We don't re-host makers' photos without permission. We note licenses so you know what you can remix, and we respect non-commercial terms. Weapon-related projects never appear here.

## Sources

- GitHub repository search for topics 3d-printing, 3d-printer, klipper, reprap, voron, toolchanger and non-planar, plus `topic:prusa` and ESP32 + printer/filament searches (pushed since Nov 1, under 150 stars; star counts and dates as of Nov 15, 2026)
- Release and commit history on each project's repo, linked in each section above
- [OrcaSlicer wiki: mixed nozzle sizes](https://www.orcaslicer.com/wiki/guides/mixed_nozzle_sizes), for context on stock OrcaSlicer's support
