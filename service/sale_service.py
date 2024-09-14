from typing import Dict

import pandas as pd
from fastapi import Depends, HTTPException

from bootstrap import resolve
from data.dataset import load_dataset
from domain import Sale
from utils.generator import generate_new_id


def _row_to_dict(row: pd.Series) -> Dict[str, str]:
    column_to_attr = {
        'Invoice ID': 'invoice_id',
        'Branch': 'branch',
        'City': 'city',
        'Customer type': 'customer_type',
        'Gender': 'gender',
        'Product line': 'product_line',
        'Unit price': 'unit_price',
        'Quantity': 'quantity',
        'Tax 5%': 'tax',
        'Total': 'total',
        'Date': 'date',
        'Time': 'time',
        'Payment': 'payment',
        'cogs': 'cogs',
        'gross margin percentage': 'gross_margin_percentage',
        'gross income': 'gross_income',
        'Rating': 'rating'
    }

    # Create the dictionary with Sale attribute names as values
    return {attr: row[original_column] for original_column, attr in column_to_attr.items()}


class SalesService:
    dataset: pd.DataFrame

    def __init__(self, dataset: pd.DataFrame = resolve(pd.DataFrame)):
        super().__init__()
        self.dataset = dataset

    def get_sales(self, page_number: int, page_size: int):
        starting_index = page_number * page_size
        ending_index = starting_index + page_size

        desired_items = self.dataset.iloc[starting_index:ending_index].reset_index()
        records = desired_items.apply(_row_to_dict, axis=1).tolist()
        return records

    def get_sale(self, invoice_id: str):
        if invoice_id not in self.dataset.index:
            raise HTTPException(status_code=404, detail="Sale not found")

        sale = self.dataset.reset_index().query(f"`Invoice ID` == '{invoice_id}'").iloc[0]
        return _row_to_dict(sale)

    def create_sale(self, sale: Sale):
        sale.invoice_id = generate_new_id()

        new_sale_df = pd.DataFrame([sale.to_dict()]).set_index('Invoice ID')
        self.dataset = pd.concat([self.dataset, new_sale_df])
        return sale

    def update_sale(self, invoice_id: str, sale: Sale):
        if invoice_id not in self.dataset.index:
            raise HTTPException(status_code=404, detail="Sale not found")

        sale.invoice_id = invoice_id
        self.dataset.loc[invoice_id] = sale.to_dict()
        return sale

    def delete_sale(self, invoice_id: str):
        if invoice_id not in self.dataset.index:
            raise HTTPException(status_code=404, detail="Sale not found")

        self.dataset = self.dataset.drop(invoice_id)

    def df_to_dict(self):
        return self.dataset.reset_index().to_dict(orient="records")

