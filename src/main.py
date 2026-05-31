import tkinter as tk
from tkinter import ttk, messagebox

from destino import adicionar_destino, ver_destinos, consultar_destinos, atualizar_destino, remover_destino
from hotel import adicionar_hotel, ver_hoteis, consultar_hotel, atualizar_hotel, remover_hotel
from viajantes import adicionar_viajante, ver_viajantes, consultar_viajantes, atualizar_viajantes, remover_viajantes
from voo import adicionar_voo, ver_voos, consultar_voo, atualizar_voo, remover_voo
from viagem import adicionar_viagem, ver_viagens, consultar_viagem, atualizar_viagem, remover_viagem
from utils import get_logger

logger = get_logger("main_tkinter")

def mostrar_resultado(caixa_texto, conteudo):
    caixa_texto.config(state="normal")
    caixa_texto.delete("1.0", tk.END)
    if isinstance(conteudo, list):
        for item in conteudo:
            for chave, valor in item.items():
                caixa_texto.insert(tk.END, f"{chave}: {valor}\n")
            caixa_texto.insert(tk.END, "-" * 30 + "\n")
    elif isinstance(conteudo, dict):
        for chave, valor in conteudo.items():
            caixa_texto.insert(tk.END, f"{chave}: {valor}\n")
    else:
        caixa_texto.insert(tk.END, str(conteudo) + "\n")
    caixa_texto.config(state="disabled")


def criar_campo(frame_pai, texto_label, numero_linha):
    tk.Label(frame_pai, text=texto_label).grid(row=numero_linha, column=0, sticky="w", padx=5, pady=2)
    campo_entrada = tk.Entry(frame_pai, width=30)
    campo_entrada.grid(row=numero_linha, column=1, padx=5, pady=2)
    return campo_entrada


# ─── ABA VIAJANTES ───────────────────────────────────────────────────────────

def aba_viajantes(notebook):
    frame_viajantes = ttk.Frame(notebook)
    notebook.add(frame_viajantes, text="Viajantes")

    frame_formulario = tk.LabelFrame(frame_viajantes, text="Dados do Viajante")
    frame_formulario.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    entrada_nome          = criar_campo(frame_formulario, "Nome:",                       0)
    entrada_nascimento    = criar_campo(frame_formulario, "Nascimento (DD/MM/AAAA):",    1)
    entrada_nacionalidade = criar_campo(frame_formulario, "Nacionalidade:",              2)
    entrada_telefone      = criar_campo(frame_formulario, "Telefone:",                   3)
    entrada_email         = criar_campo(frame_formulario, "Email:",                      4)
    entrada_nif           = criar_campo(frame_formulario, "NIF:",                        5)
    entrada_interesses    = criar_campo(frame_formulario, "Interesses:",                 6)
    entrada_orcamento     = criar_campo(frame_formulario, "Orçamento (€):",              7)

    caixa_resultado = tk.Text(frame_viajantes, width=50, height=20, state="disabled")
    caixa_resultado.grid(row=0, column=1, padx=10, pady=10)

    def adicionar():
        resposta = adicionar_viajante(
            entrada_nome.get(), entrada_nascimento.get(), entrada_nacionalidade.get(),
            entrada_telefone.get(), entrada_email.get(), entrada_nif.get(),
            entrada_interesses.get(), entrada_orcamento.get()
        )
        if resposta[0] == 201:
            messagebox.showinfo("Sucesso", "Viajante adicionado!")
            logger.info(f"Viajante adicionado via GUI: {entrada_nome.get()}")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def ver():
        resposta = ver_viajantes()
        mostrar_resultado(caixa_resultado, resposta[1])

    def consultar():
        resposta = consultar_viajantes(entrada_nome.get())
        mostrar_resultado(caixa_resultado, resposta[1])

    def atualizar():
        nome_a_procurar = entrada_nome.get()
        resposta = atualizar_viajantes(
            nome_a_procurar, entrada_nome.get(), entrada_nascimento.get(),
            entrada_nacionalidade.get(), entrada_telefone.get(), entrada_email.get(),
            entrada_nif.get(), entrada_interesses.get(), entrada_orcamento.get()
        )
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Viajante atualizado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def remover():
        resposta = remover_viajantes(entrada_nome.get())
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Viajante removido!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    frame_botoes = tk.Frame(frame_viajantes)
    frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(frame_botoes, text="Adicionar", width=12, command=adicionar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Ver Todos", width=12, command=ver).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Consultar", width=12, command=consultar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Atualizar", width=12, command=atualizar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Remover",   width=12, command=remover).pack(side="left", padx=4)


# ─── ABA DESTINOS ────────────────────────────────────────────────────────────

def aba_destinos(notebook):
    frame_destinos = ttk.Frame(notebook)
    notebook.add(frame_destinos, text="Destinos")

    frame_formulario = tk.LabelFrame(frame_destinos, text="Dados do Destino")
    frame_formulario.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    entrada_id       = criar_campo(frame_formulario, "ID (consultar/atualizar/remover):", 0)
    entrada_pais     = criar_campo(frame_formulario, "País:",     1)
    entrada_cidade   = criar_campo(frame_formulario, "Cidade:",   2)
    entrada_tipo     = criar_campo(frame_formulario, "Tipo:",     3)
    entrada_atracoes = criar_campo(frame_formulario, "Atrações:", 4)

    caixa_resultado = tk.Text(frame_destinos, width=50, height=20, state="disabled")
    caixa_resultado.grid(row=0, column=1, padx=10, pady=10)

    def adicionar():
        resposta = adicionar_destino(
            entrada_pais.get(), entrada_cidade.get(),
            entrada_tipo.get(), entrada_atracoes.get()
        )
        if resposta[0] == 201:
            messagebox.showinfo("Sucesso", "Destino adicionado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def ver():
        resposta = ver_destinos()
        mostrar_resultado(caixa_resultado, resposta[1])

    def consultar():
        try:
            id_destino = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = consultar_destinos(id_destino)
        mostrar_resultado(caixa_resultado, resposta[1])

    def atualizar():
        try:
            id_destino = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = atualizar_destino(
            id_destino, entrada_pais.get(), entrada_cidade.get(),
            entrada_tipo.get(), entrada_atracoes.get()
        )
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Destino atualizado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def remover():
        try:
            id_destino = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = remover_destino(id_destino)
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Destino removido!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    frame_botoes = tk.Frame(frame_destinos)
    frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(frame_botoes, text="Adicionar", width=12, command=adicionar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Ver Todos", width=12, command=ver).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Consultar", width=12, command=consultar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Atualizar", width=12, command=atualizar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Remover",   width=12, command=remover).pack(side="left", padx=4)


# ─── ABA HOTÉIS ──────────────────────────────────────────────────────────────

def aba_hoteis(notebook):
    frame_hoteis = ttk.Frame(notebook)
    notebook.add(frame_hoteis, text="Hotéis")

    frame_formulario = tk.LabelFrame(frame_hoteis, text="Dados do Hotel")
    frame_formulario.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    entrada_id           = criar_campo(frame_formulario, "ID (consultar/atualizar/remover):", 0)
    entrada_nome         = criar_campo(frame_formulario, "Nome:",            1)
    entrada_localizacao  = criar_campo(frame_formulario, "Local:",           2)
    entrada_preco_noite  = criar_campo(frame_formulario, "Preço/noite (€):", 3)
    entrada_tipo         = criar_campo(frame_formulario, "Tipo:",            4)

    caixa_resultado = tk.Text(frame_hoteis, width=50, height=20, state="disabled")
    caixa_resultado.grid(row=0, column=1, padx=10, pady=10)

    def adicionar():
        resposta = adicionar_hotel(
            entrada_nome.get(), entrada_localizacao.get(),
            entrada_preco_noite.get(), entrada_tipo.get()
        )
        if resposta[0] == 201:
            messagebox.showinfo("Sucesso", "Hotel adicionado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def ver():
        resposta = ver_hoteis()
        mostrar_resultado(caixa_resultado, resposta[1])

    def consultar():
        try:
            id_hotel = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = consultar_hotel(id_hotel)
        mostrar_resultado(caixa_resultado, resposta[1])

    def atualizar():
        try:
            id_hotel = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = atualizar_hotel(
            id_hotel, entrada_nome.get(), entrada_localizacao.get(),
            entrada_preco_noite.get(), entrada_tipo.get()
        )
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Hotel atualizado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def remover():
        try:
            id_hotel = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = remover_hotel(id_hotel)
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Hotel removido!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    frame_botoes = tk.Frame(frame_hoteis)
    frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(frame_botoes, text="Adicionar", width=12, command=adicionar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Ver Todos", width=12, command=ver).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Consultar", width=12, command=consultar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Atualizar", width=12, command=atualizar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Remover",   width=12, command=remover).pack(side="left", padx=4)


# ─── ABA VOOS ────────────────────────────────────────────────────────────────

def aba_voos(notebook):
    frame_voos = ttk.Frame(notebook)
    notebook.add(frame_voos, text="Voos")

    frame_formulario = tk.LabelFrame(frame_voos, text="Dados do Voo")
    frame_formulario.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    entrada_id           = criar_campo(frame_formulario, "ID (consultar/atualizar/remover):", 0)
    entrada_companhia    = criar_campo(frame_formulario, "Companhia:",              1)
    entrada_origem       = criar_campo(frame_formulario, "Origem:",                 2)
    entrada_id_destino   = criar_campo(frame_formulario, "ID Destino:",             3)
    entrada_data_partida = criar_campo(frame_formulario, "Partida (DD/MM/AAAA):",  4)
    entrada_data_chegada = criar_campo(frame_formulario, "Chegada (DD/MM/AAAA):",  5)
    entrada_preco        = criar_campo(frame_formulario, "Preço (€):",              6)

    caixa_resultado = tk.Text(frame_voos, width=50, height=20, state="disabled")
    caixa_resultado.grid(row=0, column=1, padx=10, pady=10)

    def adicionar():
        try:
            id_destino = int(entrada_id_destino.get())
        except ValueError:
            messagebox.showerror("Erro", "ID Destino inválido.")
            return
        resposta = adicionar_voo(
            entrada_companhia.get(), entrada_origem.get(), id_destino,
            entrada_data_partida.get(), entrada_data_chegada.get(), entrada_preco.get()
        )
        if resposta[0] == 201:
            messagebox.showinfo("Sucesso", "Voo adicionado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def ver():
        resposta = ver_voos()
        mostrar_resultado(caixa_resultado, resposta[1])

    def consultar():
        try:
            id_voo = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = consultar_voo(id_voo)
        mostrar_resultado(caixa_resultado, resposta[1])

    def atualizar():
        try:
            id_voo     = int(entrada_id.get())
            id_destino = int(entrada_id_destino.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = atualizar_voo(
            id_voo, entrada_companhia.get(), entrada_origem.get(), id_destino,
            entrada_data_partida.get(), entrada_data_chegada.get(), entrada_preco.get()
        )
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Voo atualizado!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def remover():
        try:
            id_voo = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = remover_voo(id_voo)
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Voo removido!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    frame_botoes = tk.Frame(frame_voos)
    frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(frame_botoes, text="Adicionar", width=12, command=adicionar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Ver Todos", width=12, command=ver).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Consultar", width=12, command=consultar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Atualizar", width=12, command=atualizar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Remover",   width=12, command=remover).pack(side="left", padx=4)


# ─── ABA VIAGENS ─────────────────────────────────────────────────────────────

def aba_viagens(notebook):
    frame_viagens = ttk.Frame(notebook)
    notebook.add(frame_viagens, text="Viagens")

    frame_formulario = tk.LabelFrame(frame_viagens, text="Dados da Viagem")
    frame_formulario.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    entrada_id          = criar_campo(frame_formulario, "ID (consultar/atualizar/remover):",    0)
    entrada_id_voo_ida  = criar_campo(frame_formulario, "ID Voo Ida:",                         1)
    entrada_id_voo_volta= criar_campo(frame_formulario, "ID Voo Volta (vazio se n/a):",        2)
    entrada_nifs        = criar_campo(frame_formulario, "NIFs viajantes (separados por vírgula):", 3)
    entrada_id_hotel    = criar_campo(frame_formulario, "ID Hotel:",                           4)
    entrada_id_destino  = criar_campo(frame_formulario, "ID Destino:",                         5)

    caixa_resultado = tk.Text(frame_viagens, width=50, height=20, state="disabled")
    caixa_resultado.grid(row=0, column=1, padx=10, pady=10)

    def _ler_campos_viagem():
        try:
            id_voo_ida   = int(entrada_id_voo_ida.get())
            id_voo_volta = int(entrada_id_voo_volta.get()) if entrada_id_voo_volta.get().strip() else None
            lista_nifs   = [nif.strip() for nif in entrada_nifs.get().split(",") if nif.strip()]
            id_hotel     = int(entrada_id_hotel.get())
            id_destino   = int(entrada_id_destino.get())
            return id_voo_ida, id_voo_volta, lista_nifs, id_hotel, id_destino
        except ValueError:
            messagebox.showerror("Erro", "IDs inválidos. Verifique os campos.")
            return None

    def adicionar():
        campos = _ler_campos_viagem()
        if not campos:
            return
        resposta = adicionar_viagem(*campos)
        if resposta[0] == 201:
            messagebox.showinfo("Sucesso", "Viagem criada!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def ver():
        resposta = ver_viagens()
        mostrar_resultado(caixa_resultado, resposta[1])

    def consultar():
        try:
            id_viagem = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = consultar_viagem(id_viagem)
        mostrar_resultado(caixa_resultado, resposta[1])

    def atualizar():
        try:
            id_viagem = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        campos = _ler_campos_viagem()
        if not campos:
            return
        resposta = atualizar_viagem(id_viagem, *campos)
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Viagem atualizada!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    def remover():
        try:
            id_viagem = int(entrada_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")
            return
        resposta = remover_viagem(id_viagem)
        if resposta[0] == 200:
            messagebox.showinfo("Sucesso", "Viagem removida!")
        else:
            messagebox.showerror("Erro", str(resposta[1]))

    frame_botoes = tk.Frame(frame_viagens)
    frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(frame_botoes, text="Adicionar", width=12, command=adicionar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Ver Todas", width=12, command=ver).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Consultar", width=12, command=consultar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Atualizar", width=12, command=atualizar).pack(side="left", padx=4)
    tk.Button(frame_botoes, text="Remover",   width=12, command=remover).pack(side="left", padx=4)


# ─── JANELA PRINCIPAL ────────────────────────────────────────────────────────

def main():
    logger.info("Sistema tkinter iniciado.")
    janela_principal = tk.Tk()
    janela_principal.title("Gestor de Viagens")
    janela_principal.resizable(False, False)

    notebook_abas = ttk.Notebook(janela_principal)
    notebook_abas.pack(padx=10, pady=10, fill="both", expand=True)

    aba_viajantes(notebook_abas)
    aba_destinos(notebook_abas)
    aba_hoteis(notebook_abas)
    aba_voos(notebook_abas)
    aba_viagens(notebook_abas)

    janela_principal.mainloop()
    logger.info("Sistema tkinter encerrado.")


if __name__ == "__main__":
    main()
