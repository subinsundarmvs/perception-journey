# ROADMAP — Perception Engineer (restructured, harder plan)

**Budget:** 10–15 hrs/week · **Werkstudent applications:** start after deep Phase 2
**Timeline:** realistically 9–15 months for the full arc (apply early, keep leveling)

Principle: **one hard thing at a time, done properly.** Perception deep first, THEN a
full C++/ROS2 dive, THEN a heavyweight OSS capstone. Depth comes from doing +
evaluating, not from more explanation. Reduced hand-holding from Phase 2 on.

---

## Phase 0 — Foundations ✅ COMPLETE
Arrays, pixel manipulation, uint8 wrap-around, affine transforms + composition order,
real-time HSV color tracker with mask cleanup. Reviewed.

## Phase 1 — Classical CV & Camera Geometry ✅ COMPLETE
- [x] Pinhole camera model (3D->2D, why depth is destroyed)
- [x] Homogeneous coordinates + the matrix-division trick
- [x] Full projection pipeline `pixel = K · [R|t] · point`
- [x] Real camera calibration — **0.36px reprojection error**, saved camera_params.npz
- [x] Undistortion from measured coefficients
- [x] AprilTag detection + PnP pose (learned planar pose ambiguity)
- [x] ORB feature detection & matching — AND its limits (texture, not meaning)
- [ ] Commit all Phase 1 code + READMEs, tick off in repo

## Phase 2 — DEEP Learning for Vision (IN PROGRESS — primary focus)
*Not a taste. Train, evaluate, debug, understand. Reduced hand-holding.*
- [x] The learning loop: weights, loss, gradient, gradient descent (hand-written y=2x)
- [ ] PyTorch + tensors + autograd (why automatic gradients matter)
- [ ] Build + train a small neural net from scratch
- [ ] CNNs: why convolution fits images; learned kernels vs hand-set kernels
- [ ] Object detection (YOLO-family): what's WHERE, with boxes
- [ ] Semantic segmentation basics
- [ ] **DEPTH TAX — solo project:** fine-tune a detector on my OWN dataset;
      report precision/recall, find + explain failure cases. Portfolio-grade.
- [ ] Outstanding: build the "Visual Servoing Tracker" assignment SOLO
- [ ] ⭐ **Start Werkstudent applications** (polish CV + GitHub first)

## Phase 3 — C++ & ROS2 Hard Dive + Remaining Perception (post-Phase-2)
*Full weight now. Industry-facing systems layer.*
- [ ] Sort the Linux path (VM / dual-boot) for ROS2
- [ ] C++ fundamentals via re-implementing things I already know (transform, filter)
- [ ] ROS2 proper: nodes, topics, services; publish perception results
- [ ] 3D perception: point clouds, LiDAR data (public datasets — KITTI/nuScenes)
- [ ] Tracking + state estimation: Kalman / EKF, multi-object tracking
- [ ] A perception node running live inside ROS2

## Phase 4 — Heavyweight Open-Source Capstone
*Genuinely useful first; paper only if a novel angle emerges (+ TU Dortmund advisor).*
- [ ] Scope a substantial, genuinely-useful perception project
- [ ] Build it well: clean C++/Python, ROS2 integration, real evaluation
- [ ] Strong docs, reproducibility, open-source hygiene
- [ ] IF a novel contribution appears -> pursue publication with an advisor

---

## Running principles
- Fast comprehension != competence. Consolidate via SOLO reps.
- Reduced hand-holding: I get the spec, I write the code, I debug, mentor reviews + deepens.
- Every phase: a solo project + a hard evaluation (metrics + failure analysis).
- Apply for Werkstudent EARLY; keep leveling toward production while employed.
- Never learn math in isolation; every project ends on GitHub with an honest README.
