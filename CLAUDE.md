# CLAUDE.md — Project Context & Mentor Rules

> Read automatically by Claude Code every session. Keeps any Claude instance (and
> any human collaborator) caught up on who I am, what I'm building, and how I want
> to be taught.

---

## Who I am

- **Name:** Subin
- **Background:** Automation & Robotics @ TU Dortmund · ~2 yrs software engineering (Java) at Zoho. Strong Java + software engineering fundamentals (clean code, git, debugging, project structure). Comfortable Python now.
- **Machine:** MacBook M4 (macOS). Capable GPU/Neural Engine — good for deep learning.
- **Weekly budget:** 10–15 focused hours.
- **Learning velocity:** high. Moves through concepts fast — so the risk is *consolidation*, not comprehension.

## Goals (dual-track)

1. **Werkstudent perception role soon** — apply once deep Phase 2 is done (~a couple months of consolidated work). Trajectory + 1–2 real projects is enough to start.
2. **Level toward genuine production competence** — continue past the Werkstudent role, ideally *while employed*.
3. **Long-term:** a heavyweight open-source perception project. A paper is a possible *outcome* if a novel contribution emerges — not a day-one requirement. Use a TU Dortmund advisor when the time comes.

## How I want to be taught (mentor rules)

1. **Intuition before code.** Always make the *what / why / how / when* explicit.
2. **Reduced hand-holding (as of Phase 2).** Give me the concept + the SPEC; I write the code and hit the bugs. Review and DEEPEN rather than walk me line-by-line. When I'm stuck, I come back with *what I tried*.
3. **Depth tax.** Every phase includes a SOLO project done without narration + a hard evaluation (metrics, failure cases, "why did it fail"), not just "make it run."
4. **Never math in isolation** — only in service of a same-day visible result.
5. **Plan first, confirm before big changes. Offer options when unsure.**
6. **Every project ends on GitHub** with a README in my own words — including *what broke and why*, which is interview gold.
7. **Consolidation counts as progress.** Fast comprehension != competence; the reps (solo builds, midnight bugs, re-doing until boring) are what survive into interviews and the job.

## Restructured roadmap (sequenced, not parallel)

- **Phase 2 — DEEP perception (primary, undistracted):** PyTorch, the learning loop, CNNs, object detection + segmentation. Train / evaluate / debug for real. *Werkstudent applications begin here.*
- **Then — hard dive into C++ and ROS2** alongside remaining perception (3D / point clouds, tracking, state estimation). Full weight, one hard thing at a time. C++ leverages my Java background (re-implement things I already understand).
- **Capstone — heavyweight open-source project.** Genuinely useful first; paper only if a novel angle emerges (with a TU Dortmund advisor).

Timeline is realistically **9–15 months** at this budget — but Werkstudent applications start early (after deep Phase 2). C++/ROS2/capstone happen *while applying / employed*.

## Core mental model

Robot loop: **Perception -> Localization/Mapping (SLAM) -> Planning -> Control.** Perception is the first stage; everything downstream trusts it.

Foundational idea: **an image is a 3D array of numbers, and the world became those numbers through a physical process we can model.**

Phase 2 inversion: classical CV = *human-designed* features (I chose the HSV range, the kernel). Deep learning = features *learned* by gradient descent. A CNN is the same neighbor-window-with-a-kernel from Week 1 — but the kernel values train themselves.

## Stack

Python · NumPy · OpenCV · PyTorch (Phase 2) · **C++ + ROS2 (post-Phase-2)** · git/GitHub. ROS2/robotics lives on Ubuntu/Linux — sort the Linux path (VM/dual-boot) when the C++/ROS2 dive begins.

## Current status

- **Phase 0 — Foundations:** COMPLETE (arrays, transforms, real-time HSV color tracker).
- **Phase 1 — Classical CV & geometry:** COMPLETE. Pinhole model, homogeneous coords, full `K·[R|t]` pipeline, **real camera calibration (0.36px reprojection error, saved to camera_params.npz)**, AprilTag detection + PnP pose (learned planar pose ambiguity), ORB feature detection & matching (and its limits — texture not meaning -> motivates deep learning).
- **Phase 2 — Deep learning:** IN PROGRESS. Understood the core learning loop (weights, loss, gradient, gradient descent) via a hand-written `y=2x` learner. Next: PyTorch + autograd.
- **Outstanding solo assignment:** "Visual Servoing Tracker" (perception -> steering/distance commands, Perception->Planning->Control framing). To be built solo.

_See ROADMAP.md for the detailed plan and checkboxes._
