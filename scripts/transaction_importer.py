import datetime

INPUT_FILE = ""
OUTPUT_FILE = ""
DELIMITER = "\t"
SQL_INSTERT_STATEMENT = "INSERT INTO budget.Transactions (t_name, t_category, t_date, t_amount) VALUES ('{t_name}', '{t_category}', '{t_date}', {t_amount});"

def transaction_importer_main():
    sql_output = []
    with open(INPUT_FILE) as input_file:
        data_lines = input_file.readlines()
        for line in data_lines:
            data_vals = line.replace("\n","").split(DELIMITER)
            name = data_vals[0].replace("'", "''")
            category = data_vals[1]
            date = format_date(data_vals[2], '%m/%d/%Y')
            value = restrict_string(data_vals[3], "$-")
            sql_output.append(SQL_INSTERT_STATEMENT.format(t_name=name, t_category=category, t_date=date, t_amount=value))
    write_to_output(sql_output, OUTPUT_FILE)

def format_date(date_string, format_string):
    return datetime.datetime.strptime(date_string, format_string).date()

def restrict_string(target_string, restrict_chars):
    for char in restrict_chars:
        target_string = target_string.replace(char, "")
    return target_string

def write_to_output(lines, output_path):
    output_file = open(output_path, "w")
    for line in lines:
        output_file.write("{line}\n".format(line=line))
    output_file.close()

if __name__ == "__main__":
    transaction_importer_main()
