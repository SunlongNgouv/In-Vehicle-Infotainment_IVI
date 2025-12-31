# IVI QA Automation Framework (Pytest + BDD)

## 📌 Project Overview

This repository demonstrates my progressive learning and practical application of QA automation principles using Python and Pytest, following a real-world SDET workflow.

The project simulates In-Vehicle Infotainment (IVI) system testing, inspired by modern automotive QA practices, where test frameworks are built incrementally and extended as system complexity grows.

Rather than waiting to master every tool upfront, this project follows a layered evolution approach, mirroring how QA automation is developed in production environments.

## 🎯 Project Goals

1. Build a scalable Pytest-based automation framework
2. Apply BDD (Behavior-Driven Development) for clear test design
3. Demonstrate test discovery, fixtures, and parametrization
4. Show learning progression from core testing logic to advanced tooling
5. Prepare a foundation for Android IVI, Appium, CI/CD, and reporting

## 🧠 Learning Progression Strategy

This project is intentionally developed in phases, not all at once.

#### ✅ Phase 1: Core QA Automation (Current)

__Focus:__

Solid fundamentals before tooling complexity

__What’s included:__

- Pytest test discovery
- Fixtures (session, function scope)
- Parametrized tests
- BDD scenarios using pytest-bdd
- Mocked IVI system logic (no UI dependency)
- Clean project structure
- Readable, business-focused test scenarios

__Why this phase matters:__

- Ensures tests are maintainable and scalable
- Separates test design from implementation
- Matches real-world SDET onboarding practices

#### 🔜 Phase 2: Android IVI UI Automation (Planned)

__Planned additions:__

- Appium integration
- Android Emulator (IVI-style apps)
- Page Object Model (POM)
- Replace mocked system with real UI interactions

__Why later:__

- UI automation is most effective after framework stability
- Prevents brittle tests and overengineering early on

#### 🔜 Phase 3: Reporting & Observability (Planned)

__Planned additions:__

- Allure reporting
- Screenshot & log attachments
- Failure trend analysis

__Purpose:__

- Improve test triage efficiency
- Support CI/CD feedback loops

#### 🔜 Phase 4: CI/CD & Metrics (Optional)

__Potential extensions:__

- GitHub Actions or Jenkins
- Test execution on pull requests
- Test stability metrics
- Grafana dashboards (optional)

## 🧪 Why BDD?

BDD is used to:
- Express test cases in business-readable language
- Improve collaboration between QA, developers, and stakeholders
- Keep test intent clear even as implementation changes

Example:

Feature: IVI system boot
  Scenario: System boots successfully
    Given the IVI system is powered off
    When the system is powered on
    Then the home screen should be available


This approach allows test logic to evolve without rewriting scenarios.

## 📂 Project Structure
```
ivi-qa-framework/
├── features/
│   ├── system_boot.feature
│   ├── media.feature
│   └── bluetooth.feature
│
├── tests/
│   ├── test_system.py
│   ├── test_media.py
│   ├── test_bluetooth.py
│   └── conftest.py
│
├── src/
│   └── ivi_system.py   # mocked IVI logic
│
├── pytest.ini
└── README.md
```

This structure reflects industry-standard QA automation design.

## 🛠️ Technologies Used (Current Phase)

- Python
- Pytest
- pytest-bdd
- Logging
- Mock-based system simulation

## 🚗 Automotive & IVI Context

Although this phase uses mocked logic, the test scenarios and structure are designed to mirror real IVI systems, such as:

- System boot validation
- Media service availability
- Bluetooth service behavior
- Settings state validation
- This ensures the framework can later be extended to:
- Android Automotive OS
- Hardware-in-the-loop (HIL) testing
- Embedded Linux environments

## 📈 Why This Project Matters

This repository demonstrates:
- QA automation thinking, not just scripting
- Ability to learn tools incrementally
- Strong understanding of test architecture
- Readiness for SDET / QA Automation Engineer roles

It reflects how automation frameworks are built and evolved in real engineering teams.

## 🔄 Future Enhancements

- Appium-based Android IVI automation
- Allure test reporting
- CI pipeline integration
- Image-based UI validation
- Protocol simulation (CAN / Bluetooth scenarios)

## 📬 Author

Sunlong Ngouv
QA Automation / Application Support / System Integration
Python | Pytest | BDD | CI/CD | ERP & System Testing
