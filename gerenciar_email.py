import imaplib
import email
from email.header import decode_header

# --- Configurações do Servidor de Email ---
IMAP_SERVER = "imap.gmail.com"  # Servidor IMAP do seu provedor
EMAIL_ADDRESS = "seu_email@gmail.com"
APP_PASSWORD = "sua_senha_de_aplicativo"

# --- Pastas de Destino ---
PASTA_IMPORTANTE = "Importante"
PASTA_PROMOCOES = "Promocoes"

def abrir_email():
    """A - Conecta ao servidor de email e abre a caixa de entrada."""
    try:
        # Conecta ao servidor usando SSL
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        # Faz login
        mail.login(EMAIL_ADDRESS, APP_PASSWORD)
        # Seleciona a caixa de entrada
        mail.select("inbox")
        print("Conexão com o email bem-sucedida.")
        return mail
    except Exception as e:
        print(f"Erro ao conectar ao email: {e}")
        return None

def processar_emails(mail):
    """Processa todos os emails não lidos na caixa de entrada."""
    # Procura por todos os emails não lidos
    status, messages = mail.search(None, "UNSEEN")

    if status != "OK":
        print("Nenhum email novo para processar.")
        return

    # Converte a lista de bytes de mensagens para uma lista de IDs
    email_ids = messages[0].split()

    for email_id in email_ids:
        print(f"\n--- Processando Email ID: {email_id.decode()} ---")
        status, msg_data = mail.fetch(email_id, "(RFC822)")

        if status == "OK":
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # B - Análise do Remetente
                    remetente = analise_remetente(msg)

                    # C - Análise do Assunto e Conteúdo
                    assunto, corpo = analise_assunto_conteudo(msg)

                    # D - Sugerir Resposta
                    sugestao = sugerir_resposta(remetente, assunto, corpo)
                    print(f"D - Sugestão de Resposta:\n{sugestao}")

                    # E - Mover para Pastas
                    mover_para_pastas(mail, email_id, remetente, assunto)

                    # F - Marcar como Lido
                    marcar_como_lido(mail, email_id)

                    # G - Arquivamento e Exclusão (Exemplo: excluir se for promoção)
                    arquivamento_exclusao(mail, email_id, remetente)

def analise_remetente(msg):
    """B - Extrai e analisa o remetente do email."""
    de = msg.get("From", "N/A")
    print(f"B - Remetente: {de}")
    # Ex: verificar se está em uma lista de contatos, se é de um domínio confiável, etc.
    return de

def analise_assunto_conteudo(msg):
    """C - Extrai e analisa o assunto e o conteúdo do email."""
    # Decodifica o assunto
    assunto, encoding = decode_header(msg["Subject"])[0]
    if isinstance(assunto, bytes):
        assunto = assunto.decode(encoding if encoding else "utf-8")
    print(f"C - Assunto: {assunto}")

    corpo = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    corpo = part.get_payload(decode=True).decode()
                    break
                except Exception as e:
                    print(f"Não foi possível decodificar o corpo do email: {e}")
                    corpo = "Corpo do email não pôde ser lido."
    else:
        try:
            corpo = msg.get_payload(decode=True).decode()
        except Exception as e:
            print(f"Não foi possível decodificar o corpo do email: {e}")
            corpo = "Corpo do email não pôde ser lido."

    print(f"C - Conteúdo (resumo): {corpo[:150]}...")
    # Ex: identificar palavras-chave, análise de sentimento, etc.
    return assunto, corpo

def sugerir_resposta(remetente, assunto, corpo):
    """D - Gera uma sugestão de resposta (simulado)."""
    if "reunião" in assunto.lower():
        return "Sugestão: 'Confirmado, estarei presente. Obrigado pelo convite!'"
    elif "problema" in assunto.lower() or "urgente" in corpo.lower():
        return "Sugestão: 'Recebido. Estou verificando a situação e retorno em breve.'"
    else:
        return "Sugestão: 'Obrigado por sua mensagem. Irei analisar e responderei assim que possível.'"

def mover_para_pastas(mail, email_id, remetente, assunto):
    """E - Move o email para uma pasta específica com base em regras."""
    if "empresa-importante.com" in remetente:
        print(f"E - Movendo email de {remetente} para a pasta '{PASTA_IMPORTANTE}'.")
        mail.copy(email_id, PASTA_IMPORTANTE)
    elif "promoção" in assunto.lower() or "oferta" in assunto.lower():
        print(f"E - Movendo email com assunto '{assunto}' para a pasta '{PASTA_PROMOCOES}'.")
        mail.copy(email_id, PASTA_PROMOCOES)

def marcar_como_lido(mail, email_id):
    """F - Marca o email como lido."""
    print("F - Marcando como lido.")
    mail.store(email_id, "+FLAGS", "\\Seen")

def arquivamento_exclusao(mail, email_id, remetente):
    """G - Arquiva ou exclui o email com base em regras."""
    # Exemplo: deletar emails de um remetente específico após mover
    if "spam@exemplo.com" in remetente:
        print(f"G - Excluindo email de {remetente}.")
        mail.store(email_id, "+FLAGS", "\\Deleted")

if __name__ == "__main__":
    # A - Abrir o email
    email_connection = abrir_email()

    if email_connection:
        processar_emails(email_connection)
        # Fecha a conexão e aplica as exclusões marcadas
        email_connection.expunge()
        email_connection.close()
        email_connection.logout()
        print("\nProcesso finalizado e conexão encerrada.")
