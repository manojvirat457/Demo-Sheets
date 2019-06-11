import gspread
from  oauth2client.service_account import ServiceAccountCredentials
from tkinter import Tk
import tkinter



scope = ["https://www.googleapis.com/auth/spreadsheets.readonly",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.readonly","https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

client = gspread.authorize(creds)

sheet = client.open("demo").sheet1

rowCount = sheet.get_all_records()

window = Tk()
window.geometry("500x500")
window.title("SpreadSheet")
B = tkinter.Tk().Button(window, text ="Hello")


B.pack()
window.mainloop()

print(len(rowCount))

# indexNum = int(len(rowCount))

insertRow = [len(rowCount)+1,"Saravana", 9487334133]

sheet.insert_row(insertRow, len(rowCount)+2)

# sheet.add_rows(insertRow)
# ypeError: can only concatenate list (not "int") to list

# print(sheet)

