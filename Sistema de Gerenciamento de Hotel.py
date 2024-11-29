import tkinter as tk
from tkinter import ttk, messagebox


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Hotel")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")

        # Dados simulados
        self.rooms = {101: "Livre", 102: "Sujo", 103: "Livre", 104: "Manutenção", 105: "Livre", 106: "Sujo", 107: "Livre", 108: "Manutenção" ,
                             109: "Livre", 110: "Livre", 111: "Livre", 112: "Manutenção", 113: "Livre", 114: "Livre", 115: "Sujo", 115: "Livre" ,
                             116: "Livre", 117: "Livre", 118: "Manutenção", 119: "Livre", 120: "Livre", 121: "Sujo", 122: "Livre", 123: "Livre" ,
                             124: "Livre", 125: "Livre", 201: "Manutenção", 202: "Livre", 203: "Manutenção", 204: "Livre", 205: "Sujo", 206: "Livre",
                             207: "Livre", 208: "Sujo", 209: "Manutenção", 210: "Sujo", 211: "Sujo", 212: "Livre", 213: "Livre", 214: "Livre",
                             215: "Manutenção", 215: "Livre", 216: "Livre", 217: "Livre", 218: "Sujo", 219: "Livre", 220: "Livre", 221: "Manutenção",
                             222: "Livre", 223: "Livre", 224: "Livre", 225: "Livre", 301: "Livre", 302: "Manutenção", 303: "Manutenção", 304: "Manutenção",
                             305: "Livre", 306: "Sujo", 307: "Sujo", 308: "Livre", 309: "Livre", 310: "Livre", 311: "Livre", 312: "Sujo",
                             313: "Livre", 314: "Livre", 315: "Manutenção", 315: "Livre", 316: "Manutenção", 317: "Manutenção", 318: "Manutenção", 319: "Livre",
                             320: "Livre", 321: "Sujo", 322: "Livre", 323: "Livre", 324: "Livre", 325:"Livre", 401: "Manutenção", 402: "Livre",
                             403: "Livre", 404: "Manutenção", 405: "Livre", 406: "Livre", 407: "Sujo", 408: "Livre", 409: "Sujo", 410: "Livre",
                             411: "Manutenção", 412: "Livre", 413: "Manutenção", 414: "Livre", 415: "Manutenção", 415: "Livre", 416: "Manutenção", 417: "Livre",
                             418: "Manutenção", 419: "Livre", 420: "Manutenção", 421: "Livre", 422: "Livre", 423: "Livre" , 424: "Livre", 425: "Livre"
                      }
        self.reservations = {}
        self.services = []
        self.financial_records = []  # Registro financeiro
        self.promotions = []  # Promoções de marketing
        self.housekeeping = {101: "Livre", 102: "Sujo", 103: "Livre", 104: "Manutenção", 105: "Livre", 106: "Sujo", 107: "Livre", 108: "Manutenção" ,
                             109: "Livre", 110: "Livre", 111: "Livre", 112: "Manutenção", 113: "Livre", 114: "Livre", 115: "Sujo", 115: "Livre" ,
                             116: "Livre", 117: "Livre", 118: "Manutenção", 119: "Livre", 120: "Livre", 121: "Sujo", 122: "Livre", 123: "Livre" ,
                             124: "Livre", 125: "Livre", 201: "Manutenção", 202: "Livre", 203: "Manutenção", 204: "Livre", 205: "Sujo", 206: "Livre",
                             207: "Livre", 208: "Sujo", 209: "Manutenção", 210: "Sujo", 211: "Sujo", 212: "Livre", 213: "Livre", 214: "Livre",
                             215: "Manutenção", 215: "Livre", 216: "Livre", 217: "Livre", 218: "Sujo", 219: "Livre", 220: "Livre", 221: "Manutenção",
                             222: "Livre", 223: "Livre", 224: "Livre", 225: "Livre", 301: "Livre", 302: "Manutenção", 303: "Manutenção", 304: "Manutenção",
                             305: "Livre", 306: "Sujo", 307: "Sujo", 308: "Livre", 309: "Livre", 310: "Livre", 311: "Livre", 312: "Sujo",
                             313: "Livre", 314: "Livre", 315: "Manutenção", 315: "Livre", 316: "Manutenção", 317: "Manutenção", 318: "Manutenção", 319: "Livre",
                             320: "Livre", 321: "Sujo", 322: "Livre", 323: "Livre", 324: "Livre", 325:"Livre", 401: "Manutenção", 402: "Livre",
                             403: "Livre", 404: "Manutenção", 405: "Livre", 406: "Livre", 407: "Sujo", 408: "Livre", 409: "Sujo", 410: "Livre",
                             411: "Manutenção", 412: "Livre", 413: "Manutenção", 414: "Livre", 415: "Manutenção", 415: "Livre", 416: "Manutenção", 417: "Livre",
                             418: "Manutenção", 419: "Livre", 420: "Manutenção", 421: "Livre", 422: "Livre", 423: "Livre" , 424: "Livre", 425: "Livre"
                      }  # Governança

        # Títulos e menus principais
        title_label = tk.Label(
            self.root, text="Sistema de Gerenciamento de Hotel",
            font=("Helvetica", 20, "bold"), bg="#4a90e2", fg="white"
        )
        title_label.pack(side=tk.TOP, fill=tk.X)

        menu_frame = tk.Frame(self.root, bg="#4a90e2")
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Botões do menu
        menu_buttons = [
            ("Gerenciar Reservas", self.manage_reservations),
            ("Check-in / Check-out", self.check_in_out),
            ("Gestão de Quartos", self.manage_rooms),
            ("Gestão da Governança", self.manage_housekeeping),
            ("Marketing e Vendas", self.manage_marketing_sales),
            ("Gerenciamento Financeiro", self.manage_financial),
            ("Relatórios", self.generate_reports),
            ("Sair", self.exit_program),
        ]

        for text, command in menu_buttons:
            btn = tk.Button(
                menu_frame, text=text, font=("Helvetica", 12), bg="#0066cc",
                fg="white", command=command, pady=10, padx=20
            )
            btn.pack(pady=5, fill=tk.X)

        # Exibe a interface de reservas ao iniciar
        self.manage_reservations()

    def add_scrollable_frame(self):
        """Adiciona um frame com barra de rolagem vertical."""
        canvas = tk.Canvas(self.main_frame, bg="#f0f0f0")
        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame

    def manage_rooms(self):
        """Gestão de Quartos."""
        self.clear_frame()
        title = tk.Label(self.main_frame, text="Gestão de Quartos", 
                         font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Frame com barra de rolagem
        room_status_frame = self.add_scrollable_frame()

        for room, status in self.rooms.items():
            tk.Label(room_status_frame, text=f"Quarto {room}: {status}", 
                     font=("Helvetica", 12), bg="#f0f0f0").pack(anchor="w", pady=5)

    def manage_financial(self):
        """Gerenciamento Financeiro."""
        self.clear_frame()
        title = tk.Label(
            self.main_frame, text="Gerenciamento Financeiro",
            font=("Helvetica", 16, "bold"), bg="#f0f0f0"
        )
        title.pack(pady=10)

        # Frame com barra de rolagem
        financial_frame = self.add_scrollable_frame()

        # Exibir registros financeiros
        for record in self.financial_records:
            tk.Label(financial_frame, text=f"{record['type']}: R${record['amount']} - {record['description']}",
                     bg="#f0f0f0").pack(anchor="w", pady=5)

        # Total de receitas
        total_income = sum(record["amount"] for record in self.financial_records if record["type"] == "Reserva")
        tk.Label(financial_frame, text=f"Receita Total: R${total_income}", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=10)

    def manage_marketing_sales(self):
        """Marketing e Vendas."""
        self.clear_frame()
        title = tk.Label(
            self.main_frame, text="Marketing e Vendas",
            font=("Helvetica", 16, "bold"), bg="#f0f0f0"
        )
        title.pack(pady=10)

        form_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Título da Promoção:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        promo_title = tk.Entry(form_frame, width=40)
        promo_title.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Descrição:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        promo_description = tk.Entry(form_frame, width=40)
        promo_description.grid(row=1, column=1, padx=5, pady=5)

        def add_promotion():
            title = promo_title.get()
            description = promo_description.get()
            if title and description:
                self.promotions.append({"title": title, "description": description})
                messagebox.showinfo("Sucesso", "Promoção adicionada com sucesso!")
                promo_title.delete(0, tk.END)
                promo_description.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")

        add_btn = tk.Button(form_frame, text="Adicionar Promoção", bg="#0066cc", fg="white", command=add_promotion)
        add_btn.grid(row=2, columnspan=2, pady=10)

        tk.Label(self.main_frame, text="Promoções Atuais:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=10)
        for promo in self.promotions:
            tk.Label(self.main_frame, text=f"Título: {promo['title']} - {promo['description']}", bg="#f0f0f0").pack(anchor="w")

    def manage_reservations(self):
        """Gerenciamento de Reservas."""
        self.clear_frame()
        title = tk.Label(self.main_frame, text="Gerenciamento de Reservas",
                         font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        form_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome do Hóspede:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        guest_name = tk.Entry(form_frame, width=30)
        guest_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Quarto:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        room_number = ttk.Combobox(form_frame, values=[r for r, s in self.rooms.items() if s == "Livre"], state="readonly")
        room_number.grid(row=1, column=1, padx=5, pady=5)

        def add_reservation():
            name = guest_name.get()
            room = room_number.get()
            if name and room:
                room = int(room)  # Converte para número
                # Verifica se o quarto já tem reservas
                if room not in self.reservations:
                    self.reservations[room] = []
                # Verifica se o limite de hóspedes foi atingido
                if len(self.reservations[room]) < 4:
                    self.reservations[room].append(name)
                    self.rooms[room] = "Reservado"
                    self.financial_records.append({"type": "Reserva", "amount": 200, "description": f"Reserva do quarto {room}"})
                    messagebox.showinfo("Sucesso", f"Reserva para {name} no quarto {room} adicionada com sucesso!")
                    guest_name.delete(0, tk.END)
                    room_number.set("")
                else:
                    messagebox.showerror("Erro", f"O quarto {room} já está com o limite de 4 hóspedes.")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")

        add_btn = tk.Button(form_frame, text="Adicionar Reserva", bg="#0066cc", fg="white", command=add_reservation)
        add_btn.grid(row=2, columnspan=2, pady=10)

        tk.Label(self.main_frame, text="Reservas Atuais:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=10)
        reservations_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        reservations_frame.pack(pady=10)

        for room, guests in self.reservations.items():
            tk.Label(reservations_frame, text=f"Quarto {room}: {', '.join(guests)}", bg="#f0f0f0").pack(anchor="w")



    def manage_housekeeping(self):
        """Gestão da Governança."""
        self.clear_frame()
        title = tk.Label(
            self.main_frame, text="Gestão da Governança",
            font=("Helvetica", 16, "bold"), bg="#f0f0f0"
        )
        title.pack(pady=10)

        # Frame com barra de rolagem
        housekeeping_frame = self.add_scrollable_frame()

        for room, status in self.housekeeping.items():
            frame = tk.Frame(housekeeping_frame, bg="#f0f0f0")
            frame.pack(anchor="w", pady=5)
            tk.Label(frame, text=f"Quarto {room}: {status}", bg="#f0f0f0", font=("Helvetica", 12)).pack(side=tk.LEFT)

            def update_status(r=room):
                self.housekeeping[r] = "Livre"
                self.rooms[r] = "Livre"  # Atualiza o status na lista principal de quartos
                messagebox.showinfo("Sucesso", f"O quarto {r} foi atualizado para 'Limpo'")
                self.manage_housekeeping()

            btn = tk.Button(frame, text="Marcar como Limpo", command=update_status, bg="#0066cc", fg="white")
            btn.pack(side=tk.RIGHT)

    def generate_reports(self):
        """Geração de Relatórios."""
        self.clear_frame()
        title = tk.Label(
            self.main_frame, text="Relatórios",
            font=("Helvetica", 16, "bold"), bg="#f0f0f0"
        )
        title.pack(pady=10)

        # Relatórios de ocupação
        total_rooms = len(self.rooms)
        occupied = sum(1 for status in self.rooms.values() if status == "Reservado")
        free = sum(1 for status in self.rooms.values() if status == "Livre")
        maintenance = sum(1 for status in self.rooms.values() if status == "Manutenção")

        tk.Label(self.main_frame, text=f"Total de Quartos: {total_rooms}", bg="#f0f0f0").pack(anchor="w", pady=5)
        tk.Label(self.main_frame, text=f"Quartos Ocupados: {occupied}", bg="#f0f0f0").pack(anchor="w", pady=5)
        tk.Label(self.main_frame, text=f"Quartos Livres: {free}", bg="#f0f0f0").pack(anchor="w", pady=5)
        tk.Label(self.main_frame, text=f"Quartos em Manutenção: {maintenance}", bg="#f0f0f0").pack(anchor="w", pady=5)

        # Relatórios financeiros
        total_income = sum(record["amount"] for record in self.financial_records)
        tk.Label(self.main_frame, text=f"Receita Total: R${total_income:.2f}", bg="#f0f0f0").pack(anchor="w", pady=10)

        # Governança
        dirty_rooms = sum(1 for status in self.housekeeping.values() if status == "Sujo")
        tk.Label(self.main_frame, text=f"Quartos Sujos: {dirty_rooms}", bg="#f0f0f0").pack(anchor="w", pady=5)

    def check_in_out(self):
        """Check-in e Check-out."""
        self.clear_frame()
        title = tk.Label(
            self.main_frame, text="Check-in e Check-out",
            font=("Helvetica", 16, "bold"), bg="#f0f0f0"
        )
        title.pack(pady=10)

        reservations_list = tk.Listbox(self.main_frame, width=70, height=15)
        reservations_list.pack(pady=10)

        for res in self.reservations:
            reservations_list.insert(tk.END, f"Quarto {res['room']} - Hóspede: {res['name']}")

        def check_out():
            selection = reservations_list.curselection()
            if selection:
                index = selection[0]
                room = self.reservations[index]['room']
                self.rooms[room] = "Livre"
                del self.reservations[index]
                messagebox.showinfo("Sucesso", "Check-out realizado com sucesso!")
                self.check_in_out()
            else:
                messagebox.showerror("Erro", "Selecione uma reserva para realizar o check-out.")

        check_out_btn = tk.Button(self.main_frame, text="Realizar Check-out", bg="#0066cc", fg="white", command=check_out)
        check_out_btn.pack(pady=10)

    def clear_frame(self):
        """Limpa o frame principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def exit_program(self):
        """Fecha o programa."""
        self.root.destroy()


# Inicialização do programa
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
