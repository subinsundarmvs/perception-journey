# ROADMAP — Perception Engineer in 6 Months

**Budget:** 10–15 hrs/week · **Focus:** general camera CV · **Job applications start:** ~Week 12

Check items off as you go. Each phase has a *why* so you never lose the thread.

---

## Phase 0 — Foundations (Weeks 1–3)
*Why: everything in perception is arrays and geometry. Build that intuition in your hands first.*

### Week 1 — Images are numbers
- [ ] Install Node.js, Python, VS Code, git
- [ ] Set up virtual env + install `numpy`, `opencv-python`, `matplotlib`
- [ ] Create + push the `perception-journey` GitHub repo
- [ ] Learn NumPy: arrays, slicing, broadcasting, `.shape`
- [ ] **Deliverable:** notebook that loads, inspects, and manipulates image pixels
- [ ] Understand: every image/model/paper operates on an ndarray

### Week 2 — Matrices move the world
- [ ] Watch 3Blue1Brown *Essence of Linear Algebra* (~2.5h across the week)
- [ ] Apply it: rotate/translate/scale an image with `cv2.warpAffine`
- [ ] **Deliverable:** transform script + short note on what the matrix does
- [ ] Understand: a matrix is a transformation of space

### Week 3 — Your first perception output
- [ ] Learn color spaces (why HSV beats RGB for detection)
- [ ] Learn convolution / filtering (blur, Sobel edges)
- [ ] **Mini-project:** color-based object tracker on your webcam
- [ ] **Deliverable:** tracker + README explaining the pipeline
- [ ] Understand: convolution is the operation that makes CNNs click later

---

## Phase 1 — Classical CV & Camera Geometry (Weeks 4–9)
*Why: understand how the world becomes pixels before you throw a neural net at it.*

- [ ] Image formation + the pinhole camera model
- [ ] Camera calibration (intrinsics, distortion) with a checkerboard
- [ ] Feature detection & matching (ORB/SIFT-style)
- [ ] Homography & perspective transforms
- [ ] **Project:** camera calibration + augmented-reality marker overlay
- [ ] **Deliverable:** repo + README + demo GIF

---

## Phase 2 — Deep Learning for Vision (Weeks 10–16)
*Why: learned features beat hand-crafted ones — this is modern perception.*

- [ ] PyTorch fundamentals (tensors, autograd, training loop)
- [ ] CNNs: what convolution layers learn
- [ ] Object detection (fine-tune a pretrained detector, e.g. YOLO-family)
- [ ] Semantic segmentation basics
- [ ] **Project:** fine-tune a detector on your own small custom dataset
- [ ] **Deliverable:** repo + README + evaluation notes
- [ ] ⭐ **Week 12: start applying to Werkstudent roles** (polish CV + GitHub first)

---

## Phase 3 — Video & Tracking (Weeks 17–21)
*Why: the world is 3D and moves; single frames aren't enough.*

- [ ] Motion & optical flow
- [ ] Multi-object tracking (association across frames)
- [ ] Intro to Kalman filtering (predict + correct)
- [ ] **Project:** real-time multi-object tracker
- [ ] **Deliverable:** repo + README + demo video

---

## Phase 4 — Integration & Polish (Weeks 22–24)
*Why: perception doesn't live alone — it feeds a robot system.*

- [ ] Sort out the Linux path (VM / dual-boot) for ROS2
- [ ] ROS2 taste: nodes, topics, publish a perception result
- [ ] **Capstone:** chain perception into a small simulated robot pipeline
- [ ] Portfolio cleanup: pin best repos, write clear READMEs
- [ ] Interview prep: be able to explain every project's *why/how*
- [ ] Continue + iterate on job applications

---

## Running principles
- Never learn math in isolation — only to unlock a same-day result.
- Type early code yourself; understand before automating.
- Every project ends on GitHub with a README.
- Applications are a *trajectory*, not a finish line — start early, keep going.
