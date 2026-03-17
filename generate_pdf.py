from fpdf import FPDF
import os

# Function to read content from text files

def read_text_files(filenames):
    content = ""
    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content += file.read() + '\n'
    return content

# Generate PDF

def generate_pdf(q_and_a_pairs, code_examples, output_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Q&A and Code Examples', ln=True, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', '', 12)
    for q_a in q_and_a_pairs:
        question, answer = q_a
        pdf.multi_cell(0, 10, f'Q: {question}', 0)
        pdf.multi_cell(0, 10, f'A: {answer}', 0)
        pdf.ln(5)

    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 10, 'Code Examples:', ln=True)
    pdf.ln(5)
    pdf.set_font('Arial', '', 10)
    for code in code_examples:
        pdf.multi_cell(0, 10, code, 0)
        pdf.ln(5)

    pdf.output(output_filename)

# Main function

def main():
    filenames = ['Notes.txt', 'OOPSNotes.txt', 'medium.txt']
    content = read_text_files(filenames)
    q_and_a_pairs = []  # Assume we extract Q&A pairs from content
    code_examples = []  # Assume we extract code examples from content

    # TODO: Add logic to parse content into q_and_a_pairs and code_examples

    output_filename = 'output.pdf'
    generate_pdf(q_and_a_pairs, code_examples, output_filename)
    print(f"PDF generated: {output_filename}")

if __name__ == '__main__':
    main()