from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.units import inch

def generate_receipt(filename, customer_name, items, total_amount, date):
    # Create the PDF document
    pdf = SimpleDocTemplate(filename, pagesize=A4)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Title of the receipt
    title = Paragraph("Payment Receipt", title_style)

    # Customer Information
    customer_info = Paragraph(f"Customer: {customer_name}<br/>Date: {date}", normal_style)

    # Table Data
    table_data = [["Item", "Quantity", "Price", "Total"]]
    for item in items:
        table_data.append([item['name'], item['quantity'], f"Rs{item['price']:.2f}", f"Rs{item['total']:.2f}"])

    # Add Total Amount
    table_data.append(["", "", "Total Amount", f"Rs{total_amount:.2f}"])

    # Create Table
    table = Table(table_data, colWidths=[3 * inch, 1 * inch, 1.5 * inch, 1.5 * inch])

    # Table Styling
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Build the PDF
    elements = [title, customer_info, table]
    pdf.build(elements)

# Example usage
if __name__ == "__main__":
    filename = "payment_receipt.pdf"
    customer_name = "Amit Sharma"
    items = [
        {"name": "Item 1", "quantity": 2, "price": 50.00, "total": 100.00},
        {"name": "Item 2", "quantity": 1, "price": 150.00, "total": 150.00},
    ]
    total_amount = 250.00
    date = "2024-09-03"

    generate_receipt(filename, customer_name, items, total_amount, date)
    print(f"Receipt generated: {filename}")
