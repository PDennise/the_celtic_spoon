<div align="center">
  <p> The Celtic Spoon </p>
</div>
<div align="center">
  <img src="/assets/images/logo.png" alt="Home Page">
</div>

## Table of Contents 

1. [Project Overview](#1-project-overview)
2. [Live Preview](#live-preview)
3. [UX & User Stories](#ux--user-stories)
4. [Design & Wireframes](#design--frames)
5. [Database Schema](#database-schema)
6. [Features / Key Highlights](#features--key-highlights)
7. [Security Features](#security-features)
8. [Technologies Used](#technologies-used)
9. [Testing Documentation](#testing-documentation)
10. [Deployment](Deployment)
11. [Credits](#credits)

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

