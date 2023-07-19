import fpdf, os

def create_pdf(name):
    pdf = fpdf.FPDF()
    pdf.add_page()

    pdf.image(f'{name}.png', 0, 0, 200, 200)

    pdf.output(f"{name}_QR.pdf", "F")

    os.remove(f"{name}.png")

    return f"{name}_QR.pdf"