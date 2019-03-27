CREATE TABLE budget.Transactions
(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    t_name VARCHAR (30) NOT NULL,
    t_category VARCHAR (30) NOT NULL,
    t_date DATE NOT NULL,
    t_amount FLOAT NOT NULL,
    t_note VARCHAR (50)
)