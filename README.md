
# 🧑‍🏫 SnapClass — AI-Powered Attendance System

https://snapclass-tracker.streamlit.app/

SnapClass is an **AI-powered attendance management system** that combines **face recognition and voice authentication** to provide secure and reliable attendance tracking.

By integrating **face embeddings with voice authentication**, SnapClass adds multiple layers of identity verification to help **reduce proxy attendance** and improve the reliability of attendance records.

## 🚀 Features

- **Face Authentication**
  - Uses face embeddings for student identity verification.
  - Captures and processes facial information for authentication.

- **Voice Authentication**
  - Uses voice embeddings for speaker verification.
  - Provides an additional biometric authentication layer.

- **Anti-Proxy Attendance**
  - Combines face and voice verification before marking attendance.
  - Helps reduce unauthorized or proxy attendance.

- **Teacher Portal**
  - Manage students and subjects.
  - Initiate attendance sessions.
  - View attendance records.

- **Student Portal**
  - Authenticate using biometric verification.
  - Participate in attendance sessions.
  - View attendance history.

- **Secure Authentication**
  - Password hashing using `bcrypt`.
  - Supabase-based database management.
  - Biometric verification.
  - Row Level Security (RLS).

- **QR-Based Attendance**
  - QR codes can be used to initiate attendance sessions.

## 🏗️ System Workflow

                    ┌─────────────────┐
                    │     Student     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Attendance      │
                    │ Session / QR    │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
          ┌─────────────────┐ ┌──────────────────┐
          │ Face Recognition│ │ Voice Recognition│
          └────────┬────────┘ └────────┬─────────┘
                   │                   │
                   ▼                   ▼
          ┌─────────────────┐ ┌─────────────────┐
          │ Face Embedding  │ │ Voice Embedding │
          └────────┬────────┘ └────────┬────────┘
                   │                   │
                   └─────────┬─────────┘
                             ▼
                    ┌─────────────────┐
                    │ Identity        │
                    │ Verification    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Attendance      │
                    │ Recorded        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Supabase     │
                    │    Database     │
                    └─────────────────┘

## 🧠 How It Works

### 1. Face Verification

The student's face is captured and processed to generate a **face embedding**.

```text
Input Image
     ↓
Face Detection
     ↓
Face Embedding
     ↓
Compare with Registered Embedding
     ↓
Face Verified

```

## 2. Voice Verification
The student's voice is captured and processed to generate a voice embedding.
```text
Voice Input
     ↓
Audio Processing
     ↓
Voice Embedding
     ↓
Compare with Registered Voice
     ↓
Voice Verified
```

## 🛠️  Tech Stack
UI - Streamlit
Face Recognition - 	dlib, Face Recognition Models
Voice Recognition - 	Resemblyzer, Librosa
Machine Learning - 	Scikit-learn
Database - 	Supabase
Authentication -	bcrypt
QR Code - 	Segno
Image Processing.- 	Pillow
Data Processing - 	NumPy, Pandas


## 🔐 Security
SnapClass incorporates multiple security mechanisms:
🔑 Password hashing using bcrypt
👤 Face-based identity verification
🎙️ Voice-based speaker verification
🗄️ Supabase database security
🛡️ Row Level Security (RLS)
👨‍🏫 Separate teacher and student access
