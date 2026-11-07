---
title: "Pilot issue"
issue: 0
date: 2026-11-07
summary: "A PCB factory bolted onto a Sovol SV08, four ESP32-and-tooling quick finds, three Prusa-friendly tools, and a Prusawire bench candidate."
---

Support Material is a biweekly roundup of open-source 3D printing projects built by individuals who never advertised them.  "The work speaks for itself" is a fallacy. People speak for the work. Support Material speaks up for the small but mighty maker. These makers are credited, linked, and are only featured if a bigger outlet does not cover them already.

## Deep cut: a PCB factory bolted onto a Sovol SV08

**[Hybrid MicroElectronics-Factory 3D Printer](https://hackaday.io/project/204938-hybrid-microelectronics-factory-3d-printer)** by [Joanbelk](https://hackaday.io/hacker/252997-joanbelk) turns a Sovol SV08 into a toolchanging electronics fab. It has about 2.5k views, 27 followers, and zero comments. That's criminally low for what it is.

**The origin story.** Joanbelk is a mechatronics student in the Dominican Republic. Custom PCBs took three weeks to ship from China, and commercial printed-electronics machines cost $50,000+. So the plan became: build the fab instead.

**What it does.** A Stealthchanger-style tool shuttle swaps between tools on one CoreXY machine:

- An FDM extruder prints the ASA/PC body and the insulating layers.
- A 10 W, 450 nm laser handles etch masks, cutting, and laser-induced graphene.
- A syringe dispenser lays down conductive paste.
- A wire embedder sinks copper wire for power and data runs.
- A drag-knife/pen tool cuts foil and plots silkscreen.
- Pick-and-place and in-situ etching are listed as future goals.

**Why it's clever.** The real goal is electronics where the circuit *is* the structure, printed in place. One trick is especially good: calibrating a paste syringe works just like tuning a filament extruder in OrcaSlicer, with flow, pressure-advance, and retraction tests. The logs are refreshingly honest about failures. Copper tape lifts off, etch gel undercuts 10 mil traces, inks clog the nozzle, and the maker writes that a 5 W laser would have been enough.

**At a glance**

| Item | Detail |
| --- | --- |
| Base machine | Sovol SV08 (CoreXY, Klipper) |
| Difficulty | Advanced: toolchanger, laser, wet chemistry |
| Status | Active research project; last log Aug 22, 2026 |
| Cost | Not published |
| Files | Fusion 360 models linked from the project page; source repo at [github.com/jbk95/HybridMicroFab](https://github.com/jbk95/HybridMicroFab) |
| License | Not stated on the project page; check the repo before remixing |

**Editor's note.** This build involves acid etching, metal-oxide inks, and a laser that can blind you. We're not reproducing the chemistry here, and the maker notes their reactive-ink recipe was hard to dial in. Read the logs for the journey; get proper safety gear before trying any of it.

## Quick finds

Four small builds from individual makers, none of which we could find covered by the major 3D printing outlets.

- **[IkeDryBox](https://github.com/byte4geek/IkeDryBox)** by byte4geek. The internet has a hundred passive IKEA Samla dry boxes. This one makes it an *active* dryer, with an ESP32, PID heat control, a web UI, and Home Assistant/MQTT hooks. It supports both common "Cheap Yellow Display" boards. MIT licensed.
- **[3d-Enclosure-Controller](https://github.com/codenquilts/3d-Enclosure-Controller)** by codenquilts. One ESP32 runs two separate printer enclosures, with fans, lights, temperature, and filament presets. The clever bit: it tells whether a printer is idle by watching its smart plug's power draw, then shuts that enclosure down. The README even warns you to check heat soak and pauses don't fool the threshold.
- **[esp32-spacepi-dryer-controller](https://github.com/DRCRecoveryData/esp32-spacepi-dryer-controller)** by DRCRecoveryData. Replacement brains for a Creality SpacePi filament dryer, built on an ESP32 Cheap Yellow Display touchscreen. It adds a BME280 sensor, 35–66 °C timed drying, automatic cooldown safeguards, a web dashboard, and OTA updates.
- **[diff3d](https://github.com/bdlucas1/diff3d)** by bdlucas1. A fast visual diff for STL, OBJ, 3MF, and STEP files. It answers the question every designer asks too late: what actually changed between rev B and rev C? 77 stars, Python.

## Tooling corner

Three small-developer tools, all updated in the last four months. Two are especially useful if you're still running an older Prusa.

- **[Panda2Prusa](https://github.com/CupsOhJoe/Panda2Prusa)** by CupsOhJoe. It converts Bambu Studio 3MF files into PrusaSlicer projects, keeping transforms, multicolor painting, and per-part extruder assignments. If you've ever downloaded a great multicolor model that only opens properly in Bambu's slicer, this is the fix. 36 stars; last updated July 2026.
- **[MINI404](https://github.com/vintagepc/MINI404)** by vintagepc. A firmware-level simulator for Prusa MK3.x, MK4, MINI, and XL boards. You can test firmware changes and custom G-code on a virtual printer before you risk the real one. It's the successor to the same author's MK404, and it was updated this week.
- **[Gantrybar](https://github.com/parametryczny/Gantrybar)** by parametryczny. A lightweight menu-bar/tray monitor for a printer fleet, covering Bambu, Klipper/Creality, Prusa, and Snapmaker. It's local-first and runs on macOS, Windows, and Linux. 64 stars.

## From the bench

*Occasional section. Johnny prints something featured here on a Prusa MK3S and reports honestly on how it went.*

No bench test this issue. Here's the one on the shortlist:

**[Prusawire](https://github.com/Positron3D/Prusawire)**, from the team behind the Positron. It started as their April Fools' joke in 2025 and grew into a real conversion. It turns MK3/MK3S/MK4 leftovers into a Voron Switchwire-style CoreXZ printer. Release 2026.R1 shipped on July 24, 2026, along with a web configurator for picking which parts to print. The printed parts take about 1,060 g of primary filament plus 225 g of accent. GPL-3.0.

It's not a Support Material pick, since All3DP covered the beta in 2025. It is the most on-brand bench test imaginable, though: an old MK3S teaching itself new tricks.

> *\[Johnny's bench notes go here: print settings, what fought back, and whether it was worth the filament.\]*

## Sign-off

That's the pilot. Know a passion project that deserves more than 30 stars? Reply and tell us. Self-promotion is welcome if you built it.

**House rules.** Every pick links to the maker's own page and is credited by name. We don't re-host makers' photos without permission. We note licenses so you know what you can remix, and we respect non-commercial terms. Weapon-related projects never appear here.

**Pilot note.** Future issues stick to a two-week window. Issue #0 relaxed that so we could pick the best long-tail finds from recent months.

## Sources

- [Hackaday.io: Hybrid MicroElectronics-Factory 3D Printer](https://hackaday.io/project/204938-hybrid-microelectronics-factory-3d-printer)
- [GitHub topic: prusa](https://github.com/topics/prusa) (star counts and update dates as of Nov 7, 2026)
- [Positron3D/Prusawire](https://github.com/Positron3D/Prusawire) and [All3DP's 2025 Prusawire coverage](https://all3dp.com/4/the-prusawire-project-uses-mk4s-leftovers-to-build-a-corexz-printer/)
- Project repos linked in each section above
