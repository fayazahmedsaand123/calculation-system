# 🧮 Calculation Management System

A professional Calculation Management System built with **Python Flask**, **MySQL**, and **Bootstrap 5**.

## 🌟 Features

- ➕ Addition, Subtraction, Multiplication, Division
- 📊 Percentage & Average Calculations
- ⚡ AJAX Calculate — No Page Reload
- ✏️ Edit Calculation with Modal — No Page Reload
- 🗑️ Delete Calculation with AJAX — No Page Reload
- 📜 Calculation History Table
- 🔒 Safe MySQL Connection with `get_db()`
- 📱 Responsive Bootstrap 5 UI

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Database | MySQL (XAMPP) |
| Frontend | HTML5, Bootstrap 5, JavaScript |
| Templates | Jinja2 |
| Version Control | Git & GitHub |

## 🗄️ Database Schema

```sql
CREATE TABLE calculations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number1 DECIMAL(10,4) NOT NULL,
    number2 DECIMAL(10,4) NOT NULL,
    operation VARCHAR(20) NOT NULL,
    result VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/fayazahmedsaand123/calculation-system.git
cd calculation-system
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install flask mysql-connector-python python-dotenv
```

### 4. Create `.env` file
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=
DB_NAME=calculation_system


### 5. Setup Database
- Start XAMPP (Apache + MySQL)
- Open phpMyAdmin
- Create database `calculation_system`
- Run the SQL schema above

### 6. Run the project
```bash
python app.py
```

Open browser: **http://127.0.0.1:5000/calculate**

## 👨‍💻 Developer

**Fayaz Ahmed Saand**
Full Stack Web Developer
- PHP, Laravel, MySQL
- Python, Flask
- HTML, CSS, Bootstrap, JavaScript, AJAX

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
