<div align="center">
  <p> The Celtic Spoon </p>
</div>
<div align="center">
  <img src="/assets/images/logo.png" alt="Home Page">
</div>

## Table of Contents 

1. [Project Overview](#1-project-overview)
2. [Live Preview](#2-live-preview)
3. [UX & User Stories](#3-ux--user-stories)
4. [Design & Wireframes](#4-design--frames)
5. [Database Schema](#5-database-schema)
6. [Features / Key Highlights](#6-features--key-highlights)
7. [Security Features](#7-security-features)
8. [Technologies Used](#8-technologies-used)
9. [Testing Documentation](#9-testing-documentation)
10. [Deployment](#10-deployment)
11. [Credits](#11-credits)

## 1. Project Overview

The Celtic Spoon is designed as a modern and welcoming restaurant website, celebrating the rich flavors of Celtic cuisine blended with inspirations from Irish, Scottish, and Northern European culinary traditions. Its goal is to give visitors a sense of the restaurant’s atmosphere and menu offerings, while highlighting signature dishes that fuse classic Celtic recipes with contemporary flavors from neighboring cultures. 

In addition, the menu creatively incorporates subtle Turkish culinary influences, offering a unique fusion experience for adventurous diners. Traditional Celtic dishes might be enhanced with Turkish spices, yogurts, or pastries, creating an innovative blend of flavors that reflects both authenticity and creativity in Celtic culinary culture.

Minimalistic design principles are applied to ensure that key information and visuals, such as featured dishes, chef specials, and restaurant highlights, stand out without distractions.

## 2. Live Preview

Live demo link: https://the-celtic-spoon-fd61489fc4df.herokuapp.com/

## 3. UX & User Stories

## User Stories

### Authentication & User Accounts

#### User Story: Account Registration
    As a user, I want to register an account so that I can make and manage my bookings.

#### Acceptance Criteria
- Registration form includes:
  - First name
  - Last name
  - Email
  - Phone
  - Password
- Email input must be validated for correct __format.__
- Password must be at least __8 characters__ long.
- Password confirmation must match the original password.
- Clear __validation error messages__ are displayed for invalid input.
- After successful registration, the user is automatically __authenticated and logged in.__
- The navigation bar reflects the user's __authentication status.__

---

#### User Story: User Login
    As a user, I want to log into my account so that I can access and manage my bookings.

#### Acceptance Criteria:
- Login form includes:
  - Email
  - Password
- Clear __error messages__ displayed for invalid credentials.
- __Successful login__ redirects the user to the appropriate __dashboard__ based on their __role.__
- __Session persists__ across pages until the user logs out.

---

#### User Story: User Logout
    As a logged-in user, I want to log out of my account so that my information remains secure.

#### Acceptance Criteria:
- __Logout option__ is visible when the user is logged in.
- __Successful logout__ clears the __session.__
- User is __redirected to the home page__ after logout.

---

#### User Story: Table Reservation
    As a customer, I want to make a table reservation so that I can dine at the restaurant.

#### Acceptance Criteria:
- Reservation form includes:
  - __Date, time, and number of guests.__
  - __Real-time availability checking.__
  - __Contact information fields__ (auto-filled for logged-in users).
  - Optional special requests field.
- __Confirmation message__ displayed upon successful booking.
- __Email confirmation__ sent (to be implemented in Django).

---

#### User Story: View Reservations
    As a customer, I want to see all my reservations so that I can keep track of my upcoming visits.

#### Acceptance Criteria:
- __Separate tabs__ for __upcoming__ and __past bookings.__
- Display all __booking details__: date, time, number of guests, table, status.
- Show __special requests__ if any.
- Include __visual status indicators__ for booking status.

---

#### User Story: Cancel Reservation
    As a customer, I want to cancel a reservation so that I can free up the table if my plans change.

#### Acceptance Criteria:
- __Cancel button__ visible for __upcoming bookings.__
- __Confirmation dialog__ before cancellation.
- __Success message__ displayed after cancellation.
- Booking __status updated to "cancelled".__

---

#### User Story: Staff/Admin View Reservations
    As a staff/admin, I want to see all reservations so that I can manage restaurant capacity.

#### Acceptance Criteria:
- __Table view__ of all bookings.
- __Search functionality__ by customer name, email, or booking ID.
- __Filter by status__: pending, confirmed, completed, cancelled
- __Sort by date/time__.
- __Export functionality__ for reservation data.

---

#### User Story: Confirm Reservation
    As a staff/admin, I want to confirm pending bookings so that customers know their reservation is comfirmed.


#### Acceptance Criteria:
- __Confirm button__ available for __pending bookings__
- Booking __status updates to "confirmed"__
- __Confirmation notification__ sent to customer __via email__

---

#### User Story: Decline Reservation
    As a staff/admin, I want to decline pending bookings when tables are not available or for operational reasons, so that I can effectively manage restaurant capacity.

#### Acceptance Criteria:
- __Decline button__ available for __pending bookings__
- Booking __status updates to "cancelled"__
- __Notification__ sent to the customer __via email__

---

#### User Story: Complete Reservation

    As a staff/admin, I want to mark confirmed bookings as completed after customers have finished dining, so that I can keep booking records accurate and up to date**.

#### Acceptance Criteria:
- __Complete button__ available for __confirmed bookings.__
- Booking __status updates to "completed".__

---

#### User Story: View Booking Statistics

    As a staff/admin, I want to view booking statistics so that I can plan restaurant operations effectively.

#### Acceptance Criteria:
- Display __today’s bookings count__
- Display __tomorrow’s bookings count__
- Display __pending approvals count__
- Display __total upcoming bookings__

---

#### User Story: View Booking Statistics

    As a staff/admin, I want to view booking statistics so that I can plan restaurant operations effectively.

#### Acceptance Criteria:
- Display __today’s bookings count.__
- Display __tomorrow’s bookings count.__
- Display __number of pending approvals.__
- Display __total number of upcoming bookings.__

---

#### User Story: Manage Restaurant Tables

    As an admin, I want to view all restaurant tables so that I can manage seating capacity effectively.

#### Acceptance Criteria:
- Display all tables with __table number__, __capacity__, and __location.__
- Show __current availability status__
- Present tables in a __visual grid layout__

---

## 4. Design & Wireframes

The Celtic Spoon website was designed with a **minimalist and user-friendly approach**, focusing on easy navigation and clear presentation of menu items, reservations, and restaurant information.

---

### Wireframes

- **Homepage:** highlights featured dishes, restaurant ambiance, and navigation links  
- **Menu Page:** displays categories, items, and signature dishes  
- **Reservation Page:** form for table booking with date, time, guests, and special requests  
- **Dashboard (Customer):** view upcoming/past bookings and manage reservations  
- **Dashboard (Staff/Admin):** view all reservations, confirm/decline bookings, manage tables

---

### Design Notes

- Clean layout with responsive design for mobile and desktop  
- Consistent color palette and typography to reflect the Celtic theme  
- Buttons and forms are easily accessible and clearly labeled  
- Visual hierarchy emphasizes key content such as specials and booking call-to-action

---

### Assets / Wireframe Images

- Placeholder for wireframe images:
  - ![Homepage Wireframe](docs/homepage-wireframe.png)  
  - ![Menu Page Wireframe](docs/menu-wireframe.png)  
  - ![Reservation Page Wireframe](docs/reservation-wireframe.png)  
  - ![Customer Dashboard Wireframe](docs/customer-dashboard-wireframe.png)  
  - ![Staff/Admin Dashboard Wireframe](docs/admin-dashboard-wireframe.png)

> Note: Actual wireframe images can be added to the `docs/` folder. These placeholders ensure links work and images can be included later.

---

## 5. Database Schema

The database is designed using Django ORM and follows a relational structure to support authentication, reservations, and restaurant capacity management.

---

### User Model

Extends Django’s built-in authentication system.

**Relationships:**
- One User can have multiple Reservations

---

### Table Model

Represents physical restaurant tables.

**Relationships:**
- One Table can have multiple Reservations

---

### Reservation Model

Handles booking data and lifecycle.

**Business Logic:**
- A reservation must not exceed table capacity
- No double-booking allowed for the same table at the same date/time
- Only confirmed bookings can be marked as completed
- Cancelled bookings remain stored for record tracking

---

### Relationships Overview

- **User (1) → (Many) Reservations**
- **Table (1) → (Many) Reservations**
- Admin/Staff users manage Reservations and Tables


The full Entity-Relationship (ER) Diagram and detailed entity structure can be accessed here:

[View ER Diagram (PDF)](https://drive.google.com/file/d/1CQ9S7YLMs-KYVGGQj0jHk-Fhb2R172fM/view?usp=share_link)

---

## 6. Features / Key Highlights

The Celtic Spoon booking system provides a reservation management system with role-based access for customers and staff/admin users.

---

### Authentication

- User registration with form validation
- Secure login and logout using Django authentication
- Automatic login after registration
- Navigation updates based on authentication status

---

### Customer Features

- Create a table reservation (date, time, number of guests, special requests)
- Prevent double-booking of tables
- Capacity validation based on table size
- View upcoming and past reservations
- Cancel upcoming reservations
- Visual status indicators (pending / confirmed / completed / cancelled)

---

### Staff / Admin Features

- View all reservations in a table layout
- Confirm or decline pending bookings
- Mark confirmed reservations as completed
- Search reservations by name, email, or booking ID
- Filter reservations by status
- View booking statistics (today, tomorrow, pending, upcoming)

---

### Table Management (Admin)

- View all restaurant tables
- See table number, capacity, and location
- View availability status

---

### Core Business Rules

- A reservation cannot exceed table capacity
- No double-booking allowed for the same table, date, and time
- Only confirmed bookings can be marked as completed
- Cancelled reservations remain stored for record keeping

---

## 7. Security Features

The Celtic Spoon booking system implements essential security measures using Django’s built-in protections and best practices.

---

### Authentication & Authorization

- Secure user authentication using Django’s built-in authentication system.
- Role-based access control (customer / staff / admin).
- Restricted access to admin-only pages and actions.
- Users can only view and manage their own reservations.

---

### Data Protection

- Passwords are securely stored using Django’s password hashing system.
- Sensitive actions require authenticated sessions.
- Session management handled securely by Django.

---

### Form & Input Validation

- Server-side validation for all forms.
- Email format validation.
- Password strength requirements.
- Protection against invalid or malicious input.

---

### Built-in Django Security Features

- CSRF protection enabled by default.
- Protection against SQL injection through Django ORM.
- XSS protection via Django template escaping.

---

## 8. Technologies Used

The project is built using modern web development technologies for both backend and frontend functionality.

---

### Backend

- **Python**
- **Django**
- Django ORM for database management
- Django Authentication System

---

### Frontend

- **HTML5**
- **CSS3**
- **JavaScript**
- Bootstrap (for responsive design)

---

### Database

- PostgreSQL (Code Institute provided database)
- Relational database design using Django ORM

---

### Tools & Development

- Git & GitHub for version control
- VS Code (development environment)
- Google Drive (documentation hosting)

---

## 9. Testing Documentation

The Celtic Spoon booking system includes a plan for testing core functionality, form validation, and business logic for both customers and staff/admin users.

---

### Planned Manual Testing

- User registration and login with valid and invalid credentials
- Table reservation creation, modification, and cancellation
- Staff/admin actions: confirm, decline, complete reservations
- Booking lifecycle validation (pending → confirmed → completed/cancelled)
- Form input validation (email format, password length, number of guests)
- Navigation and role-based access control
- UI responsiveness on different devices

---

### Planned Automated Testing (Optional / Future)

- Django test framework could be used to test:
  - Models
  - Views
  - Forms
  - Permissions

---

### Notes

- Edge cases for booking conflicts and table capacity should be checked
- Email confirmation functionality will be tested in development environment

---

## 10. Deployment

The Celtic Spoon project can be deployed to a cloud platform or run locally for development.

---

### Local Development

1. Clone the repository:  
```bash
   git clone https://github.com/PDennise/the_celtic_spoon.git
```
  
2. Navigate to the project folder:
```bash
  cd celtic-spoon
```

3. Set up Python environment:
```bash
  python -m venv venv
  source venv/bin/activate   # Linux / macOS
  venv\Scripts\activate      # Windows
```

4. Install backend dependencies:
```bash
  pip install -r requirements.txt
```

5. Set up environment variables (if any):
```bash
  cp .env.example .env
```

6. Apply Django migrations:
```bash
  python manage.py migrate
```

7. Start development servers:
```bash
  python manage.py runserver   # Django backend
```