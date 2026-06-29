#!/usr/bin/env python3
# ============================================================
# 🚀 PL7 TERMUX - File Injector
# GitHub: seu-usuario/pl7-termux
# ============================================================

import os
import sys
import time
import requests
from pathlib import Path

# ============================================================
# 🔧 CONFIGURAÇÃO (MUDE AQUI!)
# ============================================================

# 👉 COLE AQUI O CAMINHO ONDE OS ARQUIVOS SERÃO INJETADOS
INJECTION_PATH = "/sdcard/Download/PL7"

# 👉 SEU REPOSITÓRIO NO GITHUB (formato: usuario/repo)
GITHUB_REPO = "seu-usuario/pl7-termux"

# 👉 BRANCH DO GITHUB
GITHUB_BRANCH = "main"

# ============================================================
# 🎨 CORES
# ============================================================
class C:
    R = "\033[91m"      # Vermelho
    G = "\033[92m"      # Verde
    Y = "\033[93m"      # Amarelo
    B = "\033[94m"      # Azul
    P = "\033[95m"      # Roxo
    CY = "\033[96m"     # Ciano
    W = "\033[97m"      # Branco
    BOLD = "\033[1m"    # Negrito
    DIM = "\033[2m"     # Esmaecido
    BLINK = "\033[5m"   # Piscante
    END = "\033[0m"     # Reset
    
    # Gradiente
    @staticmethod
    def gradient(text, start_color, end_color):
        result = ""
        for i, char in enumerate(text):
            ratio = i / max(len(text) - 1, 1)
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            result += f"\033[38;2;{r};{g};{b}m{char}"
        return result + C.END

# ============================================================
# 🛠️ UTILIDADES
# ============================================================

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def typewriter(text, delay=0.02):
    """Efeito de digitação"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(label, duration=2):
    """Barra de carregamento animada"""
    width = 30
    steps = 50
    delay = duration / steps
    
    for i in range(steps + 1):
        filled = int(width * i / steps)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(100 * i / steps)
        
        color = C.R if percent < 33 else (C.Y if percent < 66 else C.G)
        
        sys.stdout.write(f"\r  {color}[{bar}] {percent}%{C.END} {C.CY}{label}{C.END}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(label, duration=1.5):
    """Spinner animado"""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r  {C.CY}{frames[i % len(frames)]} {label}{C.END}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r  {C.G}✓ {label}{C.END}                    \n")
    sys.stdout.flush()

# ============================================================
# 🎨 BANNER
# ============================================================

def banner():
    clear()
    
    # ASCII Art PL7
    logo = f"""
{C.CY}{C.BOLD}    ╔═══════════════════════════════════════════════╗{C.END}
{C.CY}{C.BOLD}    ║                                               ║{C.END}
{C.CY}{C.BOLD}    ║     {C.P}██████╗ ██╗     ███████╗{C.CY}                ║{C.END}
{C.CY}{C.BOLD}    ║     {C.P}██╔══██╗██║     ╚════██║{C.CY}                ║{C.END}
{C.CY}{C.BOLD}    ║     {C.P}██████╔╝██║         ██╔╝{C.CY}                ║{C.END}
{C.CY}{C.BOLD}    ║     {C.P}██╔═══╝ ██║        ██╔╝ {C.CY}                ║{C.END}
{C.CY}{C.BOLD}    ║     {C.P}██║     ███████╗   ██║  {C.CY}                ║{C.END}
{C.CY}{C.BOLD}    ║     {C.P}╚═╝     ╚══════╝   ╚═╝  {C.CY}                ║{C.END}
{C.CY}{C.BOLD}    ║                                               ║{C.END}
{C.CY}{C.BOLD}    ║          {C.Y}⚡ T E R M U X  I N J E C T O R ⚡{C.CY}     ║{C.END}
{C.CY}{C.BOLD}    ║                                               ║{C.END}
{C.CY}{C.BOLD}    ╚═══════════════════════════════════════════════╝{C.END}
"""
    print(logo)
    
    # Info bar
    print(f"  {C.DIM}┌─────────────────────────────────────────────────┐{C.END}")
    print(f"  {C.DIM}│{C.END} {C.G}●{C.END} Status: {C.G}{C.BOLD}ONLINE{C.END}      {C.CY}●{C.END} Versão: {C.W}{C.BOLD}1.0.0{C.END}     {C.DIM}│{C.END}")
    print(f"  {C.DIM}│{C.END} {C.Y}●{C.END} GitHub: {C.W}{GITHUB_REPO[:25]:<25}{C.END}     {C.DIM}│{C.END}")
    print(f"  {C.DIM}└─────────────────────────────────────────────────┘{C.END}")
    print()

# ============================================================
# 📋 MENU
# ============================================================

def show_menu():
    print(f"  {C.P}{C.BOLD}╔═══════════════════════════════════════════════╗{C.END}")
    print(f"  {C.P}{C.BOLD}║              {C.W}🎯 OPÇÕES DE INJEÇÃO 🎯{C.P}          ║{C.END}")
    print(f"  {C.P}{C.BOLD}╠═══════════════════════════════════════════════╣{C.END}")
    print(f"  {C.P}{C.BOLD}║                                               ║{C.END}")
    print(f"  {C.P}{C.BOLD}║  {C.CY}[{C.W}{C.BOLD}1{C.CY}]{C.END} {C.G}💎 Injetar Holograma{C.END}                   {C.P}{C.BOLD}║{C.END}")
    print(f"  {C.P}{C.BOLD}║  {C.CY}[{C.W}{C.BOLD}2{C.CY}]{C.END} {C.Y}🎯 Injetar HS (Headshot){C.END}              {C.P}{C.BOLD}║{C.END}")
    print(f"  {C.P}{C.BOLD}║  {C.CY}[{C.W}{C.BOLD}3{C.CY}]{C.END} {C.B}⚡ Injetar FPS Boost{C.END}                   {C.P}{C.BOLD}║{C.END}")
    print(f"  {C.P}{C.BOLD}║  {C.CY}[{C.W}{C.BOLD}4{C.CY}]{C.END} {C.R}🔥 Injetar TUDO (All-in-One){C.END}          {C.P}{C.BOLD}║{C.END}")
    print(f"  {C.P}{C.BOLD}║                                               ║{C.END}")
    print(f"  {C.P}{C.BOLD}║  {C.CY}[{C.W}{C.BOLD}0{C.CY}]{C.END} {C.R}🚪 Sair{C.END}                                {C.P}{C.BOLD}║{C.END}")
    print(f"  {C.P}{C.BOLD}║                                               ║{C.END}")
    print(f"  {C.P}{C.BOLD}╚═══════════════════════════════════════════════╝{C.END}")
    print()
    print(f"  {C.DIM}📁 Destino: {C.W}{INJECTION_PATH}{C.END}")
    print()

# ============================================================
# 💉 SISTEMA DE INJEÇÃO
# ============================================================

def baixar_arquivo(file_path):
    """Baixa um arquivo do GitHub"""
    url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}/{file_path}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            return r.content
        return None
    except Exception as e:
        return None

def listar_arquivos_pasta(pasta):
    """Lista todos os arquivos de uma pasta no GitHub via API"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/files/{pasta}?ref={GITHUB_BRANCH}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            return [item["path"] for item in r.json() if item["type"] == "file"]
        return []
    except:
        return []

def injetar(modulo, nome_visual, emoji, cor):
    """Função principal de injeção"""
    clear()
    
    # Banner do módulo
    print()
    print(f"  {cor}{C.BOLD}╔═══════════════════════════════════════════════╗{C.END}")
    print(f"  {cor}{C.BOLD}║         {emoji} INJETANDO {nome_visual.upper()}{' ' * (32 - len(nome_visual))}║{C.END}")
    print(f"  {cor}{C.BOLD}╚═══════════════════════════════════════════════╝{C.END}")
    print()
    
    # Animação inicial
    typewriter(f"  {C.CY}[*] Inicializando módulo de injeção...{C.END}", 0.02)
    time.sleep(0.3)
    typewriter(f"  {C.CY}[*] Conectando ao GitHub...{C.END}", 0.02)
    time.sleep(0.3)
    
    # Lista arquivos do módulo
    spinner(f"Buscando arquivos de {nome_visual}...", 1.2)
    
    arquivos = listar_arquivos_pasta(modulo)
    
    if not arquivos:
        print()
        print(f"  {C.R}{C.BOLD}❌ ERRO: Nenhum arquivo encontrado!{C.END}")
        print(f"  {C.DIM}Verifique se o repo '{GITHUB_REPO}' existe{C.END}")
        print(f"  {C.DIM}e se a pasta 'files/{modulo}' está populada{C.END}")
        print()
        input(f"  {C.DIM}Pressione Enter pra voltar...{C.END}")
        return
    
    print(f"  {C.G}✓ Encontrados {C.BOLD}{len(arquivos)}{C.END}{C.G} arquivo(s){C.END}")
    print()
    
    # Cria pasta destino
    os.makedirs(INJECTION_PATH, exist_ok=True)
    
    # Injeta cada arquivo
    print(f"  {C.Y}{'─' * 47}{C.END}")
    print(f"  {C.Y}{C.BOLD}  📥 INICIANDO INJEÇÃO...{C.END}")
    print(f"  {C.Y}{'─' * 47}{C.END}")
    print()
    
    sucesso = 0
    falhas = 0
    
    for i, arquivo in enumerate(arquivos, 1):
        nome_arquivo = os.path.basename(arquivo)
        print(f"  {C.CY}[{i}/{len(arquivos)}]{C.END} {C.W}{nome_arquivo}{C.END}")
        
        loading_bar(f"Baixando {nome_arquivo}...", 0.8)
        
        conteudo = baixar_arquivo(arquivo)
        
        if conteudo:
            # Mantém a estrutura de pastas dentro do destino
            relative = arquivo.replace(f"files/{modulo}/", "")
            dest = os.path.join(INJECTION_PATH, relative)
            os.makedirs(os.path.dirname(dest) if os.path.dirname(dest) else INJECTION_PATH, exist_ok=True)
            
            try:
                with open(dest, "wb") as f:
                    f.write(conteudo)
                print(f"  {C.G}  ✓ Injetado em: {C.DIM}{dest}{C.END}")
                sucesso += 1
            except Exception as e:
                print(f"  {C.R}  ✗ Erro: {e}{C.END}")
                falhas += 1
        else:
            print(f"  {C.R}  ✗ Falha no download{C.END}")
            falhas += 1
        
        print()
        time.sleep(0.2)
    
    # Resultado final
    print(f"  {C.G}{'─' * 47}{C.END}")
    print()
    print(f"  {C.G}{C.BOLD}╔═══════════════════════════════════════════════╗{C.END}")
    print(f"  {C.G}{C.BOLD}║          ✅ INJEÇÃO CONCLUÍDA! ✅            ║{C.END}")
    print(f"  {C.G}{C.BOLD}╠═══════════════════════════════════════════════╣{C.END}")
    print(f"  {C.G}{C.BOLD}║{C.END}  {C.W}Módulo:{C.END} {cor}{nome_visual:<35}{C.END}    {C.G}{C.BOLD}║{C.END}")
    print(f"  {C.G}{C.BOLD}║{C.END}  {C.W}Sucesso:{C.END} {C.G}{C.BOLD}{sucesso:<34}{C.END}    {C.G}{C.BOLD}║{C.END}")
    print(f"  {C.G}{C.BOLD}║{C.END}  {C.W}Falhas:{C.END}  {C.R}{C.BOLD}{falhas:<34}{C.END}    {C.G}{C.BOLD}║{C.END}")
    print(f"  {C.G}{C.BOLD}║{C.END}  {C.W}Destino:{C.END} {C.CY}{INJECTION_PATH[:30]:<30}{C.END}      {C.G}{C.BOLD}║{C.END}")
    print(f"  {C.G}{C.BOLD}╚═══════════════════════════════════════════════╝{C.END}")
    print()
    
    input(f"  {C.DIM}Pressione Enter pra voltar ao menu...{C.END}")

# ============================================================
# 🚀 MAIN LOOP
# ============================================================

def main():
    while True:
        banner()
        show_menu()
        
        try:
            opcao = input(f"  {C.CY}{C.BOLD}➜ Digite o número: {C.END}").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            sair()
        
        if opcao == "1":
            injetar("holograma", "Holograma", "💎", C.G)
        
        elif opcao == "2":
            injetar("hs", "HS", "🎯", C.Y)
        
        elif opcao == "3":
            injetar("fpsboost", "FPS Boost", "⚡", C.B)
        
        elif opcao == "4":
            # Injeta TUDO
            clear()
            print()
            print(f"  {C.R}{C.BOLD}╔═══════════════════════════════════════════════╗{C.END}")
            print(f"  {C.R}{C.BOLD}║       🔥 MODO ALL-IN-ONE ATIVADO 🔥          ║{C.END}")
            print(f"  {C.R}{C.BOLD}╚═══════════════════════════════════════════════╝{C.END}")
            print()
            typewriter(f"  {C.Y}⚠ Isso vai injetar TODOS os módulos!{C.END}", 0.02)
            print()
            confirma = input(f"  {C.CY}Continuar? (s/n): {C.END}").strip().lower()
            
            if confirma == "s":
                injetar("holograma", "Holograma", "💎", C.G)
                injetar("hs", "HS", "🎯", C.Y)
                injetar("fpsboost", "FPS Boost", "⚡", C.B)
                
                print()
                print(f"  {C.G}{C.BOLD}🎉 TODOS OS MÓDULOS FORAM INJETADOS! 🎉{C.END}")
                print()
                input(f"  {C.DIM}Pressione Enter pra continuar...{C.END}")
        
        elif opcao == "0":
            sair()
        
        else:
            print()
            print(f"  {C.R}❌ Opção inválida! Tente novamente.{C.END}")
            time.sleep(1.5)

def sair():
    clear()
    print()
    print(f"  {C.CY}{C.BOLD}╔═══════════════════════════════════════════════╗{C.END}")
    print(f"  {C.CY}{C.BOLD}║                                               ║{C.END}")
    print(f"  {C.CY}{C.BOLD}║         {C.P}👋 OBRIGADO POR USAR O PL7! 👋{C.CY}     ║{C.END}")
    print(f"  {C.CY}{C.BOLD}║                                               ║{C.END}")
    print(f"  {C.CY}{C.BOLD}║              {C.W}Até a próxima! 🚀{C.CY}              ║{C.END}")
    print(f"  {C.CY}{C.BOLD}║                                               ║{C.END}")
    print(f"  {C.CY}{C.BOLD}╚═══════════════════════════════════════════════╝{C.END}")
    print()
    sys.exit(0)

# ============================================================
# INÍCIO
# ============================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sair()
