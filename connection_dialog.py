import tkinter as tk
from tkinter import messagebox


class ConnectionDialog(tk.Toplevel):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.title("Connect to API")
        self.resizable(False, False)
        self.grab_set()
        self.confirmed = False

        self._url   = tk.StringVar(value="http://localhost:8888")
        self._token = tk.StringVar()

        tk.Label(self, text="API URL:").grid(
            row=0, column=0, padx=14, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self._url, width=40).grid(
            row=0, column=1, padx=10)

        tk.Label(self, text="X-API-Key:").grid(
            row=1, column=0, padx=14, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self._token,
                 width=40, show="*").grid(row=1, column=1, padx=10)

        tk.Button(self, text="Connect",
                  command=self._confirm).grid(
                      row=2, column=0, columnspan=2, pady=12)

        self.protocol("WM_DELETE_WINDOW", self._cancel)
        self.wait_window()

    def _confirm(self):
        if not self._url.get().startswith("http"):
            messagebox.showwarning("Input error", "Please enter a valid URL.")
            return
        self.confirmed = True
        self.destroy()

    def _cancel(self):
        self.destroy()

    @property
    def url(self) -> str:
        return self._url.get().rstrip("/")

    @property
    def token(self) -> str:
        return self._token.get()
