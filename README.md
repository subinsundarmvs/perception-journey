# perception-journey

My public logbook while transitioning from software engineering into **perception engineering** — the sensing layer of robots that act in the physical world (Physical AI).

**Focus:** general camera-based computer vision → classical CV → deep learning for vision → tracking → ROS2.
**Background:** Automation & Robotics @ TU Dortmund · ~2 yrs software engineering (Java) at Zoho.
**Goal:** Werkstudent perception role, building in the open the whole way.

> Author: _(add your name)_ · Machine: MacBook M4 (macOS)

---

## Tech stack
Python · NumPy · OpenCV · matplotlib · (soon) PyTorch · (later) ROS2 · git/GitHub

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Progress

| Phase | Weeks | Status |
|-------|-------|--------|
| **0 — Foundations** (arrays, transforms, first tracker) | 1–3 | 🔨 in progress |
| 1 — Classical CV & camera geometry | 4–9 | ⏳ |
| 2 — Deep learning for vision | 10–16 | ⏳ |
| 3 — Video & tracking | 17–21 | ⏳ |
| 4 — Integration, ROS2 & capstone | 22–24 | ⏳ |

See [`ROADMAP.md`](ROADMAP.md) for the full week-by-week plan.

## What lives where
- `phase0-foundations/week1-images-are-numbers/` — images as arrays, pixel manipulation
- `phase0-foundations/week2-matrices/` — affine transforms, composition order
- `phase0-foundations/week3-color-tracker/` — first real-time perception system

Each week's folder has its own short `README.md` in my own words — the *why*, not just the code.
