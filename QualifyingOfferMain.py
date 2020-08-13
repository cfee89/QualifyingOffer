from tkinter import messagebox

from src.controller.QualifyingOfferController import QualifyingOfferController
from src.servicewrappers.HtmlWrapper import HtmlWrapper


def main():
    html_wrapper = HtmlWrapper()
    controller = QualifyingOfferController(html_wrapper)
    qualifyingOffer = controller.determineQualifyingOffer()

    print("Minimum Qualifying Offer is: ", qualifyingOffer)

    messagebox.showinfo("Qualifying Offer Calculator","Minimum Qualifying Offer is: " + qualifyingOffer)


if __name__ == "__main__":
    main()
