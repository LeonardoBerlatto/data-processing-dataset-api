from decimal import Decimal

from pydantic import BaseModel


class Sale(BaseModel):
    invoice_id: str = None
    branch: str
    city: str
    customer_type: str
    gender: str
    product_line: str
    unit_price: Decimal
    quantity: int
    tax: Decimal
    total: Decimal
    date: str
    time: str
    payment: str
    cogs: Decimal
    gross_margin_percentage: Decimal
    gross_income: Decimal
    rating: Decimal

    def to_dict(self):
        return {
            "Invoice ID": self.invoice_id,
            "Branch": self.branch,
            "City": self.city,
            "Customer type": self.customer_type,
            "Gender": self.gender,
            "Product line": self.product_line,
            "Unit price": self.unit_price,
            "Quantity": self.quantity,
            "Tax 5%": self.tax,
            "Total": self.total,
            "Date": self.date,
            "Time": self.time,
            "Payment": self.payment,
            "cogs": self.cogs,
            "gross margin percentage": self.gross_margin_percentage,
            "gross income": self.gross_income,
            "Rating": self.rating
        }
