# LVDrive 🚗

A Django web application for luxury vehicle rental and lending that connects car owners with renters in a secure peer-to-peer marketplace.

## Overview

LVDrive provides a comprehensive platform where users can:

**For Renters:**
- Browse and search through a curated collection of luxury vehicles
- View detailed car specifications, photos, and owner reviews
- Book vehicles with real-time availability checking
- Manage reservations and rental history through a personal dashboard
- Rate and review vehicles after rental experiences

**For Car Owners:**
- List luxury vehicles with detailed descriptions and photo galleries
- Set pricing, availability calendars, and rental terms
- Manage booking requests and communicate with potential renters
- Track earnings and rental performance
- Build reputation through renter reviews

**Platform Features:**
- Secure user authentication and profile management
- Advanced search and filtering capabilities
- Integrated review system for trust and safety
- Cloud-based media storage for high-quality vehicle images
- RESTful API
- Comprehensive admin tools for platform management

## Tech Stack

- **Django** 5.2.4
- **Django REST Framework** 3.16.0
- **PostgreSQL** with psycopg2
- **Cloudinary** for media storage
- **WhiteNoise** for static files
- **drf-spectacular** for API documentation
- **Pillow** for image processing
- **python-decouple** for environment management

## Django Apps

- **accounts** - User authentication and profile management
- **cars** - Vehicle listings and management
- **bookings** - Reservation and booking system
- **reviews** - Rating and review system for cars and users
- **home** - Landing page and core application views
