import csv

import gspread


def convert_to_sheets(csv_file):
  gc = gspread.oauth()

  # Open or create a new Google Sheets document
  # TODO: Replace 'Your Spreadsheet Name' with your preferred name of the new file.
  spreadsheet = gc.create('Your Spreadsheet Name')

  # List to store the CSV files to
  data = []

  # Opens the CSV file and appends each row to the list 'data'
  with open(csv_file, 'r', encoding='utf-8') as csv_file:
      csv_reader = csv.reader(csv_file)
      for row in csv_reader:
          data.append(row)

  #Gets the total rows of the CSV file
  rowCount = len(data) 

  #Gets the total columns of the CSV file, based on the longest row in the list.
  columnCount = len(max(data, key=len))

  try:
    #Calls the batch_update method and inserts the data from the CSV file to the newly created Google Sheets file.
    #By default, this script inserts data starting from A1.
    spreadsheet.sheet1.batch_update([{
        #R1C1 notation of the range that where data will be inserted.
        'range': f'R1C1:R{rowCount}C{columnCount}', 
        'values': data
    }])
    print("Data successfully uploaded to Google Sheets.")
    
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  convert_to_sheets(csv_file)
