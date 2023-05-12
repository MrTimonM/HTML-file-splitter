def split_html_file(file_path, num_parts):
    # Read the HTML file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Calculate the size of each part
    total_length = len(html_content)
    part_size = total_length // num_parts

    # Split the HTML content into parts
    parts = [html_content[i:i+part_size] for i in range(0, total_length, part_size)]

    # Save each part to separate files
    for i, part in enumerate(parts):
        part_file_path = f'part{i+1}.html'
        with open(part_file_path, 'w', encoding='utf-8') as part_file:
            part_file.write(part)
        print(f'Saved part {i+1} to {part_file_path}')

# Example usage
split_html_file('all.html', 4)
