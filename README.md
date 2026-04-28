Smart Restaurant Reservation & Operations Platform


1. Executive Summary

This project is a lightweight full-stack hospitality software prototype built as a portfolio and interview demonstration.
It combines:
• Restaurant website front-end
• Reservation management backend API
• Persistent relational database storage
• Basic operational analytics dashboard

Business idea:
Demonstrate how a restaurant can manage digital customer interactions (bookings), operational data, and simple analytics using modern web technologies.

Value delivered:
• Digital reservation workflow
• Reduced manual booking handling
• Structured data capture
• Basic operational reporting
• Foundation for future POS, inventory, and CRM extensions.


2. Business Problem Solved

Restaurants often manage reservations manually through phone calls, social media messages, or disconnected tools.
Problems:
• Double bookings
• Poor visibility into reservations
• Limited digital presence
• Lack of operational data

This solution addresses:
1. Website-based booking intake
2. Central reservation database
3. Reservation retrieval
4. Operational metrics visibility
5. Foundation for scalable restaurant software


3. Technology Stack

Frontend
• HTML
• CSS
• JavaScript

Backend
• Python
• FastAPI
• SQLAlchemy ORM

Database
• SQLite (prototype persistence)

Development Tools
• Virtual environment (venv)
• Swagger API docs
• Git/GitHub


4. System Architecture

User submits reservation on landing page
-> JavaScript sends POST request
-> FastAPI endpoint receives request
-> CRUD layer stores record using SQLAlchemy
-> SQLite database persists booking
-> GET endpoints fetch stored reservations
-> Frontend dashboard displays retrieved data

Flow:
Frontend -> API -> ORM -> Database -> API -> Frontend


5. Project Structure

restaurant-ops-platform/
app/
  main.py
  database.py
  models.py
  schemas.py
  crud.py
  routers/
    reservations.py
    tables.py
    analytics.py

frontend/
  index.html
  style.css
  script.js

restaurant.db


6. Backend Components 

database.py
Defines database engine, session, and ORM base.

models.py
Defines relational tables:
• Reservation
• Table

schemas.py
Pydantic validation models for incoming API requests.

crud.py
Contains database operations:
• create reservation
• fetch reservations
• create tables
• fetch tables

routers/reservations.py
API endpoints:
POST /reservations
GET /reservations

routers/tables.py
API endpoints:
POST /tables
GET /tables

routers/analytics.py
Dashboard metrics endpoint

main.py
Application startup
Router registration
CORS middleware
Swagger documentation


7. Frontend Components 

index.html
Contains:
• Landing page
• Reservation form
• Reservations list
• Dashboard section

style.css
Provides website styling.

script.js
Contains:
• Form submission to backend
• Fetch reservations
• Fetch dashboard metrics
• Dynamic rendering of returned data


8. Database Persistence

Database:
restaurant.db (SQLite)

Stored locally in project root.

Reservation submission persists because:
db.add()
db.commit()

Data remains after server restarts.

Prototype uses local SQLite but can migrate to PostgreSQL.


9. API Endpoints

GET /
Health endpoint

POST /reservations
Create booking

GET /reservations
Fetch all bookings

POST /tables
Create tables

GET /tables
List tables

GET /analytics/dashboard
Operational dashboard


10. Business Value

Operational Value
• Digitizes reservations
• Supports website management
• Demonstrates service-industry software thinking

Management Value
• Basic occupancy insights
• Reservation visibility
• Foundation for decisions

Technical Value
• Full-stack prototype
• API-driven architecture
• Extendable software foundation
