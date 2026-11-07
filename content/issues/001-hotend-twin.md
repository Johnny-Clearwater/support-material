---
title: "A hotend that checks its own homework"
issue: 1
date: 2026-11-21
summary: "A physics-based digital twin that spots Ender 3 hotend faults from heater power alone, five quick finds from Klipper firmware to a printable fountain pen, and three small tools for calibration, monitoring and meshes."
draft: true
---

Support Material is a biweekly roundup of open-source 3D printing projects built by individuals who never advertised them. Every maker is credited and linked, and a project is only featured if the bigger outlets haven't covered it already.

## Deep cut: a hotend that checks its own homework

**[ender3-hotend-twin](https://github.com/batu63562/ender3-hotend-twin)** by Baturay Tatliatun ([batu63562](https://github.com/batu63562)) is a physics-based "digital twin" of an Ender 3 hotend. It runs next to Klipper and Moonraker on a Raspberry Pi. It has 10 stars, no forks and no watchers. That's a lot of careful engineering for an audience of nobody yet.

**The idea.** Klipper already knows how much power the heater is drawing. A small thermal model can work out how much power the heater *should* need to hold the current temperature. When the two numbers disagree, something changed at the nozzle. The README calls the heater a calorimeter. No extra sensors are needed.

**How it works.**

- A three-node thermal model, integrated with RK4, predicts the expected heater power each second.
- A Kalman filter learns two slow-moving factors: a general heat-loss factor `k`, and a heat-into-filament factor `k_fil`.
- Fast deviations in power raise one family of alarms. Drift in `k` raises another, and the README says the drift also feeds maintenance advice.
- Since v0.2, a persistent fast alarm can pause the print through Moonraker.

**Why it's worth your time.** The maker reports results with their limits attached. On the archived logs, the twin caught 24 of 31 labelled faults with a median delay of 26 s, and its 5 pauses were all on real faults. It also logged one false pause on a live print after a nozzle change. After that the author put pausing into shadow mode, then turned it back on 2026-10-28. The README states its limits too: ambient temperature is assumed constant at 25 °C, validation covers only PETG and TPU at 210–245 °C, and other hotends need recalibration. The author is asking for testers on other Klipper and Moonraker setups.

**At a glance**

| Item | Detail |
| --- | --- |
| Base machine | Creality Ender 3 with Klipper and Moonraker on a Raspberry Pi |
| Difficulty | Intermediate: Python, Klipper and Moonraker comfort needed, plus recalibration for your hotend |
| Status | v0.3, active; the README lists a 2026-10-28 change |
| Cost | Software only |
| Files | Source in the repo. A Windows viewer is released, but its Unity source is not public yet. |
| License | GPL-3.0 |

**Editor's note.** This software can pause a print on its own. Keep the printer's built-in thermal protection on, and treat the twin as an extra alarm. The author's own false pause is a good reason to start in shadow mode.

## Quick finds

Five small projects from individual makers.

- **[Kiln OS](https://github.com/djvalic/kiln-os)** by djvalic. Open firmware for the Flashforge Adventurer 5X. It is a Buildroot Linux system running mainline Klipper, Moonraker, Fluidd and a touch UI. It has two eMMC slots with a recovery OS, so a bad update falls back instead of bricking. The installer copies the Flashforge-specific files from your own printer rather than shipping them. The author runs it daily on one printer, and USB installs have only been tested under emulation. 21 stars, GPL-3.0-or-later.
- **[qidi-q2-klipper](https://github.com/n3oney/qidi-q2-klipper)** by n3oney. Patched mainline Klipper, Kalico and Katapult builds for the QIDI Q2, flashable without an ST-Link programmer. The README is blunt that it's unstable. Losing power mid-flash can brick an MCU, and recovery then needs an ST-Link. It builds on work by MisterSheikh and kuwoyuki. 22 stars, GPL-3.0.
- **[SparkShift](https://github.com/nisparks/SparkShift)** by nisparks. A quick-change hotend carriage built around an HGX drive for Voron-style printers, with an independent servo-driven cam release. It derives from the CxChanger/YUDX design, and the credits are in the repo. It is explicitly **not ready to print or use**: the README says fit, strength, retention and thermal safety are all unvalidated, and that the design is AI-assisted under human direction. Read it as a design in progress. 38 stars, GPL-3.0 with CC BY-SA 3.0 liners.
- **[SpinSlicer](https://github.com/redbluecarrot/SpinSlicer)** by redbluecarrot. A slicer and optical simulator for Computed Axial Lithography, the volumetric method that cures a whole part at once in a spinning vial. It turns an STL into projector frames, then simulates the match and the exposure margin. It runs in pure Python on CPU. Version 0.7.1, with Windows and Linux installers. 18 stars, MIT.
- **[White Feather Fountain Pen (wf672)](https://github.com/Xarfa/White-Feather-Fountain-Pen)** by Xarfa. A 3D-printable fountain pen that reworks the grooved "corn cob" capillary feed of Dandong Pen Factory's WhiteFeather line, made since 1968. STLs for v1.0.0 and v1.0.1 are in the releases. Print settings and assembly live on the maker's [project site](https://xarfa.github.io/wffp). 26 stars, CC BY 4.0.

## Tooling corner

- **[ScanNTune](https://github.com/jaak0b/ScanNTune)** by Jakob Eichberger. Caliper-free calibration from a flatbed scan. Print a coupon, scan it flat and again turned a quarter-turn, and the app averages the two to cancel the scanner's own error. A plastic ID card sets the scale. It runs in your browser (OpenCV.js, nothing uploaded) and outputs settings for Klipper, Marlin and RepRapFirmware. XY calibration is the solid part; the README calls XZ and YZ experimental. 23 stars, MIT.
- **[LayerPeek](https://github.com/pfoltynek/LayerPeek)** by Petr Foltýnek. A tray app that watches Prusa printers over PrusaLink on your local network, with a live camera, progress and notifications and no cloud account. It is read-only by design, so it can't pause or stop a print. It is tested on the CORE One with the Buddy3D camera only, and it doesn't support the MK3/MK3S. The README says most of the code was written with Claude Code under the maintainer's direction. Builds are unsigned, so expect OS warnings. 10 stars, GPL-3.0.
- **[MeshMill](https://github.com/make-your-own-world/MeshMill)** from the make-your-own-world account. A desktop tool for dense or incomplete meshes. It has QEM-based decimation with region selection, a Solidify tool for filling scan gaps, and a Cast tool that builds fitted clamshell molds. Processing is local. Windows x64 is the supported build at 0.4.0; the Linux and macOS downloads are older 0.2 previews. 18 stars, GPL-3.0-or-later.

## From the bench

*Occasional section. Ethan prints something featured here on a Prusa MK3S and reports honestly on how it went.*

> *\[Ethan's bench notes go here: print settings, what fought back, and whether it was worth the filament.\]*

## Sign-off

Know a passion project that deserves more than 30 stars? Reply and tell us. Self-promotion is welcome if you built it.

**House rules.** Every pick links to the maker's own page and is credited by name. We don't re-host makers' photos. We note licenses so you know what you can remix, and we respect non-commercial terms. Weapon-related projects never appear here.

## Sources

- [GitHub repository search](https://docs.github.com/en/rest/search/search#search-repositories), topics `3d-printing`, `3d-printer`, `klipper`, `reprap`, `voron`, `toolchanger`, pushed since 2026-10-24 (star counts as of Nov 7, 2026)
- Project repos linked in each section above
