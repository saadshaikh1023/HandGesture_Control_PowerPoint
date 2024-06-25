import convertapi

# Set your ConvertAPI secret key
convertapi.api_secret = 'RUWcvRr5rqjA997b'

# Specify the input PPT file path
input_ppt_file = "C:\pptTest\Presentation 3.pptx"

# Specify the output directory path
output_dir = 'C:\pptTest'

# Convert PPT to PNG
conversion_result = convertapi.convert('png', {'File': input_ppt_file}, from_format='ppt')

# Save the converted PNG files to the output directory
conversion_result.save_files(output_dir)

print(f"Conversion complete. PNG files saved to: {output_dir}")
