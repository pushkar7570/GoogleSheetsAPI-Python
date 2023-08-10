from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# Load credentials from the downloaded JSON file
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
credentials = flow.run_local_server()

# Create a service object for Google Sheets API
service = build('sheets', 'v4', credentials=credentials)

# Your Google Sheets ID
spreadsheet_id = '1ZqoDoe7IgikzFQ_dr7QR6VHS1mdJV9_4GMCauY9pD8w/edit#gid=0'

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    values = [[data['field1'], data['field2'], data['field3']]]  # Customize based on your data
    body = {'values': values}
    
    result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                                                    range='Sheet1',  # Customize sheet and range
                                                    valueInputOption='RAW',
                                                    insertDataOption='INSERT_ROWS',
                                                    body=body).execute()
    
    return jsonify({'message': 'Data added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
