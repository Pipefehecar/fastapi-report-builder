# Report Builder

Implementation of the Factory pattern for report generation using FastAPI background tasks. This service allows asynchronous creation of reports in different formats through a clean API interface.

## 🚀 Features

- Asynchronous report generation using background tasks
- Multiple report formats supported (PDF, Excel, CSV)
- Factory pattern implementation for extensible report types
- Queue management for report processing
- Real-time status tracking
- Secure file storage and retrieval

## 💻 Technologies

### Core
- Python 3.12+
- FastAPI
- Uvicorn
- Docker & Docker Compose

### Report Generation
- Pypdf (PDF)
- OpenPyXL (Excel)
- Pandas (Data Processing)

### Storage
- MinIO / S3
- PostgreSQL

## 🔧 Installation

### Using Docker (Recommended)

1. Clone the repository