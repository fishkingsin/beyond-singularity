import pandas as pd

# Load the CSV file
csv_file_path = 'Beyond Singularity (Responses) - Form Responses 1.csv'  # Update this to the path of your CSV file
df = pd.read_csv(csv_file_path)

def convert_row_to_html(row):
    # Define the HTML template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Submission Detail - {row['Name']}</title>
    </head>
    <body>
        <p>Submission Timestamp: {row['Timestamp']}</p>
        <p>Submitted by: {row['Name']}</p>
        <div>
    """
    
    # Assuming links start from the 3rd column
    for link in row[2:]:
        if pd.notna(link):
            file_id = link.split('id=')[-1]
            description = "Description here"  # Update or modify as necessary
            html_template += f"""
                <div>
                    <p>{description}</p>
                    <img src="https://drive.google.com/thumbnail?id={file_id}&sz=w1000" alt="{description}" style="width:100%; max-width:1000px;">
                </div>
            """
    
    html_template += """
        </div>
    </body>
    </html>
    """
    return html_template

# Iterate over each row in the DataFrame and generate an HTML file
for index, row in df.iterrows():
    html_content = convert_row_to_html(row)
    file_name = f"submission_{index+1}.html"  # Generates a unique file name for each submission
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Generated {file_name}")
