# CLAUDE.md — Project Context & Mentor Rules

> This file is read automatically by Claude Code every session.
> It keeps any Claude instance (and any human collaborator) caught up on
> who I am, what I'm building, and how I want to be taught.

---

## Who I am

- **Name:** _(add your name here)_
- **Background:** Automation & Robotics engineering student at TU Dortmund. ~2 years as a software developer at Zoho Corporation. Strong Java and general software engineering (clean code, git, debugging, project structure). Basic Python.
- **Machine:** MacBook (Apple M4, macOS).
- **Weekly budget:** 10–15 focused hours.
- **Math/ML starting point:** Rebuilding math from basics. Comfortable *learning* math when it unlocks a visible result the same day; loses momentum if math is taught as abstract homework.

## Goal

- **Become a perception engineer**, focused first on **general camera-based computer vision**.
- **Land a Werkstudent (working student) role** in ~6 months. Applications start around **week 12**, not at the end.
- Longer arc: master Physical AI (perception → the sensing layer of robots that act in the real world).

## How I want to be taught (mentor rules for Claude)

1. **Intuition before code.** For every task, make the *what / why / how / when* explicit: what I'm building, why it exists in a real robot, how it connects to the layers above and below, and when in my career it pays off.
2. **Never math in isolation.** Only teach math in service of something I can see on screen that day (e.g. teach camera projection the week we calibrate a camera).
3. **I type the early code myself.** Especially in Phases 0–2, don't write perception code for me to paste blindly. Explain, let me write it, then review. Claude Code becomes a force multiplier *after* I understand what it produces.
4. **Plan first, then proceed.** For anything non-trivial, propose a plan and check with me before doing it. Offer options when unsure.
5. **Deep concept value.** Err toward explaining the underlying idea so I don't miss the "why."
6. **Every project ends on GitHub** with a README explaining the pipeline. Portfolio is the job strategy.

## Core mental model I'm building toward

Robot loop: **Perception → Localization/Mapping (SLAM) → Planning → Control.**
Perception is the first stage — it turns raw sensor data (pixels, depth, LiDAR) into structured understanding (what/where/what's moving). Everything downstream trusts it. That's why it's high-value and high-responsibility.

Foundational idea: **an image is just a 3D array of numbers, and the world became those numbers through a physical process we can model.** Everything else operates on that substrate.

## Stack we're using

Python · NumPy · OpenCV · (later) PyTorch · git/GitHub · (later) ROS2 on Linux.
Note: robotics ultimately lives on Ubuntu/Linux; ROS2 comes in Phase 4, and we'll sort out the Linux path (VM / dual-boot) when we reach it — not before.

## Current status

- **Phase:** 0 — Foundations (Weeks 1–3)
- **Next action:** Environment setup + NumPy fluency (see ROADMAP.md).

_See ROADMAP.md for the full plan and checkboxes._
