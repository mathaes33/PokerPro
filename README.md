# PokerPro
== Milestones

=== Milestone 1: Core Backend Functionality
- [ ] Flask API setup with `/ocr` endpoint
- [ ] OCR pipeline working with Tesseract
- [ ] Regex-based parser extracting players and pot
- [ ] GameState data structure populated correctly

=== Milestone 2: Strategy Engine
- [ ] Implement basic Monte Carlo equity calculator
- [ ] Integrate equity with parsed game state
- [ ] Create action recommendation stub

=== Milestone 3: Frontend App Integration
- [ ] React Native app with image upload
- [ ] Send image to backend, show OCR + parsed data
- [ ] Format results in simple UI

=== Milestone 4: Persistence and Replay
- [ ] SQLAlchemy models for sessions, players, images
- [ ] Save every request with timestamp
- [ ] (Optional) Add image gallery or log in frontend

=== Milestone 5: Desktop Overlay (Optional)
- [ ] Basic Electron overlay to display live game info
- [ ] Transparent window overlaying PokerStars table
- [ ] Hotkey to toggle visibility

=== Milestone 6: Testing and CI
- [ ] Unit tests for parser and equity logic
- [ ] GitHub Actions for backend + React Native CI

PokerPro/
├── backend/
│   ├── app.py
│   ├── ocr.py
│   ├── parser.py
│   ├── strategy_engine.py
│   ├── models.py
│   └── utils.py
├── frontend/
│   ├── App.js
│   └── components/
├── overlay/
│   ├── main.js
│   └── renderer.js
├── .github/
│   └── workflows/
├── uploads/
├── README.md
├── requirements.txt
└── LICENSE