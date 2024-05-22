import openpyxl
from openpyxl.utils import get_column_letter

def create_excel_history(
        nama, 
        umur, 
        gender,
        status,
        pola_makan, 
        perokok, 
        alkohol, 
        obat_terlarang,
        bmi, 
        ahh,
        sisa_umur
    ):
    # Load the workbook (if it exists) or create a new one
    try:
        workbook = openpyxl.load_workbook("life_expectancy_history.xlsx")
        sheet = workbook.active
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Life Expectancy History"

        # Write column headers
        headers = [
            "Nama", 
            "Umur", 
            "Gender", 
            "Status", 
            "Pola Makan", 
            "Perokok", 
            "Alkohol", 
            "Obat Terlarang", 
            "BMI", 
            "Angka Harapan Hidup", 
            "Sisa Umur"]
        for col, header in enumerate(headers, start=1):
            sheet.cell(row=1, column=col).value = header

    # Add data to the worksheet
    data = [
            [
            nama, 
            umur,
            gender,
            status,
            pola_makan, 
            perokok, 
            alkohol, 
            obat_terlarang, 
            bmi, 
            ahh,
            sisa_umur,
        ],
        # Add more data here...
    ]

    headers = [
            "Nama", 
            "Umur", 
            "Gender", 
            "Status", 
            "Pola Makan", 
            "Perokok", 
            "Alkohol", 
            "Obat Terlarang", 
            "BMI", 
            "Angka Harapan Hidup", 
            "Sisa Umur"
        ]
    # Find the last row with data
    last_row = sheet.max_row + 1

    for row, row_data in enumerate(data, start=last_row):
        for col, value in enumerate(row_data, start=1):
            sheet.cell(row=row, column=col).value = value

    # Auto-fit column widths
    for col in range(1, len(headers) + 1):
        column_letter = get_column_letter(col)
        sheet.column_dimensions[column_letter].auto_size = True

    # Save the workbook
    workbook.save("life_expectancy_history.xlsx")

def display_history(name=None):
    # Load the workbook
    workbook = openpyxl.load_workbook("life_expectancy_history.xlsx")
    sheet = workbook.active

    # Read data from the worksheet
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    # Filter data based on the entered name
    if name:
        data = [row for row in data if row[0] == name]
    
    if not data:
        print("Data tidak ditemukan.")
        return

    # Print the history
    print("Life Expectancy History:")
    print("------------------------")
    for row in data:
        print(f"Nama\t\t\t: {row[0]}\nUmur\t\t\t: {row[1]}\nGender\t\t\t: {row[2]}\nStatus\t\t\t: {row[3]}\nPola Makan\t\t: {row[4]}\nPerokok\t\t\t: {row[5]}\nAlkohol\t\t\t: {row[6]}\nObat Terlarang\t\t: {row[7]}\nBMI\t\t\t: {row[8]:.2f}\nAngka Harapan Hidup\t: {row[9]}\nSisa Umur\t\t: {row[10]}")