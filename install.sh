#!/data/data/com.termux/files/usr/bin/bash
# ============================================================
# 🚀 PL7 TERMUX - Instalador Automático
# ============================================================

# Cores
R='\033[91m'
G='\033[92m'
Y='\033[93m'
CY='\033[96m'
P='\033[95m'
W='\033[97m'
B='\033[1m'
E='\033[0m'

clear

echo -e "${CY}${B}"
echo "    ╔═══════════════════════════════════════════════╗"
echo "    ║                                               ║"
echo "    ║         🚀 PL7 TERMUX - INSTALADOR 🚀         ║"
echo "    ║                                               ║"
echo "    ╚═══════════════════════════════════════════════╝"
echo -e "${E}"
echo ""

echo -e "  ${Y}[*] Atualizando pacotes do Termux...${E}"
pkg update -y > /dev/null 2>&1
pkg upgrade -y > /dev/null 2>&1
echo -e "  ${G}✓ Pacotes atualizados!${E}"
echo ""

echo -e "  ${Y}[*] Instalando Python...${E}"
pkg install python -y > /dev/null 2>&1
echo -e "  ${G}✓ Python instalado!${E}"
echo ""

echo -e "  ${Y}[*] Instalando Git...${E}"
pkg install git -y > /dev/null 2>&1
echo -e "  ${G}✓ Git instalado!${E}"
echo ""

echo -e "  ${Y}[*] Instalando dependências Python...${E}"
pip install requests > /dev/null 2>&1
echo -e "  ${G}✓ Dependências instaladas!${E}"
echo ""

echo -e "  ${Y}[*] Configurando permissão de armazenamento...${E}"
termux-setup-storage > /dev/null 2>&1
echo -e "  ${G}✓ Permissões configuradas!${E}"
echo ""

# Remove versão antiga se existir
if [ -d "$HOME/pl7-termux" ]; then
    echo -e "  ${Y}[*] Removendo versão antiga...${E}"
    rm -rf "$HOME/pl7-termux"
fi

echo -e "  ${Y}[*] Clonando PL7 TERMUX do GitHub...${E}"
cd $HOME
git clone https://github.com/PL7DDEV/pl7-termux.git > /dev/null 2>&1
echo -e "  ${G}✓ Projeto clonado!${E}"
echo ""

# Cria comando atalho 'pl7'
echo -e "  ${Y}[*] Criando atalho 'pl7'...${E}"
echo "#!/data/data/com.termux/files/usr/bin/bash" > $PREFIX/bin/pl7
echo "python $HOME/pl7-termux/pl7.py" >> $PREFIX/bin/pl7
chmod +x $PREFIX/bin/pl7
echo -e "  ${G}✓ Atalho criado!${E}"
echo ""

echo -e "${G}${B}"
echo "    ╔═══════════════════════════════════════════════╗"
echo "    ║                                               ║"
echo "    ║       ✅ INSTALAÇÃO CONCLUÍDA! ✅            ║"
echo "    ║                                               ║"
echo "    ║     Digite '${W}pl7${G}' pra abrir a ferramenta!       ║"
echo "    ║                                               ║"
echo "    ╚═══════════════════════════════════════════════╝"
echo -e "${E}"
echo ""
